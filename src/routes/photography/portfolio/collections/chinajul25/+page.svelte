<script lang="ts">
    import Back from "$lib/components/Back.svelte";
	import Header from "$lib/components/Header.svelte";
    import Lightbox from "$lib/components/Lightbox.svelte";
    import TypeWrite from "$lib/components/TypeWriter.svelte";
    import { TypeWriter } from "svelte-typewrite";

</script>

<div class = "bg-bg p-7 pl-15">
    <Header/>
    <nav class = "grid grid-cols-6 grid-auto-rows gap-10 p-5">
        <Back/>
        <div class = "col-start-5 col-span-2 row-start-2 text-header font-subheader">
            <h2 class = "text-3xl font-header">
                <TypeWrite text="Project Background"/>
            </h2>
            <p class = "text-md font-body">
                <TypeWriter texts={["Lorem ipsum dolor sit amet consectetur adipiscing elit. Sit amet consectetur adipiscing elit quisque faucibus ex. Adipiscing elit quisque faucibus ex sapien vitae pellentesque."]} repeat={1} typeSpeed={15} endState={{text: "typed", caret: "hidden"}} blinkDuration={1000}/>
            </p>
        </div>

        <p class = "font-body text-md col-start-1 col-span-3 row-start-8 row-span-2">
            Lorem ipsum dolor sit amet consectetur adipiscing elit. Sit amet consectetur adipiscing elit quisque faucibus ex. Adipiscing elit quisque faucibus ex sapien vitae pellentesque.
        </p>
        <p class = "font-body text-md col-start-5 col-span-2 row-start-10 row-span-2">
            Lorem ipsum dolor sit amet consectetur adipiscing elit. Sit amet consectetur adipiscing elit quisque faucibus ex. Adipiscing elit quisque faucibus ex sapien vitae pellentesque.
        </p>
        
        <img class = "zoomable col-start-3 col-span-2 row-start-1 row-span-3" src="/images/china/display/china1.jpg" data-full="/images/china/full/china1.jpg" alt="" />
        <img class = "zoomable col-start-2 col-span-4 row-start-4 row-span-2" src="/images/china/display/china2.jpg" data-full="/images/china/full/china2.jpg" alt="" />
        <img class = "zoomable col-start-1 col-span-3 row-start-6 row-span-3" src="/images/china/display/china3.jpg" data-full="/images/china/full/china3.jpg" alt="" />
        <img class = "zoomable col-start-4 col-span-3 row-start-6 row-span-4" src="/images/china/display/china4.jpg" data-full="/images/china/full/china4.jpg" alt="" />
        <img class = "zoomable col-start-2 col-span-3 row-start-10 row-span-2" src="/images/china/display/china5.jpg" data-full="/images/china/full/china5.jpg" alt="" />
    </nav>
    <Lightbox/>
</div>
