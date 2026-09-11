<script lang="ts">
    import { onMount } from 'svelte';

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

<div class = "pointer-events-none fixed inset-0 overflow-hidden text-header" style={`opacity: ${opacity}; transform: translate(${x * 5}px, ${y * 5}px);`}>
    <!-- DESKTOP -->
    <svg class = "ambient-shapes hidden lg:block w-full h-full" viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice">
        <!-- tracks -->
        <path d="M60,1600 L60,420 L500, 420 L500, -1" fill="none" stroke="currentColor" stroke-width="1" opacity="0.5"/>
        <path d="M1500, -1 L1500,345 L900,345 L900,535 L1275,535 L1275, 900" fill="none" stroke="currentColor" stroke-width="1" opacity="0.5"/>
        <path d="M782,2 L782,360 L-1,360" fill="none" stroke="currentColor" stroke-width="1" opacity="0.5"/>
        
        <!-- traveling segments -->
        <path class = "crawl-a" d="M60,650 L60,420 L500,420 L500, -1" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="40 590"/>
        <path class = "crawl-b" d="M1500, -1 L1500,345 L900,345 L900,535 L1275,535 L1275, 900" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="36 744"/>
        <path class="crawl-e" d="M782,2 L782,360 L-1,360" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="40 1055"/>

        <!-- corner nodes -->
        <circle cx="60" cy="420" r="3" fill="currentColor" opacity="0.25"/>
        <circle cx="500" cy="420" r="3" fill="currentColor" opacity="0.25"/>
        <circle cx="1500" cy="345" r="3" fill="currentColor" opacity="0.25"/>
        <circle cx="900" cy="345" r="3" fill="currentColor" opacity="0.25"/>
        <circle cx="900" cy="535" r="3" fill="currentColor" opacity="0.25"/>
        <circle cx="782" cy="360" r="3" fill="currentColor" opacity="0.25"/>
        <circle cx="1275" cy="535" r="3" fill="currentColor" opacity="0.25"/>
    </svg>

    <!-- MOBILE -->
    <svg class = "ambient-shapes lg:hidden w-full h-full" viewBox="0 0 800 1600" preserveAspectRatio="xMidYMid slice">
        <!-- tracks -->
        <path d="M1600, 800 L1600, 250 L115, 250 L115, -1" fill="none" stroke="currentColor" stroke-width="1" opacity="0.5"/>
        
        <!-- traveling segments -->
        <path class = "crawl-aa" d="M1600, 800 L1600, 250 L115, 250 L115, -1" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="40 590"/>

        <!-- corner nodes -->
        <circle cx="1600" cy="250" r="3" fill="currentColor" opacity="0.25"/>
    </svg>
</div>

<style>
    .crawl-a {
        animation: crawl-a 22s linear infinite;
    }

    .crawl-aa {
        animation: crawl-aa 15s linear infinite;
    }

    .crawl-b {
        animation: crawl-b 24s linear infinite;
    }
    
    .crawl-e { 
        animation: crawl-e 31s linear infinite; 
    }
    

    @keyframes crawl-a {
        to { stroke-dashoffset: -630; }
    }

    @keyframes crawl-aa {
        to { stroke-dashoffset: -630; }
    }

    @keyframes crawl-b {
        to { stroke-dashoffset: -780; }
    }

    @keyframes crawl-c {
        to { stroke-dashoffset: -250; }
    }

    @keyframes crawl-d {
        to { stroke-dashoffset: -300; }
    }

    @keyframes crawl-e {
        to { stroke-dashoffset: -1095; } 
    }

    @media (prefers-reduced-motion: reduce) {
        .ambient-shapes path[class] {
            animation: none !important;
        }
    }
</style>
