<script lang="ts">
  import { onMount, onDestroy } from "svelte";

  let images: string[] = [
    "/images/placeholder images/placeholder1.jpg",
    "/images/placeholder images/placeholder2.jpg",
    "/images/placeholder images/placeholder3.jpg",
    "/images/placeholder images/placeholder4.jpg",
    "/images/placeholder images/placeholder5.jpg",
  ];

  let index = 0;
  let interval: number;

  onMount(() => {
    interval = setInterval(() => {
      index = (index + 1) % images.length;
    }, 3000); // every 5 seconds
  });

  onDestroy(() => {
    clearInterval(interval);
  });
</script>

<div class = "bg-bg p-8">
    <div class = "flex">
        <nav class = "w-full flex flex-row justify-start gap-4 items-start">
            <h1 class = "text-7xl text-header font-header uppercase"> <a href = "/photography"> Photography</a> </h1>
            <h1 class = "text-xs text-header font-subheader uppercase"> <a href = "../"> By John Lao</a> </h1>
        </nav>
    </div>
    <div class="relative w-3xl aspect-5/4 overflow-hidden bg-imagebg rounded-2xl">
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
