
<!-- This file is for layouting consistencies only. 
	Since we use our header for almost every page,
	It is necessary to put them here
-->

<script>
	import Header from './components/Header.svelte';
	import Footer from './components/Footer.svelte';
	import '../global.css';

	let { children } = $props();
</script>

<div class="app">
	<Header />
	
	<main>
		{@render children()}
	</main>

	<Footer/>
</div>

<style>
	/* Put your styles here */
</style>