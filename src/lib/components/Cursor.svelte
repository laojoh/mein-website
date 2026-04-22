<script>
	import { spring } from 'svelte/motion';

	// outer
    let coords1 = spring(
		{ x: 0, y: 0 },
		{
			stiffness: 0.05,
			damping: 0.5
		}
	);

    // innter
	let coords2 = spring(
		{ x: 0, y: 0 },
		{
			stiffness: 0.15,
			damping: 0.5
		}
	);

	let size = spring(10);

</script>

<svelte:window
	on:mousemove={(e) => {
		coords1.set({ x: e.clientX, y: e.clientY })
		coords2.set({ x: e.clientX, y: e.clientY })
	}}
	on:mousedown={(e) => {
		size.set(14);
	}}
	on:mouseup={(e) => {
		size.set(10);
	}}
/>

<svg
	class ="w-full h-full"
>
	<rect 
    x={$coords1.x - $size}
    y={$coords1.y - $size}
    width={$size * 2}
    height={$size * 2}
    stroke="#52412A"
    stroke-width="1"
    fill="none"
    />

	<rect
    x={$coords2.x - $size/4}
    y={$coords2.y - $size/4}
    width={$size/2}
    height={$size/2}
    fill="#52412A"
    />
</svg>

<style>
	:global(body) {
		cursor: none;
	}
	
	.w-full {
		width: 100vw;
	}
	
	.h-full {
		height: 100vh;
	}
	
	svg {
		position: fixed;
        z-index: 9999;
		top: 0;
		left: 0;
		pointer-events: none;

        will-change: transform;
	}
</style>