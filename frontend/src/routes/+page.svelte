<!-- Debunkr Landing Page -->
<svelte:head>
	<title>Debunkr</title>
	<meta content="Debunkr Application" />
</svelte:head>

<style>
/* Global Fonts */
body, p, a, h2, h3, h4, h5, h6 {
	font-family: 'Lufga', sans-serif;
}
h1 {
	font-family: 'Attena', cursive;
}

/* Hero Section */
.hero-section {
	display: flex;
	align-items: center;
	height: 100vh;
	background: url('/bg1.png') center/cover no-repeat;
	position: relative;
	padding: 0 5%;
}
.hero-left {
	max-width: 500px;
	color: #3D2C1F;
	z-index: 1;
	margin-left: 5%;
	flex: 1;
}
.hero-left h1 {
	font-size: 7rem;
	margin: 0;
	line-height: 1;
}
.hero-left h2 {
	font-size: 2rem;
	margin-bottom: 0.5rem;
}
.hero-left p {
	font-size: 1rem;
	color: #927659;
	margin: 0;
	line-height: 1.5;
}
.hero-img {
	position: absolute;
	right: 3%;
	top: 50%;
	transform: translateY(-70%);
	max-width: 40%;
	max-height: 50vh;
	z-index: 0;
}
.btn {
	display: inline-block;
	margin-top: 1.5rem;
	background-color: #DFC789;
	color: #3D2C1F;
	font-size: 1rem;
	border: 1px solid #3D2C1F;
	padding: 0.5rem 2.5rem;
	border-radius: 8px;
	cursor: pointer;
	text-decoration: none;
	transition: background-color 0.3s ease;
}
.btn:hover {
	background-color: #C5A262;
	font-weight: 500;
}

/* Decorative Flowers */
.flower, .flower2, .flower3 {
	position: absolute;
	max-width: 100%;
	max-height: 55vh;
}
.flower { top: 70vh; }
.flower2 { top: 150vh; right: 0; }
.flower3 { top: 237vh; }

/* Features Section */
.second-section {
	display: flex;
	flex-wrap: wrap;
	gap: 20px;
	justify-content: flex-start;
	padding: 40px;
	margin: 100px 0;
}
.row {
	display: flex;
	align-items: center;
	background-color: #F8F5EE;
	padding: 30px 20px;
	border: 1px solid #ccc;
	border-radius: 8px;
	width: calc(33.333% - 20px);
	box-sizing: border-box;
}
.image-container {
	margin-right: 20px;
	max-width: 150px;
}
.image-container img {
	width: 100%;
	border-radius: 8px;
}
.text-container .title {
	font-size: 1rem;
	font-weight: bold;
	margin-bottom: 10px;
}
.text-container .text {
	font-size: 0.85rem;
	color: #3D2C1F;
}

/* How It Works Section */
.third-section {
	padding: 60px 5%;
	text-align: center;
	background: url('/bg1.png') center/cover no-repeat;
}
.third-section h2 {
	font-size: 3rem;
	color: #2E231A;
	margin-bottom: 40px;
	font-weight: bold;
}
.third-container {
	display: flex;
	justify-content: center;
	align-items: flex-start;
	gap: 40px;
	flex-wrap: wrap;
	max-width: 1200px;
	margin: 0 auto;
	text-align: left;
	transform: translateX(60px);
}
.third-image img {
	max-width: 300px;
	width: 100%;
	object-fit: contain;
}
.third-steps {
	flex: 1;
	min-width: 300px;
	max-width: 500px;
	color: #927659;
	font-size: 1rem;
	line-height: 1.6;
}
.step {
	margin-bottom: 20px;
}
.step h3 {
	font-weight: 800;
	font-size: 1rem;
	margin-bottom: 5px;
	color: #927659;
}
.step p strong {
	font-weight: 600;
	color: #927659;
}

/* Final Call To Action */
.last-section {
	padding: 100px 5%;
	text-align: center;
	display: flex;
	flex-direction: column;
	align-items: center;
}
.last-section-content {
	max-width: 700px;
	padding: 40px 0;
}
.last-section-content h2 {
	font-size: 3rem;
	color: #2E231A;
	margin-bottom: 16px;
	font-weight: bold;
}
.last-section-content p {
	font-size: 1rem;
	color: #3D2C1F;
	line-height: 1.6;
	margin-bottom: 0;
}

