<script>
	// Your script logic (if needed) goes here
</script>


<footer class="footer font-body">
	<div class="flex justify-between items-start w-full max-w-[1200px] mr-40">
		<img src="/debunkrlogo.png" alt="Debunkr Logo" class="size-[3rem] mt-[6px]" />
		<div class="footer-text">
			<span class="font-title text-[3rem] text-[#3d2c1f]">Debunkr</span>
			<p class="font-sans text-base text-[#3d2c1f] font-body mt-8">
				Debunkr equips you with tools to detect misinformation, promoting informed decision-making
				and upholding democratic integrity.
			</p>
			<p class="font-body text-[1rem] mt-[8rem]">© 2025 Debunkr - All Rights Reserved</p>
		</div>
		<div class="flex justify-center items-start w-full gap-12 mt-20 ml-56">
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

<style>
	nav a {
		font-family: 'Lufga';
		font-size: 16px;
		color: #3d2c1f;
		text-decoration: none;
		transition: color 0.3s ease;
		position: relative;
		margin-right: 5rem;
	}

	nav a:hover {
		color: #927659;
	}

	/* Line appears on hover and is persistent on click (active) */
	nav a:active {
		color: #927659; /* You can keep the hover effect */
	}

	nav a:after {
		content: '';
		position: absolute;
		bottom: 0;
		left: 0;
		width: 0;
		height: 2px;
		background-color: #927659;
		transition: width 0.3s ease;
	}

	nav a:hover:after,
	nav a:active:after {
		width: 100%;
	}

	/* Ensure the footer takes up the full width and adjusts content to align */
	footer {
		width: 100%;
		background: linear-gradient(to right, #f8f5ee 58%, rgba(223, 199, 137, 0.48));
		padding: 20px;
		display: flex;
		justify-content: center; /* Centers the content horizontally */
		align-items: flex-start;
	}

	.footer-text {
		display: flex;
		flex-direction: column;
		max-width: 50%; /* Adjust width for responsiveness */
	}

	.footer-nav {
		display: flex;
		flex-direction: column;
		gap: 1rem;
		align-items: flex-start;
	}
	.footer-nav-title {
		font-family: var(--font-body);
		font-size: 18px;
		color: #3d2c1f;
		font-weight: 600;
		margin-bottom: 10px;
	}

	.footer-link {
		font-family: var(--font-body);
		font-size: 16px;
		color: #3d2c1f;
		text-decoration: none;
		transition: color 0.3s;
	}

	.footer-link:hover {
		color: #927659;
	}

	/* Media queries for responsiveness */
	@media (max-width: 768px) {
		.footer-text {
			max-width: 100%;
			margin-bottom: 2rem;
		}

		.footer-nav {
			align-items: center; /* Center navigation links */
		}
	}

	@media (max-width: 480px) {

		.footer-link {
			font-size: 14px;
		}
	}

	nav a {
		font-family: 'Lufga';
		font-size: 16px;
		color: #3d2c1f;
		text-decoration: none;
		transition: color 0.3s ease;
		position: relative;
		margin-right: 5rem;
	}

	nav a:hover {
		color: #927659;
	}

	/* Line appears on hover and is persistent on click (active) */
	nav a:active {
		color: #927659; /* You can keep the hover effect */
	}

	nav a:after {
		content: '';
		position: absolute;
		bottom: 0;
		left: 0;
		width: 0;
		height: 2px;
		background-color: #927659;
		transition: width 0.3s ease;
	}

	nav a:hover:after,
	nav a:active:after {
		width: 100%;
	}
</style>
