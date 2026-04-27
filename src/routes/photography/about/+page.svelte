<script>
    import Header from "$lib/components/Header.svelte";
    import TypeWriter from "$lib/components/TypeWriter.svelte";

</script>
<div class = "bg-bg p-7 pl-15">
    <Header/>
    <div class = "flex flex-col w-full gap-10">
        <nav class = "relative overflow-hidden">
            <img class = " group w-full h-75 object-cover object-center" loading = "lazy" src = "/images/aboutphoto/img1.jpg" alt = "China Thumbnail"/>
            <div class = " absolute inset-0 bg-imagebg opacity-0"></div>
        </nav>
        <p class  = "text-3xl font-header text-header inset-0 flex items-center justify-start text-center">
            <TypeWriter text = "BEHIND THE CAMERA"/>
        </p>
        <div class = "flex flex-row gap-10 items-start justify-start w-full">
            <p class = "text-md font-subheader text-header indent-6 w-1/2">
                Hi! I'm John, a photographer based in the east Bay Area, California. Since I started taking candid photos for my friends in 7th grade, I've been intrigued by the craft of photography and the ability to capture moments unique to me and other people.
            </p>
            <img class = "h-auto w-1/2" src = "/images/placeholder images/placeholder6.jpg" alt = "John, the photographer"/>
        </div>

    </div>
</div>