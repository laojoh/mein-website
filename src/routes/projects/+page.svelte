<script lang="ts">
    import Star from "$lib/components/Star.svelte";
    import TypeWriter from "$lib/components/TypeWriter.svelte";
    import AmbientShapes from "$lib/components/AmbientShapes.svelte";
    import { onMount, onDestroy } from "svelte";

    let x = 0;
    let y = 0;

    let targetX = 0;
    let targetY = 0;

    onMount(() => {
        const handleMouseMove = (e: { clientX: number; clientY: number; }) => {
            targetX = (e.clientX / window.innerWidth - 0.5) * 2;
            targetY = (e.clientY / window.innerHeight - 0.5) * 2;
        };

        window.addEventListener('mousemove', handleMouseMove);

        // @ts-ignore
        let animationFrame;

        const animate = () => {
            x += (targetX - x) * 0.05;
            y += (targetY - y) * 0.05;

            animationFrame = requestAnimationFrame(animate);
        };

        animate();

        return () => {
            window.removeEventListener('mousemove', handleMouseMove);
            // @ts-ignore
            cancelAnimationFrame(animationFrame);
        };
    });
</script>

<div class = "bg-bg p-10">
    <AmbientShapes opacity={0.7} />
</div>