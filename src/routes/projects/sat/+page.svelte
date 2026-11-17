<script lang="ts">
	import { onMount, untrack } from 'svelte';
	import TypeWriter from '$lib/components/TypeWriter.svelte';
	import Desmos from '$lib/components/Desmos.svelte';
	import {
		LETTERS, imgUrl, checkSpr, loadProgress, saveProgress, shuffle,
		type Letter, type Progress, type Question
	} from '$lib/sat';

	let { data } = $props();
	const questions: Question[] = data.questions;
	const byId = new Map(questions.map((q) => [q.id, q]));
	const domains = [...new Set(questions.map((q) => q.domain))].sort();

	// ---- filters -----------------------------------------------------------------
	let domain = $state('all');
	let skill = $state('all');
	let qtype = $state<'all' | 'mcq' | 'spr'>('all');
	let status = $state<'all' | 'new' | 'missed' | 'flagged'>('all');
	let shuffled = $state(true);

	const skills = $derived(
		[...new Set(questions.filter((q) => domain === 'all' || q.domain === domain).map((q) => q.skill))].sort()
	);

	// ---- progress (localStorage) ---------------------------------------------------
	let progress = $state<Progress>({});
	let showCalc = $state(true);
	onMount(() => {
		progress = loadProgress();
		try {
			showCalc = localStorage.getItem('sat-calc') !== 'off';
		} catch {}
		rebuild();
	});
	function toggleCalc() {
		showCalc = !showCalc;
		try {
			localStorage.setItem('sat-calc', showCalc ? 'on' : 'off');
		} catch {}
	}

	// ---- floating panels: eased mouse parallax, same feel as the rest of the site -----
	// Each panel gets its own depth (px of travel at the screen edge). Motion freezes while
	// the pointer is over the calculator so dragging on the graph doesn't wobble.
	let mx = $state(0);
	let my = $state(0);
	onMount(() => {
		if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
		let tx = 0, ty = 0, frame = 0;
		const onMove = (e: MouseEvent) => {
			if ((e.target as HTMLElement)?.closest?.('[data-calc]')) return;
			tx = (e.clientX / innerWidth - 0.5) * 2;
			ty = (e.clientY / innerHeight - 0.5) * 2;
		};
		const tick = () => {
			mx += (tx - mx) * 0.05;
			my += (ty - my) * 0.05;
			frame = requestAnimationFrame(tick);
		};
		addEventListener('mousemove', onMove);
		tick();
		return () => {
			removeEventListener('mousemove', onMove);
			cancelAnimationFrame(frame);
		};
	});
	const float = (depth: number) => `transform: translate3d(${(mx * depth).toFixed(2)}px, ${(my * depth).toFixed(2)}px, 0)`;
	const windowShadow = 'shadow-[0_24px_60px_-28px_rgba(0,0,0,0.28)]';
	function record(id: string, right: boolean) {
		const p = progress[id] ?? { tries: 0, right: 0, last: false };
		progress[id] = { ...p, tries: p.tries + 1, right: p.right + (right ? 1 : 0), last: right };
		saveProgress(progress);
	}
	function toggleFlag(id: string) {
		const p = progress[id] ?? { tries: 0, right: 0, last: false };
		progress[id] = { ...p, flagged: !p.flagged };
		saveProgress(progress);
	}
	function resetProgress() {
		if (!confirm('Clear all saved answers and flags?')) return;
		progress = {};
		saveProgress(progress);
		rebuild();
	}

	// ---- question order: snapshot when filters change (not as you answer) -----------
	let order = $state<string[]>([]);
	let index = $state(0);

	function rebuild() {
		const list = questions.filter((q) => {
			const p = progress[q.id];
			return (
				(domain === 'all' || q.domain === domain) &&
				(skill === 'all' || q.skill === skill) &&
				(qtype === 'all' || q.type === qtype) &&
				(status === 'all' ||
					(status === 'new' && !p?.tries) ||
					(status === 'missed' && p?.tries && !p.last) ||
					(status === 'flagged' && p?.flagged))
			);
		});
		const ids = list.map((q) => q.id);
		order = shuffled ? shuffle(ids) : ids;
		index = 0;
		resetAttempt();
	}

	$effect(() => {
		// re-run only when filters change
		[domain, skill, qtype, status, shuffled];
		untrack(rebuild);
	});
	$effect(() => {
		if (skill !== 'all' && !skills.includes(skill)) skill = 'all';
	});

	const current = $derived(order.length ? byId.get(order[index]) : undefined);

	// ---- attempt state -----------------------------------------------------------------
	let picked = $state<Letter | null>(null);
	let typed = $state('');
	let checked = $state(false);
	let wasRight = $state(false);
	let showRationale = $state(false);
	let sprInput = $state<HTMLInputElement>();

	function resetAttempt() {
		picked = null;
		typed = '';
		checked = false;
		wasRight = false;
		showRationale = false;
	}

	function check() {
		if (!current || checked) return;
		if (current.type === 'mcq') {
			if (!picked) return;
			wasRight = picked === current.answer;
		} else {
			if (!typed.trim()) return;
			wasRight = checkSpr(typed, current.acceptedAnswers ?? []);
		}
		checked = true;
		showRationale = true;
		record(current.id, wasRight);
	}

	function go(delta: number) {
		if (!order.length) return;
		index = (index + delta + order.length) % order.length;
		resetAttempt();
		window.scrollTo({ top: 0, behavior: 'smooth' });
	}

	// preload the next question's images
	$effect(() => {
		const next = order.length ? byId.get(order[(index + 1) % order.length]) : undefined;
		if (!next) return;
		for (const img of [next.stem, ...Object.values(next.choices ?? {})]) new Image().src = imgUrl(img);
	});

	$effect(() => {
		if (current?.type === 'spr') sprInput?.focus();
	});

	function onKey(e: KeyboardEvent) {
		const target = e.target as HTMLElement;
		if (target?.closest?.('[data-calc]')) return; // typing in Desmos
		const inInput = target?.tagName === 'INPUT' || target?.tagName === 'SELECT';
		if (e.key === 'Enter') {
			e.preventDefault();
			checked ? go(1) : check();
			return;
		}
		if (inInput) return;
		if (e.key === 'ArrowRight') go(1);
		else if (e.key === 'ArrowLeft') go(-1);
		else if (current?.type === 'mcq' && !checked) {
			const k = e.key.toUpperCase();
			const L = (['1', '2', '3', '4'].includes(k) ? LETTERS[Number(k) - 1] : k) as Letter;
			if (LETTERS.includes(L)) picked = L;
		}
	}

	// ---- stats -------------------------------------------------------------------------
	const stats = $derived(
		domains.map((d) => {
			const qs = questions.filter((q) => q.domain === d);
			const done = qs.filter((q) => progress[q.id]?.tries);
			const right = done.filter((q) => progress[q.id].last).length;
			return { d, total: qs.length, done: done.length, pct: done.length ? Math.round((right / done.length) * 100) : null };
		})
	);
	const totalDone = $derived(stats.reduce((s, x) => s + x.done, 0));

	// images are rendered at 2px per PDF point; show them at 1.35 CSS px per point (~12px text)
	const half = (n: number) => Math.round(n * 0.675);
