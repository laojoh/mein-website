<script>
    import Header from "$lib/components/Header.svelte";
    import TypeWriter from "$lib/components/TypeWriter.svelte";

</script>
<div class = "bg-bg p-7 pl-15 2xl:p-10 2xl:pl-20">
    <Header/>
    <div class = "flex flex-col w-full ">
        <nav class = "relative overflow-hidden">
            <img class = " group w-full h-75 2xl:h-125 object-cover object-center" loading = "lazy" src = "/images/about/img1.jpg" alt = "The Bay Bridge"/>
            <div class = " absolute inset-0 bg-imagebg opacity-0"></div>
        </nav>
        <div class = "pl-20 pr-20 2xl:pl-40 2xl:pr-40">
            <p class  = "text-3xl 2xl:text-5xl font-header text-header inset-0 flex items-center justify-start text-center pt-10 pb-2.5 2xl:pt-20 2xl:pb-5">
                <TypeWriter text = "BEHIND THE CAMERA"/>
            </p>
            <div class = "flex flex-row gap-10 items-start justify-start w-full">
                <p class = "text-sm 2xl:text-lg font-body text-header indent-6 w-2/3">
                    If you didn't see my main page, hi! I'm John, a photographer based in the east Bay Area, California. Since I started taking candid photos for my friends in 7th grade, I've been intrigued by the craft of photography and the ability to capture moments unique to me and other people. This page is mainly about the photography facet of me, but I also have other pages for different creative outlets, all accessible through the main page!
                </p>
                <img class = "h-auto w-1/3 aspect-3/4 object-cover object-bottom" src = "/images/about/img2.jpg" alt = "John, the photographer"/>
            </div>
        </div>

    </div>
</div>