<script lang="ts">
    import Header from "$lib/components/Header.svelte";
    import B2Port from "$lib/components/Back.svelte";
    import Lightbox from "$lib/components/Lightbox.svelte";
    import TypeWrite from "$lib/components/TypeWriter.svelte";
    import { TypeWriter } from "svelte-typewrite";
    import Preload from "$lib/components/Preload.svelte";
</script>

<div class = "bg-bg p-7 pl-15">
    <Header/>
    <nav class="grid grid-cols-6 grid-auto-rows gap-10 p-5">
        <B2Port/>
        <div class="col-start-5 col-span-2 row-start-4 text-header font-subheader">
            <h2 class="text-3xl font-header">
                <TypeWrite text="Project Background"/>
            </h2>
            <p class="text-md font-body">
                <TypeWriter texts={["Lorem ipsum dolor sit amet consectetur adipiscing elit. Sit amet consectetur adipiscing elit quisque faucibus ex. Adipiscing elit quisque faucibus ex sapien vitae pellentesque."]} repeat={1} typeSpeed={15} endState={{text: "typed", caret: "hidden"}} blinkDuration={1000}/>
            </p>
        </div>

        <p class="text-md font-body col-start-4 col-span-3 row-start-8 row-span-2">
            Lorem ipsum dolor sit amet consectetur adipiscing elit. Sit amet consectetur adipiscing elit quisque faucibus ex. Adipiscing elit quisque faucibus ex sapien vitae pellentesque.
        </p>

        <img class="zoomable col-start-2 col-span-3 row-start-1 row-span-4 " src="/images/automotive/display/automotive1.jpg" data-full = "/images/automotive/full/automotive1.jpg" alt="" />
        <img class="zoomable col-start-2 col-span-2 row-start-7 row-span-2 " src="/images/automotive/display/automotive2.jpg" data-full = "/images/automotive/full/automotive2.jpg" alt="" />
        <img class="zoomable col-start-1 col-span-3 row-start-5 row-span-2 " src="/images/automotive/display/automotive3.jpg" data-full = "/images/automotive/full/automotive3.jpg" alt="" />
        <img class="zoomable col-start-4 col-span-3 row-start-6 row-span-2 " src="/images/automotive/display/automotive4.jpg" data-full = "/images/automotive/full/automotive4.jpg" alt="" />
        <img class="zoomable col-start-1 col-span-2 row-start-9 row-span-2 " src="/images/automotive/display/automotive5.jpg" data-full = "/images/automotive/full/automotive5.jpg" alt="" />
    </nav>
    <Lightbox/>
</div>