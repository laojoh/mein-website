<script lang="ts">
  import { onMount, onDestroy } from "svelte";
  import { TypeWriter } from 'svelte-typewrite'

  let images: string[] = [
    "/images/photo home/img1.jpg",
    "/images/photo home/img2.jpg",
    "/images/photo home/img3.jpg",
    "/images/photo home/img4.jpg",
    "/images/photo home/img5.jpg",
    "/images/photo home/img6.jpg",
  ];

  let index = 0;
  let interval: number;

  onMount(() => {
    interval = setInterval(() => {
      index = (index + 1) % images.length;
    }, 3500); // every 3.5 seconds
  });

  onDestroy(() => {
    clearInterval(interval);
  });
</script>

<div class = "bg-bg p-7 pl-15">
    <div class = "flex">
        <!-- Header -->
        <nav class = "w-full flex flex-row justify-start gap-4 items-start rounded-xl p-5">
            <a href="/photography">
              <div class = "text-8xl text-header font-header uppercase">
                <TypeWriter texts={['photography']} repeat={1} typeSpeed={120} endState={{text: "typed", caret: "hidden"}} blinkDuration={1000}/>
              </div>
            </a>
            <h1 class = "text-xs text-header font-subheader uppercase"> <a href = "../">
            <TypeWriter texts={['By John Lao']} repeat={1} typeSpeed={120} endState={{text: "typed", caret: "hidden"}} blinkDuration={1000}/>
            </a> </h1>
        </nav>
        <!-- Menu -->
        <nav class = "flex flex-col gap-10 origin-top-left rotate-90 text-header font-header text-5xl uppercase absolute top-34 -right-60 rounded-xl p-5">
            <div class = "flex w-full gap-7 items-center">
                <a href = "/portfolio">
                  <TypeWriter texts={['portfolio']} repeat={1} typeSpeed={120} endState={{text: "typed", caret: "hidden"}} blinkDuration={1000}/>
                </a>
                <a class = "text-xs font-subheader -rotate-90 w-10 text-center" href = "/portfolio">
                  <TypeWriter texts={['my photo projects']} repeat={1} typeSpeed={120} endState={{text: "typed", caret: "hidden"}} blinkDuration={1000}/>
                </a>
            </div>
            <div class = "flex gap-7 items-center w-full">
                <a href = "/../aboutphoto">
                  <TypeWriter texts={['A Glimpse']} repeat={1} typeSpeed={120} endState={{text: "typed", caret: "hidden"}} blinkDuration={1000}/>
                </a>
                <p class = "text-xs font-subheader -rotate-90 w-10 text-center">
                  <TypeWriter texts={['A little about me']} repeat={1} typeSpeed={120} endState={{text: "typed", caret: "hidden"}} blinkDuration={1000}/>
                </p>
            </div>
            <div class = "flex w-full gap-7 items-center">
                <a href = "/contact">
                  <TypeWriter texts={['Contact']} repeat={1} typeSpeed={120} endState={{text: "typed", caret: "hidden"}} blinkDuration={1000}/>
                </a>
                <p class = "text-xs font-subheader -rotate-90 w-10 text-center">
                  <TypeWriter texts={['Where to find me']} repeat={1} typeSpeed={120} endState={{text: "typed", caret: "hidden"}} blinkDuration={1000}/>
                </p>
          </div>
          <div class = "flex w-full gap-3 items-center">
                <a href = "/contact">
                  <TypeWriter texts={['Services']} repeat={1} typeSpeed={120} endState={{text: "typed", caret: "hidden"}} blinkDuration={1000}/>
                </a>
                <p class = "text-xs font-subheader -rotate-90 w-10 text-center">
                  <TypeWriter texts={['For you']} repeat={1} typeSpeed={120} endState={{text: "typed", caret: "hidden"}} blinkDuration={1000}/>
                </p>
            </div>
        </nav>
        <!-- Seal -->
        <img class = "w-50 h-50 object-contain absolute right-47.5 top-140" src = "/images/favicon.svg" alt = "Photography Logo Seal"/>
    </div>
    <!-- Slideshow -->
    <div class="relative w-212 aspect-5/4 overflow-hidden bg-imagebg rounded-xl">
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
