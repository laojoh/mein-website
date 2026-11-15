import * as THREE from 'three';

type Disposable = { dispose(): void };

// Collapses thousands of per-face meshes into one mesh per color so the GPU
// only issues ~one draw call per color instead of one per primitive.
export function mergeByMaterial(root: THREE.Object3D): { group: THREE.Group; disposables: Disposable[] } {
    root.updateMatrixWorld(true);

    const buckets = new Map<string, THREE.Mesh[]>();
    const originals = new Set<Disposable>();

    root.traverse((o) => {
        const mesh = o as THREE.Mesh;
        if (!mesh.isMesh) return;
        const mat = (Array.isArray(mesh.material) ? mesh.material[0] : mesh.material) as THREE.MeshStandardMaterial;
        const key = mat.color ? mat.color.getHexString() : 'cccccc';
        if (!buckets.has(key)) buckets.set(key, []);
        buckets.get(key)!.push(mesh);
        originals.add(mesh.geometry);
        (Array.isArray(mesh.material) ? mesh.material : [mesh.material]).forEach((m) => originals.add(m));
    });

    const group = new THREE.Group();
    const disposables: Disposable[] = [];
    const v = new THREE.Vector3();
    const nm = new THREE.Matrix3();

    for (const [hex, meshes] of buckets) {
        let vCount = 0;
        let iCount = 0;
        for (const m of meshes) {
            const g = m.geometry;
            vCount += g.attributes.position.count;
            iCount += g.index ? g.index.count : g.attributes.position.count;
        }

        const pos = new Float32Array(vCount * 3);
        const nor = new Float32Array(vCount * 3);
        const idx = new Uint32Array(iCount);
        let vo = 0;
        let io = 0;

        for (const m of meshes) {
            const g = m.geometry;
            if (!g.attributes.normal) g.computeVertexNormals();
            const p = g.attributes.position;
            const n = g.attributes.normal;
            nm.getNormalMatrix(m.matrixWorld);

            for (let i = 0; i < p.count; i++) {
                v.fromBufferAttribute(p, i).applyMatrix4(m.matrixWorld);
                pos[(vo + i) * 3] = v.x;
                pos[(vo + i) * 3 + 1] = v.y;
                pos[(vo + i) * 3 + 2] = v.z;
                v.fromBufferAttribute(n, i).applyMatrix3(nm).normalize();
                nor[(vo + i) * 3] = v.x;
                nor[(vo + i) * 3 + 1] = v.y;
                nor[(vo + i) * 3 + 2] = v.z;
            }

            const count = g.index ? g.index.count : p.count;
            const mirrored = m.matrixWorld.determinant() < 0;
            for (let j = 0; j < count; j += 3) {
                const a = g.index ? g.index.getX(j) : j;
                const b = g.index ? g.index.getX(j + 1) : j + 1;
                const c = g.index ? g.index.getX(j + 2) : j + 2;
                idx[io + j] = vo + a;
                idx[io + j + 1] = vo + (mirrored ? c : b);
                idx[io + j + 2] = vo + (mirrored ? b : c);
            }

            vo += p.count;
            io += count;
        }

        const geometry = new THREE.BufferGeometry();
        geometry.setAttribute('position', new THREE.BufferAttribute(pos, 3));
        geometry.setAttribute('normal', new THREE.BufferAttribute(nor, 3));
        geometry.setIndex(new THREE.BufferAttribute(idx, 1));

        const material = new THREE.MeshStandardMaterial({
            color: parseInt(hex, 16),
            roughness: 0.55,
            metalness: 0.15,
            side: THREE.DoubleSide
        });

        group.add(new THREE.Mesh(geometry, material));
        disposables.push(geometry, material);
    }

    originals.forEach((d) => d.dispose());
    return { group, disposables };
}
