<script lang="ts">
    export let size = 100;
    export let stretchX = 1;
    export let stretchY = 1;
    export let rotation = 0;
    export let color : string = "black";
</script>

<svg
    width={size}
    height={size}
    viewBox="0 0 100 100"
    xmlns="http://w3.org"
>
    <!-- 
    1. Translate(50, 50) moves the origin to the center of the canvas.
    2. Rotate and Scale are applied directly around this central origin.
    3. Translate(-50, -50) moves the shape back so its center aligns with the origin.
    -->
    <g transform={`translate(50, 50) rotate(${rotation}) scale(${stretchX}, ${stretchY}) translate(-50, -50)`}>
        <path
            d="
                M50 0
                C53 30 70 47 100 50
                C70 53 53 70 50 100
                C47 70 30 53 0 50
                C30 47 47 30 50 0
                Z
            "
            fill={color}
        />
    </g>
</svg>
