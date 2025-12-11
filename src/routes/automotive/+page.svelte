<script lang="ts">
    import Header from "$lib/components/Header.svelte";
    import B2Port from "$lib/components/B2Port.svelte";
    import { onMount } from "svelte";

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

<div class = "bg-bg p-7 pl-15">
    <Header/>
    <nav class="grid grid-cols-6 grid-auto-rows gap-10 p-5">
        <B2Port/>
        <div class="col-start-5 col-span-2 row-start-2 text-header font-subheader">
            <h2 class="text-3xl">Project Background</h2>
            <p class="text-xl">
                Lorem ipsum dolor sit amet consectetur adipiscing elit. Sit amet consectetur adipiscing elit quisque faucibus ex. Adipiscing elit quisque faucibus ex sapien vitae pellentesque.
            </p>
        </div>

        <p class="text-xl col-start-4 col-span-3 row-start-7 row-span-2">
            Lorem ipsum dolor sit amet consectetur adipiscing elit. Sit amet consectetur adipiscing elit quisque faucibus ex. Adipiscing elit quisque faucibus ex sapien vitae pellentesque.
        </p>

        <img class="zoomable col-start-2 col-span-3 row-start-1 row-span-3 rounded-xl" src="/images/automotive/automotive1.jpg" alt="" />
        <img class="zoomable col-start-2 col-span-2 row-start-6 row-span-2 rounded-xl" src="/images/automotive/automotive2.jpg" alt="" />
        <img class="zoomable col-start-1 col-span-3 row-start-4 row-span-2 rounded-xl" src="/images/automotive/automotive3.jpg" alt="" />
        <img class="zoomable col-start-4 col-span-3 row-start-5 row-span-2 rounded-xl" src="/images/automotive/automotive4.jpg" alt="" />
        <img class="zoomable col-start-1 col-span-2 row-start-8 row-span-2 rounded-xl" src="/images/automotive/automotive5.jpg" alt="" />
    </nav>
    <!-- Lightbox Overlay -->
    <div id="lightbox"
        class="hidden fixed inset-0 bg-black/70 backdrop-blur-sm flex items-center justify-center z-50">
        <img id="lightbox-img" class="max-w-[90vw] max-h-[90vh] rounded-xl shadow-xl" src="" alt="" />
    </div>
</div>