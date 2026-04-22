<script lang="ts">
    import Header from "$lib/components/Header.svelte";
    import B2Port from "$lib/components/B2Port.svelte";
    import { onMount } from "svelte";
    import Lightbox from "$lib/components/Lightbox.svelte";
    import TypeWrite from "$lib/components/TypeWriter.svelte";
    import { TypeWriter } from "svelte-typewrite";
    import Preload from "$lib/components/Preload.svelte";

	let zoom = 1;
	let originX = "50%";
	let originY = "50%";

	onMount(() => {
		const lightbox = document.getElementById("lightbox");
		const lightboxImg = document.getElementById("lightbox-img") as HTMLImageElement | null;

		if (!lightbox || !lightboxImg) return;

		// Open lightbox
		document.querySelectorAll(".zoomable").forEach(imgEl => {
			const img = imgEl as HTMLImageElement;
			img.addEventListener("click", () => {
				zoom = 1;
				lightboxImg.style.transform = "scale(1)";
				lightboxImg.style.transformOrigin = "50% 50%";

				lightboxImg.src = img.src;
				lightbox.classList.remove("hidden");
			});
		});

		// Close when clicking outside the image
		lightbox.addEventListener("click", (e) => {
			if (e.target === lightbox) {
				lightbox.classList.add("hidden");
				lightboxImg.src = "";
			}
		});

		// Zoom on scroll
        lightboxImg.addEventListener("wheel", (e: WheelEvent) => {
            e.preventDefault();

            const delta = -e.deltaY * 0.0015;

            // Store previous zoom
            const prevZoom = zoom;

            // Apply new zoom with limits
            zoom = Math.min(Math.max(zoom + delta, 0.5), 5);

            // If we hit min/max zoom, DO NOT move origin
            if (zoom === prevZoom) return;

            const rect = lightboxImg.getBoundingClientRect();
            const offsetX = e.clientX - rect.left;
            const offsetY = e.clientY - rect.top;

            originX = `${(offsetX / rect.width) * 100}%`;
            originY = `${(offsetY / rect.height) * 100}%`;

            lightboxImg.style.transformOrigin = `${originX} ${originY}`;
            lightboxImg.style.transform = `scale(${zoom})`;
        });
	});
</script>

<Preload path = "/images/automotive/automotive1.jpg"/>

<div class = "bg-bg p-7 pl-15">
    <Header/>
    <nav class="grid grid-cols-6 grid-auto-rows gap-10 p-5">
        <B2Port/>
        <div class="col-start-5 col-span-2 row-start-4 text-header font-subheader">
            <h2 class="text-3xl">
                <TypeWrite text="Project Background"/>
            </h2>
            <p class="text-md">
                <TypeWriter texts={["Lorem ipsum dolor sit amet consectetur adipiscing elit. Sit amet consectetur adipiscing elit quisque faucibus ex. Adipiscing elit quisque faucibus ex sapien vitae pellentesque."]} repeat={1} typeSpeed={15} endState={{text: "typed", caret: "hidden"}} blinkDuration={1000}/>
            </p>
        </div>

        <p class="text-xl col-start-4 col-span-3 row-start-7 row-span-2">
            Lorem ipsum dolor sit amet consectetur adipiscing elit. Sit amet consectetur adipiscing elit quisque faucibus ex. Adipiscing elit quisque faucibus ex sapien vitae pellentesque.
        </p>

        <img class="zoomable col-start-2 col-span-3 row-start-1 row-span-4 " src="/images/automotive/automotive1.jpg" alt="" />
        <img class="zoomable col-start-2 col-span-2 row-start-7 row-span-2 " src="/images/automotive/automotive2.jpg" alt="" />
        <img class="zoomable col-start-1 col-span-3 row-start-5 row-span-2 " src="/images/automotive/automotive3.jpg" alt="" />
        <img class="zoomable col-start-4 col-span-3 row-start-6 row-span-2 " src="/images/automotive/automotive4.jpg" alt="" />
        <img class="zoomable col-start-1 col-span-2 row-start-9 row-span-2 " src="/images/automotive/automotive5.jpg" alt="" />
    </nav>
    <Lightbox/>
</div>