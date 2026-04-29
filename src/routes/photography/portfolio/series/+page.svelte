<script lang="ts">
    import Header from "$lib/components/Header.svelte";
    // @ts-ignore
    import Tile from "$lib/components/Tile.svelte";

    let active: string | null = null;

</script>

<div class = "bg-bg p-7 pl-15">
    <Header/>
    <div class = "grid grid-cols-3 grid-rows-2 gap-y-15 w-full">
        <!-- Street -->
            <Tile
            id = "street"
            active = {active}
            setActive = {(id) => active = id}
            img = "/images/portfolio thumbs/Street thumb.jpg"
            alt = "Street Photography Thumbnail"
            title = "STREET"
            href = "series/street"
            />
        <!-- Portraiture -->
            <Tile
            id = "portraiture"
            active = {active}
            setActive = {(id) => active = id}
            img = "/images/portfolio thumbs/Portrait thumb.jpg"
            alt = "Portrait Thumbnail"
            title = "PORTRAITURE"
            href = "series/portraiture"
            />
        <!-- Automotive -->
            <Tile
            id = "auto"
            active = {active}
            setActive = {(id) => active = id}
            img = "/images/portfolio thumbs/Automotive thumb.jpg"
            alt = "Automotive Thumbnail"
            title = "AUTOMOTIVE"
            href = "series/automotive"
            x = {-547.5} y = {38}
            />
    </div>
</div>