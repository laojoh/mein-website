<script>
    import { onMount } from 'svelte';
    import Star from '$lib/components/Star.svelte';
    import TypeWriter from '$lib/components/TypeWriter.svelte';
    import AmbientShapes from '$lib/components/AmbientShapes.svelte';

    let x = 0;
    let y = 0;

    let targetX = 0;
    let targetY = 0;

    onMount(() => {
        // @ts-ignore
        const handleMouseMove = (e) => {
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
    <div class="relative min-h-screen lg:fixed lg:inset-0 select-none lg:overflow-hidden">
        <AmbientShapes opacity={0.7} />
        <!-- decorative parallax elements are tuned for desktop proportions, so they only show at lg+ -->
        <div class = "hidden lg:block pointer-events-none">
            <!-- planet -->
            <!-- <img class = " w-15xl absolute -bottom-160 -left-100 rotate-90" src = "/images/home/planet.png" alt = "planet" style={`transform: translate(${y * 25}px, ${x * -25}px);`}/> -->
            <!-- stars (max stretch 1) -->
            <div class = "absolute top-20 left-130" style={`transform: translate(${x * 10}px, ${y * 10}px);`}>
                <Star
                size={100}
                stretchX={1}
                stretchY={1}
                rotation={0}
                waist = {0.2}
                />
            </div>
            <div class = "absolute bottom-15 left-15" style={`transform: translate(${x * 25}px, ${y * 25}px);`}>
                <Star
                size={350}
                stretchX={1}
                stretchY={1}
                rotation={0}
                waist = {0.3}
                />
            </div>

            <div class = "absolute top-45 left-155" style={`transform: translate(${x * 9}px, ${y * 9}px);`}>
                <Star
                size={70}
                stretchX={1}
                stretchY={1}
                rotation={0}
                waist = {0.2}
                />
            </div>

        </div>
        <div class = "p-4 lg:p-7 lg:pl-15">
            <nav class = "w-full flex flex-col justify-start items-start gap-3 lg:gap-4 p-2 lg:p-5 " style={`transform: translate(${x * 15}px, ${y * 15}px);`}>
            <div class = "text-4xl sm:text-6xl lg:text-8xl 2xl:text-9xl text-header font-header uppercase">
                <TypeWriter text = "John Lao"/>
            </div>
            <p class = "text-sm lg:text-md font-body pl-1 lg:pl-3">&mdash; Robotics, Photography, Web Development &mdash;</p>
            </nav>
            <nav class = "static lg:absolute lg:top-45 lg:right-35 flex flex-col gap-5 lg:gap-8 text-header font-header text-3xl sm:text-4xl lg:text-6xl uppercase mt-6 lg:mt-0 px-2 lg:px-0" style={`transform: translate(${x * 15}px, ${y * 15}px);`}>
                <div class = "flex flex-col sm:flex-row w-full lg:w-100 gap-1 sm:gap-4 sm:items-center transition-transform duration-300 hover:scale-110">
                    <a href = "/projects"><TypeWriter text = "Projects"/></a>
                    <a class = "text-xs font-subheader" href = "/projects">My personal projects</a>
                </div>
                <div class = "flex flex-col sm:flex-row w-full lg:w-100 gap-1 sm:gap-4 sm:items-center transition-transform duration-300 hover:scale-110">
                    <a href = "/photography"><TypeWriter text = "Photography"/></a>
                    <a class = "text-xs font-subheader" href = "/photography">My photography gallery</a>
                </div>
                <div class = "flex flex-col sm:flex-row w-full lg:w-120 gap-1 sm:gap-6 sm:items-center transition-transform duration-300 hover:scale-110">
                    <a href = "/about"><TypeWriter text = "A Glimpse"/></a>
                    <p class = "text-xs font-subheader lg:w-30">A little about me and my life</p>
                </div>
                <div class = "flex flex-col sm:flex-row w-full lg:w-80 gap-1 sm:gap-4 sm:items-center transition-transform duration-300 hover:scale-110">
                    <a href = "/contact"><TypeWriter text = "Contact"/></a>
                    <p class = "text-xs font-subheader">Where to find me</p>
                </div>
            </nav>
        </div>
    </div>
</div>
