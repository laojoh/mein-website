<script>
    import Header from "$lib/components/Header.svelte";
    // @ts-ignore
    import Tile from "$lib/components/Tile.svelte";

</script>

<div class = "bg-bg p-7 pl-15">
    <Header/>
    <div class = "grid grid-cols-3 grid-rows-2 gap-y-15 w-full">
        <!-- Portraiture -->
            <Tile img = "/images/portfolio thumbs/Portrait thumb.jpg" alt = "Portrait Thumbnail" title = "PORTRAITURE" href = "portfolio/portraiture"/>
        <!-- China -->
            <Tile img = "/images/portfolio thumbs/China thumb.png" alt = "China Thumbnail" title = "CHINA" href = "portfolio/china" x = {32} y = {138}/>
        <!-- Automotive -->
            <Tile img = "/images/portfolio thumbs/Automotive thumb.png" alt = "Automotive Thumbnail" title = "AUTOMOTIVE" href = "portfolio/automotive" x = {-547.5} y = {38}/>
        <!-- Blue Angels -->
            <Tile img = "/images/portfolio thumbs/Blue Angels thumb.png" alt = "Blue Angels Thumbnail" title = "BLUE ANGELS" href = "portfolio/blueangels"/>
        <!-- Street -->
            <Tile img = "/images/portfolio thumbs/Street thumb.jpg" alt = "Street Photography Thumbnail" title = "STREET" href = "portfolio/street"/>
    </div>
</div>