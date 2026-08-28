<script lang="ts">
    import Back from "$lib/components/Back.svelte";
    import Header from "$lib/components/PhotoHeader.svelte";
    import SCTile from "$lib/components/SCTile.svelte";

</script>

<div class = "bg-bg p-7 pl-15 ">
    <Header/>
    <div class = "grid grid-cols-2 gap-y-15 w-full p-10">
        <!-- Series -->
        <SCTile path = "portfolio/series" img = "/images/portfolio thumbs/series.jpg" title = "SERIES" desc = "ongoing projects"/>
        <!-- Collections -->
        <SCTile path = "portfolio/collections" img = "/images/portfolio thumbs/collections.jpg" title = "COLLECTIONS" desc = "moments in time"/>
    </div>
</div>