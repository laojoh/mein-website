<script lang="ts">
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

<div id="lightbox" class="hidden fixed inset-0 bg-black/70 backdrop-blur-sm flex items-center justify-center z-50">
    <img id="lightbox-img" class="max-w-[90vw] max-h-[90vh] shadow-xl" src="" alt="" />
</div>