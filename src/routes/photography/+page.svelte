<script lang="ts">
  import { onMount, onDestroy } from "svelte";

  let images: string[] = [
    "/images/placeholder images/placeholder1.jpg",
    "/images/placeholder images/placeholder2.jpg",
    "/images/placeholder images/placeholder3.jpg",
    "/images/placeholder images/placeholder4.jpg",
    "/images/placeholder images/placeholder5.jpg",
    "/images/placeholder images/placeholder6.jpg",
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

<div class = "bg-bg p-10">
    <div class = "flex">
        <nav class = "w-full flex flex-row justify-start gap-4 items-start">
            <h1 class = "text-7xl text-header font-header uppercase"> <a href = "/photography"> Photography</a> </h1>
            <h1 class = "text-xs text-header font-subheader uppercase"> <a href = "../"> By John Lao</a> </h1>
        </nav>
        <nav class = "flex flex-col gap-8 origin-top-left rotate-90 text-header font-header text-7xl uppercase absolute top-28 -right-75">
            <div class = "flex w-100 gap-4 items-center">
                <a href = "/portfolio">Portfolio</a>
                <a class = "text-xs font-subheader" href = "/portfolio">My photography projects</a>
            </div>
            <div class = "flex gap-4 items-center">
                <a class = "w-80"href = "/../about">A Glimpse</a>
                <p class = "text-xs font-subheader w-15">A little about me</p>
            </div>
            <div class = "flex w-80 gap-4 items-center">
                <a href = "/contact">Contact</a>
                <p class = "text-xs font-subheader">Where to find me</p>
          </div>
          <div class = "flex w-90 gap-4 items-center">
                <a href = "/contact">Services</a>
                <p class = "text-xs font-subheader">What I can do for you</p>
            </div>
        </nav>
    </div>
    <div class="relative w-212.5 aspect-5/4 overflow-hidden bg-imagebg rounded-xl">
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
