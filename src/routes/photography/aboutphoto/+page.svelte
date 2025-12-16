<script>
    import Header from "$lib/components/Header.svelte";
    import TypeWriter from "$lib/components/TypeWriter.svelte";

</script>
<div class = "bg-bg p-7 pl-15">
    <Header/>
    <nav class = "relative overflow-hidden">
        <img class = " group w-full h-75 rounded-xl object-cover object-center" loading = "lazy" src = "/images/aboutphoto/img1.jpg" alt = "China Thumbnail"/>
        <div class = " absolute inset-0 bg-imagebg opacity-0"></div>
        <p class  = "text-7xl font-header font-bold text-header absolute inset-0 flex items-center justify-center opacity-0text-center">
            <TypeWriter text = "ABOUT"/>
        </p>
    </nav>
</div>