<script lang="ts">
	import Back from "$lib/components/Back.svelte";
    import Header from "$lib/components/PhotoHeader.svelte";
    import Lightbox from "$lib/components/Lightbox.svelte";
    import TypeWrite from "$lib/components/TypeWriter.svelte";
    import { TypeWriter } from "svelte-typewrite";
    import { onMount } from "svelte";
    import { animate, onScroll } from "animejs";

    let container: HTMLDivElement | null = null;
    let img1: HTMLDivElement | null = null;
    let img2: HTMLDivElement | null = null;
    let img3: HTMLImageElement | null = null;
    let img4: HTMLImageElement | null = null;
    let txt1: HTMLDivElement | null = null;
    let img5: HTMLImageElement | null = null;
    let img6: HTMLImageElement | null = null;
    let img7: HTMLImageElement | null = null;

    onMount(() => {

        if (!container) return;
        // @ts-ignore
        animate(img1, {
            duration: 1000,
            ease: "linear",
            opacity: [0, 1],
            x: "20vh",
            autoplay: onScroll({
                container: container,
                enter: "bottom-=50 top+=200",
                leave: "top+=700 bottom-=200",
                sync: true,
                debug: false,
            }),
        });

        // @ts-ignore
        animate(img2, {
            duration: 1000,
            ease: "linear",
            opacity: [0, 1],
            x: "-10vh",
            autoplay: onScroll({
                container: container,
                enter: "bottom-=50 top+=200",
                leave: "top+=700 bottom-=200",
                sync: true,
                debug: false,
            }),
        });

        // @ts-ignore
        animate(img3, {
            duration: 1000,
            ease: "linear",
            opacity: [0, 1],
            x: -150,
            autoplay: onScroll({
                container: container,
                enter: "bottom-=50 top+=100",
                leave: "top+=700 bottom-=200",
                sync: true,
                debug: false,
            }),
        });

        // @ts-ignore
        animate(img4, {
            duration: 1000,
            ease: "linear",
            opacity: [0, 1],
            y: -200,
            autoplay: onScroll({
                container: container,
                enter: "bottom-=50 top-=300",
                leave: "top+=700 bottom-=500",
                sync: true,
                debug: false,
            }),
        })

    });

</script>

<div bind:this = {container} class = "bg-bg p-7 pl-15 h-screen overflow-y-scroll">
    <Header/>
    <Back/>
    <div class = "relative h-150 2xl:h-200">
        <div class = "flex flex-row gap-5 items-center absolute left-50 2xl:left-125">
            <img class="zoomable h-125 aspect-4/3 object-cover 2xl:h-175"
                src="/images/blueangels/display/blueangels1.jpg"
                data-full="/images/blueangels/full/blueangels1.jpg"
                alt=""/>
        </div>
        <div class="text-header font-subheader w-100 absolute top-60 2xl:top-70 left-230 2xl:left-365">
            <h2 class="text-4xl 2xl:text-5xl font-header">
                <TypeWrite text="Project Background"/>
            </h2>
            <p class="text-md 2xl:text-lg font-body">
                <TypeWriter texts={["Cool planes have always piqued my interest, especially military aircraft. So, when the Blue Angels came out near me, I went to go take some photos!"]} repeat={1} typeSpeed={15} endState={{text: "typed", caret: "hidden"}} blinkDuration={1000}/>
            </p>
        </div>
    </div>

    <div class = "relative h-auto pt-10"> 
        <img bind:this = {img1} class = "zoomable h-125 aspect-4/3 object-cover 2xl:h-175 absolute left-68"
            src="/images/blueangels/display/blueangels2.jpg"
            data-full="/images/blueangels/full/blueangels2.jpg"
            alt=""/>

        <img bind:this = {img2} class = "zoomable h-125 aspect-4/3 object-cover 2xl:h-175 absolute left-50 top-200"
            src="/images/blueangels/display/blueangels3.jpg"
            data-full="/images/blueangels/full/blueangels3.jpg"
            alt=""/>

        <img bind:this = {img3} class = "zoomable h-125 aspect-4/3 object-cover 2xl:h-175 absolute left-310 top-300"
            src="/images/blueangels/display/blueangels4.jpg"
            data-full="/images/blueangels/full/blueangels4.jpg"
            alt=""/>

        <img bind:this = {img4} class = "zoomable h-125 aspect-4/3 object-cover 2xl:h-175 absolute left-22 top-440"
            src="/images/blueangels/display/blueangels5.jpg"
            data-full="/images/blueangels/full/blueangels5.jpg"
            alt=""/>

        <img bind:this = {img5} class = "zoomable h-125 aspect-4/3 object-cover 2xl:h-175 absolute top-1000 left-50 2xl:left-125"
            src="/images/blueangels/display/blueangels6.jpg"
            data-full="/images/blueangels/full/blueangels6.jpg"
            alt=""/>

        <img bind:this = {img6} class = "zoomable h-125 aspect-4/3 object-cover 2xl:h-175 absolute top-800 left-100 2xl:left-200"
            src="/images/blueangels/display/blueangels7.jpg"
            data-full="/images/blueangels/full/blueangels7.jpg"
            alt=""/>

        <img bind:this = {img7} class = "zoomable h-125 aspect-4/3 object-cover 2xl:h-175 absolute top-1200 left-150 2xl:left-275"
            src="/images/blueangels/display/blueangels8.jpg"
            data-full="/images/blueangels/full/blueangels8.jpg"
            alt=""/>

    </div>


    <Lightbox/>
</div>