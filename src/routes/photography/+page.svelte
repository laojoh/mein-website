<script lang="ts">
  import TypeWriter from "$lib/components/TypeWriter.svelte";
  import { onMount, onDestroy } from "svelte";

  let images: string[] = [
    "/images/photo home/img1.jpg",
    "/images/photo home/img2.jpg",
    "/images/photo home/img3.jpg",
    "/images/photo home/img4.jpg",
    "/images/photo home/img5.jpg",
    "/images/photo home/img6.jpg",
  ];

  let index = 0;
  let interval: ReturnType<typeof setInterval>;

  onMount(() => {
    interval = setInterval(() => {
      index = (index + 1) % images.length;
    }, 5000); // every 5 seconds
  });

  onDestroy(() => {
    clearInterval(interval);
  });
</script>

<div class = "bg-bg p-7 pl-15">
    <div class = "flex">
        <!-- Header -->
        <nav class = "w-full flex flex-row justify-start gap-4 items-start p-5 ">
            <a href="/photography">
              <div class = "text-7xl 2xl:text-8xl text-header font-header uppercase">
                <TypeWriter text = "Photography"/>
              </div>
            </a>
            <h1 class = "text-xs 2xl:text-lg text-header font-subheader uppercase"> <a href = "../">
            <TypeWriter text = "By John Lao"/>
            </a> </h1>
        </nav>
        <!-- Menu -->
        <nav class = "flex flex-col gap-10 origin-top-left rotate-90 text-header font-header text-5xl uppercase absolute top-30 -right-60 p-5 2xl:top-36 2xl:-right-72">
        <!-- Portfolio -->
            <a class = "flex w-full gap-7 items-center group cursor-pointer transition-transform duration-300 hover:scale-110"
              href = "photography/portfolio">
                <h2 class = "text-5xl 2xl:text-6xl font-header">
                  <TypeWriter text = "portfolio"/>
                </h2>
                <p class = "text-xs 2xl:text-lg font-subheader -rotate-90 w-10 text-center">
                  <!-- <TypeWriter text = "my photo projects"/> --> My photo projects
                </p>
            </a>
        <!-- About -->
            <a class = "flex w-full gap-10 items-center group cursor-pointer transition-transform duration-300 hover:scale-110"
              href = "photography/about">
                <h2 class = "text-5xl 2xl:text-6xl font-header">
                  <TypeWriter text = "A Glimpse"/>
                </h2>
                <p class = "text-xs 2xl:text-lg font-subheader -rotate-90 w-10 text-center">
                  <!-- <TypeWriter text = "A little about me"/> --> A little about me
                </p>
            </a>
        <!-- Contact -->
            <a class = "flex w-full gap-10 items-center group cursor-pointer transition-transform duration-300 hover:scale-110"
              href = "photography/contact">
                <h2 class = "text-5xl 2xl:text-6xl font-header">
                  <TypeWriter text = "Contact"/>
                </h2>
                <p class = "text-xs 2xl:text-lg font-subheader -rotate-90 w-10 text-center">
                  <!-- <TypeWriter text = "Where to find me"/> --> Where to find me
                </p>
              </a>
        <!-- Sevices -->
          <a class = "flex w-full gap-3 items-center group cursor-pointer transition-transform duration-300 hover:scale-110"
            href = "photography/services">
                <h2 class = "text-5xl 2xl:text-6xl font-header">
                  <TypeWriter text = "Services"/>
                </h2>
                <p class = "text-xs 2xl:text-lg font-subheader -rotate-90 w-10 text-center">
                  <!-- <TypeWriter text = "For you"/> --> For you
                </p>
            </a>
        </nav>
    </div>
    <!-- Slideshow -->
    <div class="relative md:w-212 2xl:w-350 aspect-5/4 overflow-hidden bg-imagebg">
    {#each images as src, i}
      <img
        src={src}
        alt=""
        class={`absolute inset-0 w-full h-full object-cover transition-opacity duration-1000 ${
        i === index ? "opacity-100" : "opacity-0"
      }`}
      />
    {/each}
</div>


</div>
