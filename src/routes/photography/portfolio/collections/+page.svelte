<script lang="ts">
    import Back from "$lib/components/Back.svelte";
    import Header from "$lib/components/PhotoHeader.svelte";
    // @ts-ignore
    import Tile from "$lib/components/Tile.svelte";
    import {onMount} from "svelte";

    let active: string | null = null;

    export let opacity = 0.5;

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

<div class = "bg-bg p-7 pl-15">
    <div style={`transform: translate(${x * 10}px, ${y * 10}px);`}>
        <Header/>
    </div>
    <div class = "mt-5 mb-10" style={`transform: translate(${x * 10}px, ${y * 10}px);`}>
        <Back/>
    </div>
    <div class = "grid grid-cols-2 grid-auto-rows-auto gap-y-15 w-full 2xl:gap-10 place-items-center" style={`transform: translate(${x * 15}px, ${y * 15}px);`}>
        <!-- Blue Angels -->
            <Tile
            id = "blue"
            active = {active}
            setActive = {(id) => active = id}
            img = "/images/portfolio thumbs/Blue Angels thumb.jpg"
            alt = "Blue Angels Thumbnail"
            title = "BLUE ANGELS"
            desc = "October 14, 2024"
            href = "collections/blueangels"
            x = {{default: 185, '2xl': 440}}
            y= {{default: -10, '2xl': -30}}
            />
        <!-- China -->
            <Tile
            id = "china"
            active = {active}
            setActive = {(id) => active = id}
            img = "/images/portfolio thumbs/China thumb.jpg"
            alt = "China Thumbnail"
            title = "CHINA"
            desc = "July 1-12, 2025"
            href = "collections/chinajul25"
            x = {{default: -352, '2xl': -548}}
            y = {{default: 47, '2xl': 140}}
            />
    </div>
</div>