<script lang="ts">
    import Back from "$lib/components/Back.svelte";
    import Header from "$lib/components/Header.svelte";
    import Lightbox from "$lib/components/Lightbox.svelte";
    import TypeWrite from "$lib/components/TypeWriter.svelte";
    import { TypeWriter } from "svelte-typewrite";
    import { onMount } from 'svelte';
    import { animate, onScroll } from 'animejs';

    let container: HTMLDivElement | null = null;
    let img2: HTMLDivElement | null = null;

    onMount(() => {
        if (!img2 || !container) return;
        animate(img2, {
            scale: [0, 1],
            duration: 1000,
            ease: 'linear',
            autoplay: onScroll({
                container: container,
                enter: 'bottom-=50',
                leave: 'top+=500',
                sync: true,
                debug: false,
            })
        });
    });
</script>

<div bind:this={container} class="bg-bg p-7 pl-15 h-screen overflow-y-scroll">
    <Header/>
    <nav class="grid grid-cols-6 grid-auto-rows gap-10 p-5">
        <Back/>
        <div class="col-start-5 col-span-2 row-start-2 text-header font-subheader">
            <h2 class="text-4xl 2xl:text-5xl font-header">
                <TypeWrite text="Project Background"/>
            </h2>
            <p class="text-md 2xl:text-lg font-body">
                <TypeWriter texts={["2025 was the first time I had ever been to China. Some of my family had gone before, but I had personally never been until July of that year."]} repeat={1} typeSpeed={15} endState={{text: "typed", caret: "hidden"}} blinkDuration={1000}/>
            </p>
        </div>

        <!-- Text -->
        <p class="font-body text-md col-start-1 col-span-3 row-start-8 row-span-2">
            Lorem ipsum dolor sit amet consectetur adipiscing elit. Sit amet consectetur adipiscing elit quisque faucibus ex. Adipiscing elit quisque faucibus ex sapien vitae pellentesque.
        </p>
        <p class="font-body text-md col-start-5 col-span-2 row-start-10 row-span-2">
            Lorem ipsum dolor sit amet consectetur adipiscing elit. Sit amet consectetur adipiscing elit quisque faucibus ex. Adipiscing elit quisque faucibus ex sapien vitae pellentesque.
        </p>
        
        <!-- Images -->
        <img class="zoomable col-start-3 col-span-2 row-start-1 row-span-3" 
            src="/images/china/display/china1.jpg" 
            data-full="/images/china/full/china1.jpg" 
            alt=""/>

        <div bind:this={img2} id="img2" class="col-start-2 col-span-4 row-start-4 row-span-2">
            <img class="zoomable"
                src="/images/china/display/china2.jpg"
                data-full="/images/china/full/china2.jpg"
                alt=""
            />
        </div>


        <img class="zoomable col-start-1 col-span-3 row-start-6 row-span-4"
            src="/images/china/display/china3.jpg"
            data-full="/images/china/full/china3.jpg"
            alt=""
        />

        <img class="zoomable col-start-4 col-span-3 row-start-6 row-span-4" 
            src="/images/china/display/china4.jpg" 
            data-full="/images/china/full/china4.jpg" 
            alt="" />

        <img class="zoomable col-start-2 col-span-3 row-start-10 row-span-2" 
            src="/images/china/display/china5.jpg" 
            data-full="/images/china/full/china5.jpg" 
            alt="" />
    </nav>
    <Lightbox/>
</div>