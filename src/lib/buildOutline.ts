import * as THREE from 'three';

type Disposable = { dispose(): void };

export type OutlineOptions = {
    edgeAngle?: number;
    lineColor?: THREE.ColorRepresentation;
    fillColor?: THREE.ColorRepresentation;
    fill?: boolean;
};

export function buildOutline(
    root: THREE.Object3D,
    { edgeAngle = 30, lineColor = 0x000000, fillColor = 0xffffff, fill = true }: OutlineOptions = {}
): { group: THREE.Group; disposables: Disposable[] } {
    root.updateMatrixWorld(true);

    const meshes: THREE.Mesh[] = [];
    root.traverse((o) => {
        if ((o as THREE.Mesh).isMesh) meshes.push(o as THREE.Mesh);
    });

    // Repeated parts (bearings, sprockets) share one geometry, so edges are only computed once per unique part.
    const edgeCache = new Map<THREE.BufferGeometry, THREE.BufferGeometry>();
    let lineVerts = 0;
    let fillVerts = 0;
    let fillIndices = 0;
    for (const m of meshes) {
        let edges = edgeCache.get(m.geometry);
        if (!edges) {
            edges = new THREE.EdgesGeometry(m.geometry, edgeAngle);
            edgeCache.set(m.geometry, edges);
        }
        const g = m.geometry;
        lineVerts += edges.attributes.position.count;
        fillVerts += g.attributes.position.count;
        fillIndices += g.index ? g.index.count : g.attributes.position.count;
    }

    const v = new THREE.Vector3();
    const group = new THREE.Group();
    const disposables: Disposable[] = [];

    if (fill) {
        const pos = new Float32Array(fillVerts * 3);
        const idx = new Uint32Array(fillIndices);
        let vo = 0;
        let io = 0;
        for (const m of meshes) {
            const g = m.geometry;
            const p = g.attributes.position;
            for (let i = 0; i < p.count; i++) {
                v.fromBufferAttribute(p, i).applyMatrix4(m.matrixWorld);
                pos[(vo + i) * 3] = v.x;
                pos[(vo + i) * 3 + 1] = v.y;
                pos[(vo + i) * 3 + 2] = v.z;
            }
            const count = g.index ? g.index.count : p.count;
            for (let j = 0; j < count; j++) idx[io + j] = vo + (g.index ? g.index.getX(j) : j);
            vo += p.count;
            io += count;
        }

        const geometry = new THREE.BufferGeometry();
        geometry.setAttribute('position', new THREE.BufferAttribute(pos, 3));
        geometry.setIndex(new THREE.BufferAttribute(idx, 1));
        // polygonOffset nudges the fill slightly back so lines on its surface win the depth test.
        const material = new THREE.MeshBasicMaterial({
            color: fillColor,
            side: THREE.DoubleSide,
            polygonOffset: true,
            polygonOffsetFactor: 1,
            polygonOffsetUnits: 1
        });
        group.add(new THREE.Mesh(geometry, material));
        disposables.push(geometry, material);
    }

    const linePos = new Float32Array(lineVerts * 3);
    let lo = 0;
    for (const m of meshes) {
        const p = edgeCache.get(m.geometry)!.attributes.position;
        for (let i = 0; i < p.count; i++, lo += 3) {
            v.fromBufferAttribute(p, i).applyMatrix4(m.matrixWorld);
            linePos[lo] = v.x;
            linePos[lo + 1] = v.y;
            linePos[lo + 2] = v.z;
        }
    }
    const lineGeometry = new THREE.BufferGeometry();
    lineGeometry.setAttribute('position', new THREE.BufferAttribute(linePos, 3));
    const lineMaterial = new THREE.LineBasicMaterial({ color: lineColor });
    group.add(new THREE.LineSegments(lineGeometry, lineMaterial));
    disposables.push(lineGeometry, lineMaterial);

    const originals = new Set<Disposable>();
    for (const m of meshes) {
        originals.add(m.geometry);
        (Array.isArray(m.material) ? m.material : [m.material]).forEach((mat) => originals.add(mat));
    }
    edgeCache.forEach((e) => originals.add(e));
    originals.forEach((d) => d.dispose());

    return { group, disposables };
}
