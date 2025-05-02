
<!-- This file is for layouting consistencies only. 
	Since we use our header for almost every page,
	It is necessary to put them here
-->

<script>
	import Header from './components/Header.svelte';
	import '../global.css';

	let { children } = $props();
</script>

<div class="app">
	<Header />
	
	<main>
		{@render children()}
	</main>

	<footer>
		<p>Hello from FOOTER!</p>
	</footer>
</div>

<style>
	/* Put your styles here */
</style>