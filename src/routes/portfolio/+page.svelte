<script>
    import Header from "$lib/components/Header.svelte";

</script>
<div class = "bg-bg p-7 pl-15">
    <Header/>
    <div class = "grid grid-cols-3 grid-rows-2 gap-y-15 w-full">
        <!-- Tile 1 -->
        <nav class = "relative">
            <a class = "block relative overflow-hidden group w-100 rounded-xl" href = "/china">
                <img class = " w-100 aspect-square object-cover transition-transform duration-500 group-hover:scale-110" loading = "lazy" src = "/images/portfolio thumbs/China thumb.png" alt = "China Thumbnail"/>
                <div class = " absolute inset-0 bg-imagebg opacity-15 group-hover:opacity-0 transition-opacity duration-300 rounded-xl"></div>
                <p class  = "text-4xl font-subheader font-bold text-white absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300 text-center">CHINA</p>
            </a>
        </nav>
        <!-- Tile 2 -->
        <nav>
            <a class = "block relative overflow-hidden group w-100 rounded-xl" href = "/automotive">
                <img class = " w-100 aspect-square object-cover transition-transform duration-500 group-hover:scale-110" loading = "lazy" src = "/images/portfolio thumbs/Automotive thumb.png" alt = "Automotive Thumbnail"/>
                <div class = " absolute inset-0 bg-imagebg opacity-15 group-hover:opacity-0 transition-opacity duration-300 rounded-xl"></div>
                <p class  = "text-4xl font-subheader font-bold text-white absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300 text-center">AUTOMOTIVE</p>
            </a>
        </nav>
        <!-- Tile 3 -->
        <nav>
            <a class = "block relative overflow-hidden group w-100 rounded-xl" href = "/blueangels">
                <img class = " w-100 aspect-square object-cover transition-transform duration-500 group-hover:scale-110" loading = "lazy" src = "/images/portfolio thumbs/Blue Angels thumb.png" alt = "Blue Angels Thumbnail"/>
                <div class = " absolute inset-0 bg-imagebg opacity-15 group-hover:opacity-0 transition-opacity duration-300 rounded-xl"></div>
                <p class  = "text-4xl font-subheader font-bold text-white absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300 text-center">BLUE ANGELS</p>
            </a>
        </nav>
        <!-- Tile 4 -->
        <nav>
            <a class = "block relative overflow-hidden group w-100 rounded-xl" href = "/street">
                <img class = " w-100 aspect-square object-cover transition-transform duration-500 group-hover:scale-110" loading = "lazy" src = "/images/portfolio thumbs/Street thumb.jpg" alt = "Street Photography Thumbnail"/>
                <div class = " absolute inset-0 bg-imagebg opacity-15 group-hover:opacity-0 transition-opacity duration-300 rounded-xl"></div>
                <p class  = "text-4xl font-subheader font-bold text-white absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300 text-center">STREET</p>
            </a>
        </nav>
    </div>
</div>