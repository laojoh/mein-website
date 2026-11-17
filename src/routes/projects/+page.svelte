<script lang="ts">
    import Star from "$lib/components/Star.svelte";
    import TypeWriter from "$lib/components/TypeWriter.svelte";
    import AmbientShapes from "$lib/components/AmbientShapes.svelte";
    import { onMount, onDestroy } from "svelte";

    let x = 0;
    let y = 0;

    let targetX = 0;
    let targetY = 0;

    onMount(() => {
        const handleMouseMove = (e: { clientX: number; clientY: number; }) => {
            targetX = (e.clientX / window.innerWidth - 0.5) * 2;
            targetY = (e.clientY / window.innerHeight - 0.5) * 2;
        };

        window.addEventListener('mousemove', handleMouseMove);

        // @ts-ignore
        let animationFrame;

        const animate = () => {
            x += (targetX - x) * 0.05;
            y += (targetY - y) * 0.05;

            animationFrame = requestAnimationFrame(animate);
        };

        animate();

        return () => {
            window.removeEventListener('mousemove', handleMouseMove);
            // @ts-ignore
            cancelAnimationFrame(animationFrame);
        };
    });

import * as THREE from 'three';
let canvas: HTMLCanvasElement;

onMount(() => {
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(45, innerWidth / innerHeight, 0.1, 100);
    camera.position.z = 8;

    const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
    renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
    renderer.setSize(innerWidth, innerHeight);

    // temporary placeholder, swap for real models later
    const mesh = new THREE.Mesh(
        new THREE.TorusKnotGeometry(1, 0.3, 100, 16),
        new THREE.MeshNormalMaterial()
    );
    scene.add(mesh);

    const onResize = () => {
        camera.aspect = innerWidth / innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(innerWidth, innerHeight);
    };
    window.addEventListener('resize', onResize);

    let frame: number;
    const tick = () => {
        mesh.rotation.y += 0.005;
        renderer.render(scene, camera);
        frame = requestAnimationFrame(tick);
    };
    tick();

    return () => {
        window.removeEventListener('resize', onResize);
        cancelAnimationFrame(frame);
        renderer.dispose();
    };
});
</script>

<div class = "p-10">
        <nav class = "relative w-full flex flex-row justify-start gap-4 items-center p-5 z-10">
            <a href="/projects">
              <div class = "text-8xl 2xl:text-9xl text-header font-header uppercase"  style={`transform: translate(${x * 15}px, ${y * 15}px);`}>
                <TypeWriter text = "Projects"/>
                </div>
            </a>
            <h1 class = "text-md 2xl:text-lg text-header font-subheader uppercase" style={`transform: translate(${x * 10}px, ${y * 10}px);`}> <a href = "../" >
                <TypeWriter text = "By John Lao"/>
            </a> </h1>

        </nav>

    
    <canvas bind:this={canvas} class="fixed inset-0 w-full h-full z-0"></canvas>

    <section class="relative z-10 min-h-screen ...">
        <a href="/projects/sat" class="group inline-block border-2 border-header bg-bg/80 p-6 max-w-md hover:bg-header hover:text-bg transition-colors">
            <div class="text-4xl font-header uppercase">SAT Math</div>
            <p class="font-subheader uppercase text-sm mt-2">596 question practice bank</p>
            <p class="font-body text-sm mt-3 opacity-70">Every hard math question from College Board's question bank, extracted from a 626-page PDF into a practice app with answer checking, explanations and progress tracking.</p>
        </a>
    </section>
    <section class="min-h-screen ..."> <!-- project 2 text --> </section>

</div>