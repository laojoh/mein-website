<script lang="ts">
    import Back from "$lib/components/Back.svelte";
    import Header from "$lib/components/PhotoHeader.svelte";
    import Lightbox from "$lib/components/Lightbox.svelte";
    import TypeWrite from "$lib/components/TypeWriter.svelte";
    import { TypeWriter } from "svelte-typewrite";
    import { onMount } from 'svelte';
    import { animate, onScroll } from 'animejs';

    let container: HTMLDivElement | null = null;
    let img1: HTMLDivElement | null = null;
    let img2: HTMLDivElement | null = null;
    let img3: HTMLImageElement | null = null;
    let img4: HTMLImageElement | null = null;
    let txt1: HTMLDivElement | null = null;


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

    onMount(() => {
        if (!container) return;
        // @ts-ignore
        animate(img1, {
            duration: 1000,
            ease: 'linear',
            opacity: [0, 1],
            x: '20vh',
            autoplay: onScroll({
                container: container,
                enter: 'bottom-=50',
                leave: 'top+=700',
                sync: true,
                debug: false,
            })
        });

        // @ts-ignore
        animate(img2, {
            duration: 1000,
            ease: 'linear',
            opacity: [0, 1],
            x: '-10vh',
            autoplay: onScroll({
                container: container,
                enter: 'bottom-=50',
                leave: 'top+=700',
                sync: true,
                debug: false,
            })
        });

        // @ts-ignore
        animate(img3, {
            duration: 1000,
            ease: 'linear',
            opacity: [0, 1],
            y: -150,
            autoplay: onScroll({
                container: container,
                enter: 'bottom-=50 top-=100',
                leave: 'top+=700 top+=100',

                sync: true,
                debug: false,
            })
        });

        // @ts-ignore
        animate(txt1, {
            duration: 1000,
            ease: 'linear',
            opacity: [0, 1],
            y: 275,
            autoplay: onScroll({
                container: container,
                enter: 'bottom-=50 top-=100',
                leave: 'top+=500 bottom+=100',

                sync: true,
                debug: false,
            })
        });

        // @ts-ignore
        animate(img4, {
            duration: 1000,
            ease: 'linear',
            opacity: [0, 1],
            x: -250,
            autoplay: onScroll({
                container: container,
                enter: 'bottom-=50 top-=100',
                leave: 'bottom-=100 bottom-=400',

                sync: true,
                debug: false,
            })

        });
    });
</script>

<div bind:this={container} class="bg-bg p-7 pl-15 h-screen overflow-y-scroll">
    <div style={`transform: translate(${x * 10}px, ${y * 10}px);`}>
        <Header/>
    </div>
    <div style={`transform: translate(${x * 10}px, ${y * 10}px);`}>
        <Back/>
    </div>
    <div class = "relative" style={`transform: translate(${x * 15}px, ${y * 15}px);`}>
        <div class = "flex flex-row gap-5 items-center place-content-center">
            <img class="zoomable w-100 2xl:w-175"
                src="/images/china/display/china1.jpg"
                data-full="/images/china/full/china1.jpg"
                alt=""/>
        </div>
        <div class="text-header font-subheader w-100 absolute top-70 2xl:top-70 left-230 2xl:left-365">
            <h2 class="text-4xl 2xl:text-5xl font-header">
                <TypeWrite text="Project Background"/>
            </h2>
            <p class="text-md 2xl:text-lg font-body">
                <TypeWriter texts={["2025 was the first time I had ever been to China. Some of my family had gone before, but I had personally never been until July of that year."]} repeat={1} typeSpeed={15} endState={{text: "typed", caret: "hidden"}} blinkDuration={1000}/>
            </p>
        </div>
    </div>

        
    <div class = "relative h-auto pt-10 mb-10" style={`transform: translate(${x * 15}px, ${y * 15}px);`}>
        <img bind:this={img1} class = "zoomable w-150 2xl:w-225 absolute -left-37.5"
            src="/images/china/display/china2.jpg"
            data-full="/images/china/full/china2.jpg"
            alt=""
        />

        <img bind:this={img2} class="zoomable w-175 2xl:w-250 absolute left-180 top-30 2xl:left-293"
            src="/images/china/display/china3.jpg"
            data-full="/images/china/full/china3.jpg"
            alt=""
        />

        <img bind:this={img3} class="zoomable w-100 2xl:w-150 absolute top-160 left-50 2xl:top-215 2xl:left-94"
            src="/images/china/display/china4.jpg"
            data-full="/images/china/full/china4.jpg"
            alt="" />

        <p bind:this={txt1} class="font-body text-md 2xl:text-2xl w-150 2xl:w-200 absolute left-175 2xl:left-290 top-90 2xl:top-140">
            It all really started with an opportunity to go to China on a school trip. Before that, I had went to Taiwan at my previous school, but I had never been to mainland China. I was really excited to go, and I had a lot of fun while I was there. I took a lot of photos, and I wanted to share them with people. I also wanted to document my experience in China, and I thought that a photo series would be a good way to do that.
        </p>

        <img bind:this={img4} class="zoomable w-100 2xl:w-150 absolute top-200 left-225 2xl:top-270 2xl:left-330" 
            src="/images/china/display/china5.jpg" 
            data-full="/images/china/full/china5.jpg" 
            alt="" />

    </div>

    <Lightbox/>
</div>