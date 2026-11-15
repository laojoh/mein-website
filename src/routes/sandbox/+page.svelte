<script lang="ts">
    import ModelViewer from '$lib/components/ModelViewer.svelte';

    const tiles: { shape?: 'knot' | 'cube' | 'octa' | 'torus'; src?: string; title: string }[] = [
        { src: '/models/B24-200.glb', title: 'B24-200' },
        { shape: 'knot', title: 'Knot' },
        { shape: 'cube', title: 'Cube' },
        { shape: 'octa', title: 'Octa' }
    ];
</script>

<div class="p-10">
    <h1 class="text-6xl font-header text-header uppercase mb-8">Sandbox</h1>

    <div class="grid grid-cols-2 lg:grid-cols-4 gap-6">
        {#each tiles as t}
            <a href="/projects" class="block border-2 border-header p-4 transition-transform duration-300 hover:scale-105">
                <ModelViewer shape={t.shape} src={t.src} />
                <h2 class="font-header text-header text-2xl uppercase mt-2">{t.title}</h2>
            </a>
        {/each}
    </div>
</div>
