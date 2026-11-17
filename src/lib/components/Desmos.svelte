<script lang="ts">
	// Desmos graphing calculator (the same embed the Bluebook SAT app uses).
	// Needs an API key: set PUBLIC_DESMOS_API_KEY in .env. Falls back to Desmos's public
	// demo key, which is meant for development only — request a free key at desmos.com/api.
	import { onMount } from 'svelte';
	import { env } from '$env/dynamic/public';

	const DEMO_KEY = 'dcb31709b452b1cf9dc26972add0fda6';
	const API = 'https://www.desmos.com/api/v1.11/calculator.js';

	/** Changing this saves the current graph and swaps to the graph for the new key. */
	let { stateKey }: { stateKey: string } = $props();

	let el: HTMLDivElement;
	let calc: any = $state.raw();
	let failed = $state(false);
	const saved = new Map<string, unknown>();
	let activeKey: string | null = null;

	function loadScript(): Promise<void> {
		const w = window as any;
		if (w.Desmos) return Promise.resolve();
		w.__desmosLoading ??= new Promise<void>((resolve, reject) => {
			const s = document.createElement('script');
			s.src = `${API}?apiKey=${env.PUBLIC_DESMOS_API_KEY || DEMO_KEY}`;
			s.async = true;
			s.onload = () => resolve();
			s.onerror = () => reject(new Error('Desmos failed to load'));
			document.head.appendChild(s);
		});
		return w.__desmosLoading;
	}

	onMount(() => {
		let destroyed = false;
		loadScript()
			.then(() => {
				if (destroyed) return;
				calc = (window as any).Desmos.GraphingCalculator(el, {
					keypad: true,
					expressions: true,
					settingsMenu: true,
					zoomButtons: true,
					expressionsTopbar: true,
					border: false,
					autosize: true
				});
			})
			.catch(() => (failed = true));
		return () => {
			destroyed = true;
			calc?.destroy();
		};
	});

	// per-question graphs: stash the old one, restore (or blank) the new one
	$effect(() => {
		const key = stateKey;
		if (!calc || key === activeKey) return;
		if (activeKey) saved.set(activeKey, calc.getState());
		const next = saved.get(key);
		next ? calc.setState(next) : calc.setBlank();
		activeKey = key;
	});

	export function clear() {
		calc?.setBlank();
	}
</script>

<div class="relative w-full h-full" data-calc>
	<div bind:this={el} class="w-full h-full"></div>
	{#if failed}
		<div class="absolute inset-0 grid place-items-center p-6 text-center text-sm bg-bg">
			<p>Couldn’t load the Desmos calculator. Check your connection or open
				<a class="underline" href="https://www.desmos.com/calculator" target="_blank" rel="noreferrer">desmos.com/calculator</a>.
			</p>
		</div>
	{:else if !calc}
		<div class="absolute inset-0 grid place-items-center text-xs font-subheader uppercase opacity-50">Loading calculator…</div>
	{/if}
</div>
