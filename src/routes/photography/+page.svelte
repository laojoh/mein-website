<script lang="ts">
    import Star from "$lib/components/Star.svelte";
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


  let x = 0;
  let y = 0;

  let targetX = 0;
  let targetY = 0;

  let index = 0;
  let interval: ReturnType<typeof setInterval>;

  onMount(() => {
    interval = setInterval(() => {
      index = (index + 1) % images.length;
    }, 5000); // every 5 seconds

    const handleMouseMove = (e: { clientX: number; clientY: number; }) => {
        targetX = (e.clientX / window.innerWidth - 0.5) * 2;
        targetY = (e.clientY / window.innerHeight - 0.5) * 2;
        };

        window.addEventListener('mousemove', handleMouseMove);

        // @ts-ignore
        let animationFrame;

        const animate = () => {
        x += (targetX - x) * 0.05;
        y += (targetY - y) * 0.05;

        animationFrame = requestAnimationFrame(animate);
        };

        animate();

        return () => {
        window.removeEventListener('mousemove', handleMouseMove);
        // @ts-ignore
        cancelAnimationFrame(animationFrame);
        };
  });

  onDestroy(() => {
    clearInterval(interval);
  });


</script>

<div class = "bg-bg p-7 pl-15">
    <div class = "flex">
        <div class = pointer-events-none>
            <!-- planet -->
            <div class = "absolute bottom-20 right-57" style={`transform: translate(${x * 10}px, ${y * 10}px);`}>
                <Star
                size={100}
                stretchX={1}
                stretchY={1}
                rotation={0}
                />
            </div>
        </div>
        <!-- Header -->
        <nav class = "w-full flex flex-row justify-start gap-4 items-center p-5 ">
            <a href="/photography">
              <div class = "text-8xl 2xl:text-9xl text-header font-header uppercase"  style={`transform: translate(${x * 15}px, ${y * 15}px);`}>
                <TypeWriter text = "Photography"/>
              </div>
            </a>
            <h1 class = "text-md 2xl:text-lg text-header font-subheader uppercase" style={`transform: translate(${x * 10}px, ${y * 10}px);`}> <a href = "../" >
            <TypeWriter text = "By John Lao"/>
            </a> </h1>
        </nav>
        <!-- Menu -->
        <nav class = "flex flex-col gap-10 origin-top-left rotate-90 text-header font-header text-5xl uppercase absolute top-30 -right-60 p-5 2xl:top-36 2xl:-right-72" style={`transform: translate(${y * 15}px, ${x * -15}px);`}>
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
                  <TypeWriter text = "About"/>
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
    <div class="relative md:w-212 2xl:w-350 aspect-5/4 overflow-hidden bg-imagebg" style={`transform: translate(${x * 20}px, ${y * 20}px);`}>
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
