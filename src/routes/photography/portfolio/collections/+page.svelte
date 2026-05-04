<script lang="ts">
    import Back from "$lib/components/Back.svelte";
    import Header from "$lib/components/Header.svelte";
    // @ts-ignore
    import Tile from "$lib/components/Tile.svelte";

    let active: string | null = null;

</script>

<div class = "bg-bg p-7 pl-15">
    <Header/>
    <div class = "mt-5 mb-10">
        <Back/>
    </div>
    <div class = "grid grid-cols-3 grid-rows-2 gap-y-15 w-full 2xl:gap-10">
        <!-- Blue Angels -->
            <Tile
            id = "blue"
            active = {active}
            setActive = {(id) => active = id}
            img = "/images/portfolio thumbs/Blue Angels thumb.jpg"
            alt = "Blue Angels Thumbnail"
            title = "BLUE ANGELS"
            desc = "October 14, 2024"
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
            desc = "July 1-12, 2025"
            href = "collections/chinajul25"
            x = {{default: 34, '2xl': 25.5}}
            y = {{default: 55, '2xl': 123}}
            />
    </div>
</div>