/* Responsive Design */
@media (max-width: 768px) {
	.hero-section {
		flex-direction: column;
		height: auto;
		padding: 0 20px;
	}
	.hero-left {
		max-width: 100%;
		margin-left: 0;
		text-align: center;
	}
	.hero-left h1 { font-size: 4rem; margin-top: 100px; }
	.hero-left h2 { font-size: 1.5rem; }
	.hero-left p { font-size: 0.9rem; }
	.hero-img { display: none !important; }
	.btn { margin-bottom: 100px; }

	.second-section {
		flex-direction: column;
		padding: 20px;
	}
	.row {
		width: 100%;
		margin-bottom: 20px;
	}

	.third-section {
		padding: 60px 20px;
	}
	.third-section h2 {
		font-size: 2.5rem;
	}
	.third-container {
		flex-direction: column;
		text-align: center;
		transform: none;
	}
	.third-steps {
		max-width: 100%;
		padding: 10px 20px;
	}
	.third-image {
		display: flex;
		justify-content: center;
		margin-left: 30px;
	}
	.third-image img {
		max-width: 50%;
		margin-bottom: 20px;
	}
	.step h3 {
		font-size: 1.2rem;
	}
	.flower, .flower2, .flower3 {
		display: none !important;
	}
}
</style>

<!-- HERO SECTION -->
<section class="hero-section">
	<div class="hero-left">
		<h1>Debunkr</h1>
		<h2>Verify before you believe.</h2>
		<p>In an age where information spreads rapidly, it’s easy to fall for fake news.
		Debunkr helps you quickly determine if a news article or Facebook post—especially those in Tagalog/Taglish—might be fake or unreliable.</p>
		<a href="#" class="btn">GET STARTED</a>
	</div>
	<img class="hero-img" src="/img1.png" alt="Star Illustration">
</section>

<img class="flower" src="/img6.png" alt="flower">

<!-- FEATURES SECTION -->
<section class="second-section">
	<div class="row">
		<div class="image-container">
			<img src="/img2.png" alt="Fast and Accurate" />
		</div>
		<div class="text-container">
			<div class="title">FAST AND ACCURATE</div>
			<div class="text">Get reliable results in no time, ensuring you can make quick decisions on the information you come across.</div>
		</div>
	</div>

	<div class="row">
		<div class="image-container">
			<img src="/img3.png" alt="User Friendly" />
		</div>
		<div class="text-container">
			<div class="title">USER FRIENDLY</div>
			<div class="text">Our simple, clean interface makes the analysis process easy for everyone, from casual users to experts.</div>
		</div>
	</div>

	<div class="row">
		<div class="image-container">
			<img src="/img4.png" alt="Trusted Tool" />
		</div>
		<div class="text-container">
			<div class="title">TRUSTED TOOL</div>
			<div class="text">Trusted by many, Debunkr is your go-to platform for identifying and verifying misinformation.</div>
		</div>
	</div>
</section>

<img class="flower2" src="/img7.png" alt="flower">

<!-- HOW IT WORKS SECTION -->
<section class="third-section">
	<h2>HOW DOES IT WORK?</h2>
	<div class="third-container">
		<div class="third-image">
			<img src="/img5.png" alt="How it works graphic">
		</div>
		<div class="third-steps">
			<div class="step">
				<h3>Submit Content</h3>
				<p><strong>Upload files, paste links,</strong> or enter text for analysis.</p>
			</div>
			<div class="step">
				<h3>Content Processing</h3>
				<p>The app <strong>analyzes and prepares</strong> the content for accurate evaluation.</p>
			</div>
			<div class="step">
				<h3>Fake News Detection</h3>
				<p>The AI <strong>determines the authenticity</strong> of the content.</p>
			</div>
			<div class="step">
				<h3>View Results</h3>
				<p>See clear, <strong>visual results</strong> showing influence and credibility markers.</p>
			</div>
			<div class="step">
				<h3>Easy to Use</h3>
				<p>The app is <strong>responsive and intuitive</strong>, ensuring seamless interaction.</p>
			</div>
		</div>
	</div>
</section>

<img class="flower3" src="/img6.png" alt="flower">

<!-- FINAL CTA -->
<section class="last-section">
	<div class="last-section-content">
		<h2>START ANALYZING NOW!</h2>
		<p>Ready to get started? Simply upload your content or paste a link to begin the verification process.</p>
		<a href="#" class="btn">START ANALYZING</a>
	</div>
</section>
