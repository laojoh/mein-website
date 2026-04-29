<script lang="ts">
    import Header from "$lib/components/Header.svelte";
    // @ts-ignore
    import Tile from "$lib/components/Tile.svelte";

    let active: string | null = null;

</script>

<div class = "bg-bg p-7 pl-15">
    <Header/>
    <div class = "grid grid-cols-3 grid-rows-2 gap-y-15 w-full">
        <!-- Blue Angels -->
            <Tile
            id = "blue"
            active = {active}
            setActive = {(id) => active = id}
            img = "/images/portfolio thumbs/Blue Angels thumb.jpg"
            alt = "Blue Angels Thumbnail"
            title = "BLUE ANGELS"
            href = "collections/blueangels"
            />
        <!-- China -->
            <Tile
            id = "china"
            active = {active}
            setActive = {(id) => active = id}
            img = "/images/portfolio thumbs/China thumb.jpg"
            alt = "China Thumbnail"
            title = "CHINA"
            href = "collections/chinajul25"
            x = {32} y = {138}
            />
    </div>
</div>