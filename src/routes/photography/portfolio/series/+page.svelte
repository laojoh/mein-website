<script lang="ts">
    import Back from "$lib/components/Back.svelte";
    import Header from "$lib/components/PhotoHeader.svelte";
    // @ts-ignore
    import Tile from "$lib/components/Tile.svelte";
    import { onMount } from "svelte";

    let active: string | null = null;

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
    <div class = "grid grid-cols-3 grid-auto-rows-auto gap-y-15 w-full place-items-center" style={`transform: translate(${x * 15}px, ${y * 15}px);`}>
        <!-- Street -->
            <Tile
            id = "street"
            active = {active}
            setActive = {(id) => active = id}
            img = "/images/portfolio thumbs/Street thumb.jpg"
            alt = "Street Photography Thumbnail"
            title = "STREET"
            desc = ""
            href = "series/street"
            />
        <!-- Portraiture -->
            <Tile
            id = "portraiture"
            active = {active}
            setActive = {(id) => active = id}
            img = "/images/portfolio thumbs/Portrait thumb.jpg"
            alt = "Portrait Thumbnail"
            title = "PORTRAITURE"
            desc =""
            href = "series/portraiture"
            x = {{default: 0, '2xl': 0}}
            y = {{default: 46, '2xl': 140}}
            />
        <!-- Automotive -->
            <Tile
            id = "auto"
            active = {active}
            setActive = {(id) => active = id}
            img = "/images/portfolio thumbs/Automotive thumb.jpg"
            alt = "Automotive Thumbnail"
            title = "AUTOMOTIVE"
            desc = ""
            href = "series/automotive"
            x = {{default: -592, '2xl': -895}} 
            y = {{default: -46, '2xl': -37}}
            />
    </div>
</div>