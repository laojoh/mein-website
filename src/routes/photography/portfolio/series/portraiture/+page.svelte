<script>
    import Back from "$lib/components/Back.svelte";
    import Header from "$lib/components/Header.svelte";
    import TypeWrite from "$lib/components/TypeWriter.svelte";
    import { TypeWriter } from "svelte-typewrite";

</script>
<div class = "bg-bg p-7 pl-15">
    <Header/>
    <div class = "absolute">
        <Back/>
    </div>
    <div class = "relative">
        <div class = "flex flex-row gap-5 items-center place-content-center">
            <img class="zoomable w-100 2xl:w-175"
                src="/images/portraiture/display/portraiture1.jpg"
                data-full="/images/portraiture/full/portraiture1.jpg"
                alt=""/>
        </div>
        <div class="text-header font-subheader w-100 absolute top-70 2xl:top-70 left-230 2xl:left-365">
            <h2 class="text-4xl 2xl:text-5xl font-header">
                <TypeWrite text="Project Background"/>
            </h2>
            <p class="text-md 2xl:text-lg font-body">
                <TypeWriter texts={["If you read my about me page, you'll know I started off photography taking pictures of my friends. Since then, I've expanded my skillset and portfolio."]} repeat={1} typeSpeed={15} endState={{text: "typed", caret: "hidden"}} blinkDuration={1000}/>
            </p>
        </div>
    </div>


</div>