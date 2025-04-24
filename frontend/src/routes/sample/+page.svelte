<svelte:head>
	<title>Debunkr | Backend</title>
	<meta content="Test of backend" />
</svelte:head>

<!-- This page will serve as the landing page for our users -->
<script lang="ts">
	import { callFastAPI } from '$lib/api';

	type response = {
		message: string;
	};

	let msg = '';

	async function fetchFastAPI() {
		try {
			const res = await callFastAPI<response>('/api/hello');
			msg = res.message;
		}
		catch (err) {
			console.error(err);
			alert('Failed to catch message from server');
		}
	}

</script>

<section class="bg-blue-200 rounded-2xl p-3 w-[45rem] h-[10rem]">
	<p>Hello from HOME PAGE!</p>
	<button on:click={fetchFastAPI} class="bg-amber-200 rounded-xl shadow-2xl w-[6rem] h-[2rem]">
		<p>Click Me!</p>
	</button>
	{#if msg}
		<p>{msg}</p>
	{/if}
</section>

<style>

</style>
