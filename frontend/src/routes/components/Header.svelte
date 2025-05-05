<script>
	// Your script logic (if needed) goes here
</script>

<header
	class="flex w-full items-center justify-between p-4 text-gray-800 shadow-md"
	style="background: linear-gradient(to right, #F8F5EE 58%, rgba(223, 199, 137, 0.48));"
>
	<!-- Logo Section with Image -->
	<div class="text-2xl font-bold text-[#325F89]">
		<img src="/debunkrlogo.png" class="logo" alt="Debunkr Logo" />
	</div>

	<!-- Navigation Links -->
	<nav class="flex gap-8 px-[5%] text-[1rem] font-medium">
		<a href="/" class="nav-link">HOME</a>
		<a href="/analyze" class="nav-link">ANALYZE</a>
		<a href="/about" class="nav-link">ABOUT US</a>
	</nav>
</header>

<style>
	.logo {
		width: 3rem;
		height: auto;
	}

	.nav-link {
		font-family: var(--font-body);
		font-size: 16px;
		color: #3d2c1f;
		position: relative;
		text-decoration: none;
		transition: color 0.3s ease;
	}

	.nav-link:hover {
		color: #927659;
	}

	.nav-link:active {
		color: #927659;
	}

	.nav-link::after {
		content: '';
		position: absolute;
		bottom: 0;
		left: 0;
		width: 0;
		height: 2px;
		background-color: #927659;
		transition: width 0.3s ease;
	}

	.nav-link:hover::after,
	.nav-link:active::after {
		width: 100%;
	}
</style>
