<script lang="ts">
	import '../app.css';
	import favicon from '$lib/assets/favicon.svg';
	import { onNavigate } from '$app/navigation';
	import { injectSpeedInsights } from '@vercel/speed-insights/sveltekit';
	import Cursor from '$lib/components/Cursor.svelte';
	import AmbientShapes from '$lib/components/AmbientShapes.svelte';

	injectSpeedInsights();

	onNavigate((navigation) => {
		if (!document.startViewTransition) return;

		return new Promise((resolve) => {
			document.startViewTransition(async () => {
				resolve();
				await navigation.complete;
			});
		});
	});
	
	let { children } = $props();
</script>

<Cursor/>
<AmbientShapes opacity={0.7}/>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>



{@render children?.()}


