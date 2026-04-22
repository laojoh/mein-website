<script lang="ts">
	import B2Port from "$lib/components/B2Port.svelte";
    import Header from "$lib/components/Header.svelte";
    import Lightbox from "$lib/components/Lightbox.svelte";
    import TypeWrite from "$lib/components/TypeWriter.svelte";
    import { TypeWriter } from "svelte-typewrite";
    import { onMount } from "svelte";
    import Preload from "$lib/components/Preload.svelte";

</script>

<Preload path = "/images/china/china1.jpg"/>

<div class = "bg-bg p-7 pl-15">
    <Header/>
    <nav class = "grid grid-cols-6 grid-auto-rows gap-10 p-5">
        <B2Port/>
        <div class = "col-start-5 col-span-2 row-start-2 text-header font-subheader">
            <h2 class = "text-3xl">
                <TypeWrite text="Project Background"/>
            </h2>
            <p class = "text-md">
                <TypeWriter texts={["Lorem ipsum dolor sit amet consectetur adipiscing elit. Sit amet consectetur adipiscing elit quisque faucibus ex. Adipiscing elit quisque faucibus ex sapien vitae pellentesque."]} repeat={1} typeSpeed={15} endState={{text: "typed", caret: "hidden"}} blinkDuration={1000}/>
            </p>
        </div>

        <p class = "font-subheader text-xl col-start-1 col-span-3 row-start-8 row-span-2">
            Lorem ipsum dolor sit amet consectetur adipiscing elit. Sit amet consectetur adipiscing elit quisque faucibus ex. Adipiscing elit quisque faucibus ex sapien vitae pellentesque.
        </p>
        
        <img class = "zoomable col-start-3 col-span-2 row-start-1 row-span-3" src="/images/china/china1.jpg" alt="" />
        <img class = "zoomable col-start-2 col-span-4 row-start-4 row-span-2" src="/images/china/china2.jpg" alt="" />
        <img class = "zoomable col-start-1 col-span-3 row-start-6 row-span-2" src="/images/china/china3.jpg" alt="" />
        <img class = "zoomable col-start-4 col-span-3 row-start-6 row-span-4" src="/images/china/china4.jpg" alt="" />
        <img class = "zoomable col-start-1 col-span-3 row-start-10 row-span-2" src="/images/china/china5.jpg" alt="" />
    </nav>
    <Lightbox/>
</div>
