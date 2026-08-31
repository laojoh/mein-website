<script lang="ts">
    export let size = 100;
    export let stretchX = 1;
    export let stretchY = 1;
    export let rotation = 0;
    export let color : string = "black";
    // How full each arm is: 1 = original shape, lower = skinnier/pointier arms,
    // higher = rounder/chubbier arms. This just scales how close the curve
    // between each tip pulls in toward the center — no coordinate math needed.
    export let waist = 1;

    // The 8 control points below are the original hand-placed ones (waist = 1),
    // each written as an offset from the center (50, 50) so scaling by `waist`
    // pulls them toward/away from the center symmetrically.
    $: cp1 = 50 + 3 * waist;
    $: cp2 = 50 - 20 * waist;
    $: cp3 = 50 + 20 * waist;
    $: cp4 = 50 - 3 * waist;
    $: cp5 = 50 - 3 * waist;
    $: cp6 = 50 + 20 * waist;
    $: cp7 = 50 - 20 * waist;
    $: cp8 = 50 + 3 * waist;

    $: starPath = `M50 0 C${cp1} ${cp2} ${cp3} ${cp4} 100 50 C${cp3} ${cp8} ${cp1} ${cp6} 50 100 C${cp5} ${cp6} ${cp7} ${cp8} 0 50 C${cp7} ${cp4} ${cp5} ${cp2} 50 0 Z`;
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
        <path d={starPath} fill={color} />
    </g>
</svg>