</script>

<svelte:head>
	<title>SAT Math Practice — John Lao</title>
</svelte:head>

<svelte:window onkeydown={onKey} />

<div class="relative z-10 min-h-screen p-6 md:p-10 font-body text-header">
	<nav class="flex flex-row flex-wrap items-end gap-4 pb-6">
		<a href="/projects" class="text-6xl md:text-8xl font-header uppercase leading-none" style={float(15)}>
			<TypeWriter text="SAT" />
		</a>
		<p class="font-subheader uppercase text-sm md:text-md pb-2" style={float(10)}>
			Math question bank · {questions.length} questions
		</p>
		<a href="/projects" class="ml-auto border-2 border-header bg-bg/80 font-subheader uppercase text-sm px-4 py-2 hover:bg-header hover:text-bg transition-colors" style={float(6)}>
			Back
		</a>
	</nav>

	<!-- stats -->
	<section class="grid grid-cols-2 lg:grid-cols-5 gap-px mb-6 text-sm {windowShadow}" style={float(5)}>
		<div class="bg-bg/80 p-3 ring-1 ring-shadow">
			<div class="font-subheader uppercase text-xs opacity-60">Answered</div>
			<div class="text-xl font-header">{totalDone}<span class="opacity-40">/{questions.length}</span></div>
		</div>
		{#each stats as s}
			<button
				class="bg-bg/80 p-3 ring-1 ring-shadow text-left hover:bg-imagebg transition-colors {domain === s.d ? 'outline-2 outline-header -outline-offset-2' : ''}"
				onclick={() => (domain = domain === s.d ? 'all' : s.d)}
			>
				<div class="font-subheader uppercase text-xs opacity-60 truncate">{s.d}</div>
				<div class="text-xl font-header">
					{s.done}<span class="opacity-40">/{s.total}</span>
					{#if s.pct !== null}<span class="text-sm font-body opacity-70 ml-1">{s.pct}%</span>{/if}
				</div>
				<div class="h-1 bg-something mt-2"><div class="h-1 bg-header" style="width: {(s.done / s.total) * 100}%"></div></div>
			</button>
		{/each}
	</section>

	<!-- filters -->
	<section class="flex flex-wrap gap-3 items-center mb-6 text-sm" style={float(3)}>
		<select bind:value={domain} class="border border-shadow bg-bg/80 px-3 py-2">
			<option value="all">All domains</option>
			{#each domains as d}<option value={d}>{d}</option>{/each}
		</select>
		<select bind:value={skill} class="border border-shadow bg-bg/80 px-3 py-2 max-w-72">
			<option value="all">All skills</option>
			{#each skills as s}<option value={s}>{s}</option>{/each}
		</select>
		<select bind:value={qtype} class="border border-shadow bg-bg/80 px-3 py-2">
			<option value="all">All types</option>
			<option value="mcq">Multiple choice</option>
			<option value="spr">Student-produced response</option>
		</select>
		<select bind:value={status} class="border border-shadow bg-bg/80 px-3 py-2">
			<option value="all">Any status</option>
			<option value="new">Not attempted</option>
			<option value="missed">Missed last time</option>
			<option value="flagged">Flagged</option>
		</select>
		<label class="flex items-center gap-2 select-none">
			<input type="checkbox" bind:checked={shuffled} /> Shuffle
		</label>
		<button
			class="ml-auto px-3 py-2 border {showCalc ? 'bg-header text-bg border-header' : 'border-shadow bg-bg/80'}"
			onclick={toggleCalc}
			aria-pressed={showCalc}
		>
			Desmos calculator
		</button>
		<button class="underline opacity-60 hover:opacity-100" onclick={resetProgress}>Reset progress</button>
	</section>

	{#if !current}
		<div class="border border-shadow bg-bg/80 p-10 text-center">
			<p class="font-subheader uppercase">No questions match these filters.</p>
		</div>
	{:else}
		{@const p = progress[current.id]}
		<div class="flex flex-col lg:flex-row gap-6 items-start">
		<div class="flex-1 min-w-0 max-w-4xl w-full" style={float(8)}>
		<article class="border border-shadow bg-bg/80 {windowShadow}">
			<header class="flex flex-wrap items-center gap-x-4 gap-y-1 px-5 py-3 border-b border-shadow text-xs font-subheader uppercase">
				<span class="font-header text-sm">{index + 1} / {order.length}</span>
				<span>{current.domain}</span>
				<span class="opacity-60 normal-case font-body">{current.skill}</span>
				<span class="opacity-60">{current.type === 'mcq' ? 'Multiple choice' : 'Type your answer'}</span>
				{#if p?.tries && !checked}
					<span class={p.last ? 'text-green-700' : 'text-red-700'}>
						{p.last ? 'Got it last time' : 'Missed last time'}
					</span>
				{/if}
				<button
					class="ml-auto px-2 py-1 border {p?.flagged ? 'bg-header text-bg border-header' : 'border-shadow'}"
					onclick={() => toggleFlag(current.id)}
					aria-pressed={!!p?.flagged}
				>
					{p?.flagged ? '★ Flagged' : '☆ Flag'}
				</button>
			</header>

			<div class="p-5 md:p-8 space-y-6">
				<img
					src={imgUrl(current.stem)}
					alt={current.stemText || 'Question'}
					width={half(current.stem.w)}
					height={half(current.stem.h)}
					class="max-w-full h-auto"
				/>

				{#if current.type === 'mcq' && current.choices}
					<div class="grid gap-3">
						{#each LETTERS as L, i}
							{@const c = current.choices[L]}
							{@const isAnswer = checked && L === current.answer}
							{@const isWrongPick = checked && L === picked && L !== current.answer}
							<button
								class="flex items-center gap-4 text-left border-2 px-4 py-3 transition-colors
									{isAnswer ? 'border-green-600 bg-green-50' : isWrongPick ? 'border-red-600 bg-red-50' : picked === L ? 'border-header bg-imagebg' : 'border-something hover:border-shadow'}"
								onclick={() => !checked && (picked = L)}
								disabled={checked}
							>
								<span class="shrink-0 w-8 h-8 grid place-items-center border font-header text-sm
									{picked === L || isAnswer ? 'bg-header text-bg border-header' : 'border-shadow'}">{L}</span>
								<img src={imgUrl(c)} alt="Choice {L}" width={half(c.w)} height={half(c.h)} class="max-w-full h-auto" />
								<kbd class="ml-auto text-xs opacity-30 hidden md:block">{i + 1}</kbd>
							</button>
						{/each}
					</div>
				{:else}
					<div class="flex flex-wrap items-center gap-3">
						<input
							bind:this={sprInput}
							bind:value={typed}
							disabled={checked}
							inputmode="decimal"
							autocomplete="off"
							placeholder="Your answer"
							class="border-2 px-4 py-3 text-lg w-48 font-body
								{checked ? (wasRight ? 'border-green-600 bg-green-50' : 'border-red-600 bg-red-50') : 'border-shadow focus:border-header outline-none'}"
						/>
						<span class="text-xs opacity-60">Integer, decimal (.75) or fraction (3/4)</span>
					</div>
				{/if}

				<div class="flex flex-wrap items-center gap-3 pt-2">
					<button class="border-2 border-something px-4 py-2 font-subheader uppercase text-sm hover:border-shadow" onclick={() => go(-1)}>
						← Prev
					</button>
					{#if !checked}
						<button
							class="bg-header text-bg px-6 py-2 font-subheader uppercase text-sm disabled:opacity-30"
							onclick={check}
							disabled={current.type === 'mcq' ? !picked : !typed.trim()}
						>
							Check
						</button>
						<button class="underline text-sm opacity-60 hover:opacity-100" onclick={() => (showRationale = !showRationale)}>
							{showRationale ? 'Hide' : 'Show'} explanation
						</button>
					{:else}
						<span class="font-header uppercase {wasRight ? 'text-green-700' : 'text-red-700'}">
							{wasRight ? 'Correct' : 'Incorrect'}
						</span>
						{#if !wasRight}
							<span class="text-sm">
								Answer: <b>{current.type === 'mcq' ? current.answer : (current.acceptedAnswers ?? []).join(' or ')}</b>
							</span>
						{/if}
					{/if}
					<button class="ml-auto bg-header text-bg px-6 py-2 font-subheader uppercase text-sm" onclick={() => go(1)}>
						Next →
					</button>
				</div>

				{#if showRationale}
					<div class="border-t border-shadow pt-6">
						<h2 class="font-subheader uppercase text-xs opacity-60 mb-3">Explanation</h2>
						<img
							src={imgUrl(current.rationale)}
							alt={current.rationaleText}
							width={half(current.rationale.w)}
							height={half(current.rationale.h)}
							class="max-w-full h-auto"
						/>
					</div>
				{/if}
			</div>
		</article>
		<p class="text-xs opacity-40 mt-3">
			Keys: 1–4 / A–D pick · Enter check, then next · ← → move · Question ID {current.id} · Questions © College Board
		</p>
		</div>
		{#if showCalc}
			<aside class="w-full lg:w-[440px] xl:w-[540px] shrink-0 h-[520px] lg:h-[calc(100vh-3rem)] lg:sticky lg:top-6 border border-shadow bg-bg/80 {windowShadow}" style={float(12)}>
				<Desmos stateKey={current.id} />
			</aside>
		{/if}
		</div>
	{/if}
</div>
