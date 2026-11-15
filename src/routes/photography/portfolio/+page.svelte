<script lang="ts">
    import Back from "$lib/components/Back.svelte";
    import Header from "$lib/components/PhotoHeader.svelte";
    import SCTile from "$lib/components/SCTile.svelte";
    import { onMount } from "svelte";

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

<div class = "bg-bg p-7 pl-15 ">
    <div style={`transform: translate(${x * 10}px, ${y * 10}px);`}>
        <Header/>
    </div>
    <div class = "grid grid-cols-2 gap-y-15 w-full p-10" style={`transform: translate(${x * 15}px, ${y * 15}px);`}>
        <!-- Series -->
        <SCTile path = "portfolio/series" img = "/images/portfolio thumbs/series.jpg" title = "SERIES" desc = "ongoing projects"/>
        <!-- Collections -->
        <SCTile path = "portfolio/collections" img = "/images/portfolio thumbs/collections.jpg" title = "COLLECTIONS" desc = "moments in time"/>
    </div>
</div>