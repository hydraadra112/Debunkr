<!-- layout.svelte -->

<script>
	import Header from './components/Header.svelte';
	import '../global.css';
	
	let { children } = $props();
</script>

<div class="app min-h-screen flex flex-col">
	<Header />
	
	<main class="flex-grow">
		{@render children()}
	</main>

	<footer class="footer">
		<div class="footer-content">
			<img src="/debunkrlogo.png" alt="Debunkr Logo" class="footer-logo" />
			<div class="footer-text">
				<span class="footer-title">Debunkr</span>
				<p class="footer-description">
					Debunkr equips you with tools to detect misinformation, promoting informed decision-making and upholding democratic integrity.
				</p>
				<p class="footer-copyright">
					© 2025 Debunkr - All Rights Reserved
				</p>
			</div>
			<div class="footer-nav-container">
				<nav class="footer-nav">
					<p class="footer-nav-title">NAVIGATION</p>
					<a href="/" class="footer-link">Home</a>
					<a href="/analyze" class="footer-link">Analyze</a>
					<a href="/about" class="footer-link">About Us</a>
				</nav>
				<nav class="footer-nav">
					<p class="footer-nav-title">SOCIAL</p>
					<a href="/" class="footer-link">Facebook</a>
					<a href="/analyze" class="footer-link">Instagram</a>
					<a href="/about" class="footer-link">X</a>
				</nav>
				<nav class="footer-nav">
					<p class="footer-nav-title">COMPANY</p>
					<a href="/" class="footer-link">Terms and Condition</a>
					<a href="/analyze" class="footer-link">Privacy Policy</a>
					<a href="/about" class="footer-link">Cookies</a>
				</nav>
			</div>
		</div>
	</footer>
</div>


<style>
		.app {
		min-height: full;
		display: flex;
		flex-direction: column;
	}

	main {
		flex-grow: 1;
	}
</style>
