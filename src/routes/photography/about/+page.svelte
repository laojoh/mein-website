<script>
    import Header from "$lib/components/Header.svelte";
    import TypeWriter from "$lib/components/TypeWriter.svelte";

</script>
<div class = "bg-bg p-7 pl-15 2xl:p-10 2xl:pl-20">
    <Header/>
    <div class = "flex flex-col w-full ">
        <div class = "relative overflow-hidden">
            <img class = " group w-full h-75 2xl:h-125 object-cover object-center" loading = "lazy" src = "/images/about/img1.jpg" alt = "The Bay Bridge"/>
            <div class = " absolute inset-0 bg-imagebg opacity-0"></div>
        </div>
        <div class = "pl-20 pr-20 mt-10 2xl:pl-40 2xl:pr-40">
            <div class = "flex flex-row items-start justify-start w-full gap-10">
                <div>
                    <p class  = "text-4xl 2xl:text-6xl font-header text-header inset-0 flex items-center justify-start text-center pt-10 pb-2.5 2xl:pt-20 2xl:pb-5">
                        <TypeWriter text = "BEHIND THE CAMERA"/>
                    </p>
                    <p class = "text-lg/7 2xl:text-xl/8 font-body text-header indent-6 w-full">
                        If you didn't see my main page about me, Hello! I'm John, a photographer based in the east Bay Area, California. Since I started taking candid photos for my friends in 7th grade, I've been intrigued by the craft of photography and the ability to capture moments unique to me and other people. This page is mainly about the photography facet of me, but I also have other pages for different creative outlets, all accessible through the main page!
                        <br><br>
                        My interest kicked off when I took my first week-long unofficial class on photography in 7th grade. I had lots of fun taking photos with my friends, especially with my first new phone! As I developed my skill more and more, my friend started asking me to take photos for her to post on her social media pages. Of course, since I liked photographing, I agreed.
                    </p>
                </div>
                <img class = "h-auto w-2/5 aspect-4/5 object-cover object-bottom" src = "/images/about/img2.jpg" alt = "John, the photographer"/>
            </div>
        </div>
    </div>
</div>