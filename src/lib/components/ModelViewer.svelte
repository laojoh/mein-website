<script lang="ts">
    import * as THREE from 'three';
    import { getGLTFLoader } from '$lib/gltfLoader';
    import { mergeByMaterial } from '$lib/mergeByMaterial';
    import { buildOutline } from '$lib/buildOutline';
    import { onMount } from 'svelte';

    let {
        shape = 'knot',
        src = '',
        mode = 'outline',
        edgeAngle = 30,
        lineColor = '#000000',
        fillColor = '#ffffff',
        fill = true
    }: {
        shape?: 'knot' | 'cube' | 'octa' | 'torus';
        src?: string;
        mode?: 'outline' | 'shaded';
        edgeAngle?: number;
        lineColor?: string;
        fillColor?: string;
        fill?: boolean;
    } = $props();

    let canvas: HTMLCanvasElement;
    let hovered = false;
    let loading = $state(!!src);

    const geometries = {
        knot: () => new THREE.TorusKnotGeometry(1, 0.3, 64, 8),
        cube: () => new THREE.BoxGeometry(1.6, 1.6, 1.6),
        octa: () => new THREE.OctahedronGeometry(1.3),
        torus: () => new THREE.TorusGeometry(1, 0.4, 16, 48)
    };

    onMount(() => {
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(45, 1, 0.1, 100);
        camera.position.z = 5;

        scene.add(new THREE.AmbientLight(0xffffff, 1.4));
        const key = new THREE.DirectionalLight(0xffffff, 2);
        key.position.set(3, 4, 5);
        scene.add(key);

        const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
        renderer.setPixelRatio(Math.min(devicePixelRatio, 2));

        const pivot = new THREE.Group();
        pivot.rotation.x = 0.4;
        scene.add(pivot);

        const disposables: { dispose(): void }[] = [];
        let destroyed = false;

        const show = (root: THREE.Object3D) => {
            const t0 = performance.now();
            const { group, disposables: d } =
                mode === 'outline'
                    ? buildOutline(root, { edgeAngle, lineColor, fillColor, fill })
                    : mergeByMaterial(root);
            disposables.push(...d);

            const sphere = new THREE.Box3().setFromObject(group).getBoundingSphere(new THREE.Sphere());
            group.position.sub(sphere.center);
            pivot.scale.setScalar(1.8 / sphere.radius);
            pivot.add(group);

            console.info('[ModelViewer]', src || shape, {
                mode,
                buildMs: Math.round(performance.now() - t0),
                drawCalls: group.children.length
            });
        };

        if (src) {
            getGLTFLoader().load(src, (gltf) => {
                if (destroyed) return;
                show(gltf.scene);
                loading = false;
            });
        } else {
            show(new THREE.Mesh(geometries[shape](), new THREE.MeshStandardMaterial({ color: 0xcccccc })));
        }

        const resize = () => {
            const w = canvas.clientWidth;
            const h = canvas.clientHeight;
            renderer.setSize(w, h, false);
            camera.aspect = w / h;
            camera.updateProjectionMatrix();
        };
        resize();
        const ro = new ResizeObserver(resize);
        ro.observe(canvas);

        let visible = false;
        const io = new IntersectionObserver(([e]) => (visible = e.isIntersecting));
        io.observe(canvas);

        let speed = 0.005;
        let frame = 0;
        const tick = () => {
            frame = requestAnimationFrame(tick);
            if (!visible) return;
            speed += ((hovered ? 0.04 : 0.005) - speed) * 0.08;
            pivot.rotation.y += speed;
            renderer.render(scene, camera);
        };
        tick();

        return () => {
            destroyed = true;
            cancelAnimationFrame(frame);
            ro.disconnect();
            io.disconnect();
            disposables.forEach((d) => d.dispose());
            renderer.dispose();
        };
    });
</script>

<div class="relative">
    <canvas
        bind:this={canvas}
        class="w-full aspect-square"
        onmouseenter={() => (hovered = true)}
        onmouseleave={() => (hovered = false)}
    ></canvas>
    {#if loading}
        <p class="absolute inset-0 flex items-center justify-center font-subheader text-xs uppercase text-header/60 pointer-events-none">
            Loading model...
        </p>
    {/if}
</div>
