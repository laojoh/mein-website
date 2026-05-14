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
    <div class = "grid grid-cols-3 grid-auto-rows-auto gap-y-15 w-full place-items-center">
        <!-- Street -->
            <Tile
            id = "street"
            active = {active}
            setActive = {(id) => active = id}
            img = "/images/portfolio thumbs/Street thumb.jpg"
            alt = "Street Photography Thumbnail"
            title = "STREET"
            desc = ""
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
            desc =""
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
            desc = ""
            href = "series/automotive"
            x = {{default: -592, '2xl': -895}} 
            y = {{default: -46, '2xl': -37}}
            />
    </div>
</div>