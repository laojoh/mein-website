import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { DRACOLoader } from 'three/examples/jsm/loaders/DRACOLoader.js';

let loader: GLTFLoader | null = null;

// One shared loader so every tile reuses the same Draco decoder workers.
export function getGLTFLoader() {
    if (!loader) {
        const draco = new DRACOLoader().setDecoderPath('/draco/');
        loader = new GLTFLoader().setDRACOLoader(draco);
    }
    return loader;
}
