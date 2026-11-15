"""Extract SAT question-bank PDF into questions.json / questions.csv + cropped PNGs.

Usage: python -I extract_sat.py <pdf> <out_dir> [limit] [--no-images]
  out_dir/questions.json, out_dir/questions.csv, out_dir/q/<id>/{stem,a,b,c,d,rationale}.png

The PDF draws all math/graphs as vector paths (no text), so each question part is
cropped straight from the PDF into a transparent grayscale PNG. Text fields keep the
plain-English parts only (math shows up as gaps).
"""
import csv
import json
import re
import sys
from pathlib import Path

import pymupdf

SCALE = 2.0          # render scale (144 dpi) — crisp on retina at ~1x CSS width
PAD = 3              # pt padding around crops
LEFT = 16            # pt — page left margin; stem/rationale crops start here for alignment
GAP = 4              # pt gap between stitched page segments

args = [a for a in sys.argv[1:] if not a.startswith("--")]
NO_IMAGES = "--no-images" in sys.argv
pdf_path, out_dir = Path(args[0]), Path(args[1])
limit = int(args[2]) if len(args) > 2 else None
doc = pymupdf.open(pdf_path)


# word fragments the PDF splits before a 't' (kerning): "cer tain", "ver tex", "par ticipants"
SPLIT_FRAGS = ("ver|cer|par|ar|shir|shor|wor|star|tor|repor|adver|conver|suppor|quar|fur|impor|"
               "propor|proper|sor|por|cour|depar|sur|ser|inver|exper|aler|ear|mor|hor|ster")


def clean(t):
    t = re.sub(r"\s?’\s?", "’", t)                         # It ’ s -> It’s
    t = re.sub(rf"\b({SPLIT_FRAGS}) (t[a-z]*)", r"\1\2", t, flags=re.I)
    t = re.sub(r"\b(four|six|seven|eigh|nin|ten) (th)\b", r"\1\2", t, flags=re.I)
    return re.sub(r"\s+", " ", t).strip()


def page_info(pno):
    p = doc[pno]
    spans = []
    for b in p.get_text("dict")["blocks"]:
        if b["type"] != 0:
            continue
        for l in b["lines"]:
            for s in l["spans"]:
                if s["text"].strip():
                    spans.append({"t": s["text"], "bbox": pymupdf.Rect(s["bbox"]), "pno": pno})
    boxes = []
    W, H = p.rect.width, p.rect.height
    for _, r in p.get_bboxlog():
        r = pymupdf.Rect(r)
        if r.is_empty or (r.width > W * 0.9 and r.height > H * 0.5):
            continue
        boxes.append(r)
    return spans, boxes


pages = [page_info(i) for i in range(doc.page_count)]

# ---- group pages into questions (each question starts at the top of a page) -------
questions = []
for pno, (spans, _) in enumerate(pages):
    if spans and spans[0]["t"].startswith("Question ID:"):
        questions.append({"pages": [pno]})
    elif questions:
        questions[-1]["pages"].append(pno)

if limit:
    questions = questions[:limit]


def content_box(pno, y0, y1, x0=None):
    """Union of drawn content on page pno within [y0, y1] (extending right of x0)."""
    r = pymupdf.Rect()
    for b in pages[pno][1]:
        cy = (b.y0 + b.y1) / 2
        if y0 - 0.5 <= cy <= y1 + 0.5 and (x0 is None or b.x1 > x0 + 1):
            r |= b
    return r


def render(segments, out_path):
    """segments: list of (pno, y0, y1, x0). Stitch vertically into one PNG.
    x0 (if given) is a hard left clip, used to cut the 'A.' label off choices."""
    clips = []
    for pno, y0, y1, x0 in segments:
        cb = content_box(pno, y0, y1, x0)
        if cb.is_empty:
            continue
        left = (min(LEFT, cb.x0) - PAD) if x0 is None else x0
        clips.append((pno, pymupdf.Rect(left, cb.y0 - PAD, cb.x1 + PAD, cb.y1 + PAD)))
    if not clips:
        return None
    W = max(c.width for _, c in clips)
    H = sum(c.height for _, c in clips) + GAP * (len(clips) - 1)
    if not NO_IMAGES:
        tmp = pymupdf.open()
        page = tmp.new_page(width=W, height=H)
        y = 0
        for pno, c in clips:
            page.show_pdf_page(pymupdf.Rect(0, y, c.width, y + c.height), doc, pno, clip=c)
            y += c.height + GAP
        pix = page.get_pixmap(matrix=pymupdf.Matrix(SCALE, SCALE), colorspace=pymupdf.csGRAY, alpha=True)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        pix.save(out_path)
    return {"w": round(W * SCALE), "h": round(H * SCALE)}


def region(q, start, end, x0=None):
    """start/end: (pno, y). Returns per-page segments between them."""
    (sp, sy), (ep, ey) = start, end
    segs = []
    for pno in q["pages"]:
        if pno < sp or pno > ep:
            continue
        y0 = sy if pno == sp else 0
        y1 = ey if pno == ep else doc[pno].rect.height
        segs.append((pno, y0, y1, x0))
    return segs


META_KEYS = ["assessment", "test", "domain", "skill", "difficulty"]
records, problems = [], []

