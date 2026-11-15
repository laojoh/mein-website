<script lang="ts">
    import Star from "./Star.svelte";
</script>


<nav class="w-full flex flex-row justify-start gap-4 items-center p-5">
    <h1 class="text-5xl 2xl:text-7xl text-header font-header uppercase">
        <a href="/photography"> Photography</a>
    </h1>
    <h1 class="text-sm 2xl:text-md text-header font-subheader uppercase">
        <a href="/"> By John Lao</a>
    </h1>
    <Star
        size={50}
        stretchX={1}
        stretchY={1}
        rotation={0}
        waist = {0.3}
    />
</nav>