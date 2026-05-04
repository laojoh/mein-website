<script lang="ts">
    
    export let path: string;
    export let img: string;
    export let title: string;
    export let desc: string;

</script>

<a class = "relative" href = {path}>
    <div class = "block relative overflow-hidden group w-150 2xl:w-225">
        <img class = "w-full aspect-4/3 object-cover transition-transform duration-500 group-hover:scale-105" loading = "lazy" src = {img} alt = ""/>
        <div class = "absolute inset-0 bg-imagebg opacity-15 group-hover:opacity-0 transition-opacity duration-300"></div>
        <div class = "font-subheader font-bold text-white absolute inset-0 flex items-start justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300 text-center mt-15">
            <div class = "flex flex-col gap-2 items-center justify-center">
                <p class = "text-4xl 2xl:text-5xl">{title}</p>
                <p class = "text-sm 2xl:text-lg uppercase">{desc}</p>
            </div>
        </div>
    </div>
</a>