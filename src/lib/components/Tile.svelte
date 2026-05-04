<script lang="ts">
    import { goto } from '$app/navigation';

    export let href: string;
    export let title: string;
    export let desc: string | null;
    export let img: string;
    export let alt: string;
    export let x: number | Record<string, number> = 0;
    export let y: number | Record<string, number> = 0;
    export let id: string;
    export let active: string | null;
    export let setActive: (id: string) => void;

    let animate = false;
    let adjustedY = 0;
    let screenWidth = 0;

    function resolve(val: number | Record<string, number>, width: number) {
        if (typeof val === 'number') return val;
        if (width >= 1536) return val['2xl'] ?? val['default'] ?? 0;
        return val['default'] ?? 0;
    }

    $: resolvedX = resolve(x, screenWidth);
    $: resolvedY = resolve(y, screenWidth);

    function open() {
        adjustedY = resolvedY + window.scrollY;
        setActive(id);
        animate = true;

        setTimeout(() => {
            goto(href);
        }, 1000);
    }
</script>

<svelte:window bind:innerWidth={screenWidth} />

<nav class="relative">
    <!-- svelte-ignore a11y_click_events_have_key_events -->
    <!-- svelte-ignore a11y_no_static_element_interactions -->
    <div
        on:click={open}
        class="block relative overflow-hidden group w-100 2xl:w-160 transition-all duration-1000 ease-in-out origin-center will-change-transform cursor-pointer"
        style={`
            transform: ${
                animate
                    ? `translate(${resolvedX}px, ${adjustedY}px) scale(1.05)`
                    : active && active !== id
                    ? 'scale(1.00)'
                    : 'none'
            };
            opacity: ${active && active !== id ? 0 : 1};
            filter: ${active && active !== id ? 'blur(2px)' : 'none'};
            z-index: ${animate ? 50 : 1};
        `}
    >
        <img class="w-100 2xl:w-160 aspect-square object-cover transition-transform duration-500 group-hover:scale-105" loading="lazy" src={img} alt={alt}/>
        <div class="absolute inset-0 bg-imagebg opacity-15 group-hover:opacity-0 transition-opacity duration-300"></div>
        <div class="text-white absolute inset-0 flex flex-col items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300 text-center">
            <p class="text-4xl font-subheader font-bold">{title}</p>
            <p class="text-lg font-body">{desc}</p>
        </div>
    </div>
</nav>