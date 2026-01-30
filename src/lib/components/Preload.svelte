<script lang="ts">
    let {path} = $props();
</script>

<svelte:head>
    <link rel = "preload" as = "image" href = {path}/>
</svelte:head>