for q in questions:
    spans = [s for pno in q["pages"] for s in pages[pno][0]]
    qid = spans[0]["t"].split(":", 1)[1].strip()

    def pos(s, which="top"):
        return (s["pno"], s["bbox"].y0 if which == "top" else s["bbox"].y1)

    def find(pred, after=0):
        for i in range(after, len(spans)):
            if pred(spans[i]["t"].strip()):
                return i
        return None

    i_q = find(lambda t: t == "Question")
    i_rat = find(lambda t: t == "Rationale", i_q or 0)
    if None in (i_q, i_rat):
        problems.append((qid, "missing label"))
        continue
    i_ca = find(lambda t: t.startswith("Correct Answer:"), i_q)
    if i_ca is not None and i_ca > i_rat:
        i_ca = None
    i_ans = find(lambda t: t == "Answer", i_q)
    if i_ans is not None and i_ans > (i_ca if i_ca is not None else i_rat):
        i_ans = None
    i_end = i_ca if i_ca is not None else i_rat   # where the stem/choices stop

    # metadata table: header row cells by x, values below them
    hdr = {s["t"].strip(): s["bbox"] for s in spans[1:i_q] if s["t"].strip() in
           ("Assessment", "Test", "Domain", "Skill", "Difficulty")}
    cols = sorted(hdr.items(), key=lambda kv: kv[1].x0)
    meta = {k.lower(): [] for k, _ in cols}
    hdr_bottom = max(b.y1 for b in hdr.values())
    for s in spans[1:i_q]:
        if s["bbox"].y0 <= hdr_bottom:
            continue
        col = max((k for k, b in cols if s["bbox"].x0 >= b.x0 - 2), key=lambda k: hdr[k].x0, default=None)
        if col:
            meta[col.lower()].append(s["t"].strip())
    meta = {k: clean(" ".join(v)) for k, v in meta.items()}

    # answer: "Correct Answer:" label, else parse it out of the rationale (older layout)
    rationale_text = clean(" ".join(s["t"].strip() for s in spans[i_rat + 1:]))
    answer_source = "label"
    if i_ca is not None:
        ca = spans[i_ca]["t"].split(":", 1)[1].strip()
        answers = [a.strip() for a in ca.split(",") if a.strip()]
    else:
        m = re.match(r"\s*Choice ([A-D]) is correct", rationale_text)
        n = re.search(r"Note that (.+?) (?:are|is) (?:examples|an example|one of)", rationale_text)
        c = re.match(r"\s*The correct answer is (-?\d[\d,]*(?:\.\d+)?(?:/\d+)?)", rationale_text)
        if m:
            answers, answer_source = [m.group(1)], "rationale"
        elif n:
            answers = [a.strip() for a in re.split(r",\s*(?:and\s+)?|\s+and\s+", n.group(1)) if a.strip()]
            answer_source = "rationale"
        elif c:
            answers, answer_source = [c.group(1).replace(",", "")], "rationale"
        else:
            answers, answer_source = [], None

    out_q = out_dir / "q" / qid
    rec = {"id": qid, **{k: meta.get(k, "") for k in META_KEYS}}

    # stem
    stem_end = pos(spans[i_ans]) if i_ans is not None else pos(spans[i_end])
    stem = render(region(q, pos(spans[i_q], "bottom"), stem_end), out_q / "stem.png")
    rec["stem"] = stem and {"src": f"q/{qid}/stem.png", **stem}
    rec["stemText"] = clean(" ".join(s["t"].strip() for s in spans[i_q + 1:(i_ans if i_ans is not None else i_end)]))

    # choices
    choices = {}
    if i_ans is not None:
        idx = [i for i in range(i_ans + 1, i_end) if re.match(r"[A-D]\.(\s|$)", spans[i]["t"].strip() + " ")
               and spans[i]["bbox"].x0 < 40]
        for n_, i in enumerate(idx):
            letter = spans[i]["t"].strip()[0]
            end = pos(spans[idx[n_ + 1]]) if n_ + 1 < len(idx) else pos(spans[i_end])
            img = render(region(q, pos(spans[i]), end, x0=spans[i]["bbox"].x0 + 8.5), out_q / f"{letter.lower()}.png")
            if img:
                choices[letter] = {"src": f"q/{qid}/{letter.lower()}.png", **img}
        if len(choices) != 4:
            problems.append((qid, f"{len(choices)} choices"))
    rec["type"] = "mcq" if choices else "spr"
    rec["choices"] = choices or None
    rec["answer"] = answers[0] if (choices and answers) else None
    rec["acceptedAnswers"] = None if choices else (answers or None)
    rec["answerSource"] = answer_source
    if not answers:
        problems.append((qid, "no answer found (self-check)"))
    elif choices and rec["answer"] not in choices:
        problems.append((qid, f"answer {rec['answer']!r} not a choice"))

    # rationale: to the end of the last page of the question
    last = q["pages"][-1]
    rat = render(region(q, pos(spans[i_rat], "bottom"), (last, doc[last].rect.height)), out_q / "rationale.png")
    rec["rationale"] = rat and {"src": f"q/{qid}/rationale.png", **rat}
    rec["rationaleText"] = rationale_text
    rec["pages"] = [p + 1 for p in q["pages"]]
    records.append(rec)

out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "questions.json").write_text(json.dumps(records, indent=1, ensure_ascii=False), encoding="utf-8")

with open(out_dir / "questions.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["id", "domain", "skill", "difficulty", "type", "answer", "accepted_answers",
                "stem_img", "choice_a_img", "choice_b_img", "choice_c_img", "choice_d_img",
                "rationale_img", "stem_text", "rationale_text"])
    for r in records:
        ch = r["choices"] or {}
        w.writerow([r["id"], r["domain"], r["skill"], r["difficulty"], r["type"], r["answer"] or "",
                    "|".join(r["acceptedAnswers"] or []),
                    r["stem"] and r["stem"]["src"], *[(ch.get(L) or {}).get("src", "") for L in "ABCD"],
                    r["rationale"] and r["rationale"]["src"], r["stemText"], r["rationaleText"]])

print(f"{len(records)} questions written, {len(problems)} problems")
for p in problems:
    print("  ", *p)
