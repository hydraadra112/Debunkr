<script>
	// Your script logic (if needed) goes here
  </script>
  
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
  
<style>
  

  nav a {
	font-family: 'Lufga';
	font-size: 16px;
	color: #3D2C1F;
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
	color: #927659;  /* You can keep the hover effect */
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
	background: linear-gradient(to right, #F8F5EE 58%, rgba(223, 199, 137, 0.48));
	padding: 20px;
	display: flex;
	justify-content: center; /* Centers the content horizontally */
	align-items: flex-start;
}


.footer-content {
	display: flex;
	justify-content: space-between;
	align-items: flex-start;
	width: 100%; /* Stretches the content across the width */
	max-width: 1200px; /* Limit the maximum width for larger screens */
	margin-right: 10rem;
}

.footer-logo {
	width: 50px;
	height: auto;
	margin-top: 6px;
}

.footer-text {
	display: flex;
	flex-direction: column;
	max-width: 50%; /* Adjust width for responsiveness */
}

.footer-title {
	font-family: 'Attena';
	color: #3D2C1F;
	font-size: 40px;
}

.footer-description {
	font-family: 'Lufga', sans-serif;
	font-size: 16px;
	color: #3D2C1F;
	font-weight: 400;
	margin-top: 2rem;
}

.footer-copyright {
	font-family: 'Lufga', sans-serif;
	font-size: 16px;
	color: #3D2C1F;
	margin-top: 8rem;
}

/* Responsive footer navigation */
.footer-nav-container {
	display: flex;
	justify-content: center; /* Center navigation horizontally */
	align-items: flex-start;
	width: 100%;
	gap: 3rem; /* Space between sections */
	margin-top: 5rem;
	margin-left: 14rem;
	
}

.footer-nav { 
	display: flex;
	flex-direction: column; 
	gap: 1rem; 
	align-items: flex-start; 
}
.footer-nav-title {
	font-family: 'Lufga';
	font-size: 18px;
	color: #3D2C1F;
	font-weight: 600;
	margin-bottom: 10px;
}

.footer-link {
	font-family: 'Lufga';
	font-size: 16px;
	color: #3D2C1F;
	text-decoration: none;
	transition: color 0.3s;
}

.footer-link:hover {
	color: #927659;
}

/* Media queries for responsiveness */
@media (max-width: 768px) {
	.footer-content {
		flex-direction: column;
		align-items: center;
		text-align: center; /* Center align text on smaller screens */
	}

	.footer-text {
		max-width: 100%;
		margin-bottom: 2rem;
	}

	.footer-nav-container {
		justify-content: center;
		gap: 1rem;
	}

	.footer-nav {
		align-items: center; /* Center navigation links */
	}
}

@media (max-width: 480px) {
	.footer-title {
		font-size: 32px;
	}

	.footer-description {
		font-size: 14px;
	}

	.footer-link {
		font-size: 14px;
	}
}

nav a {
	font-family: 'Lufga';
	font-size: 16px;
	color: #3D2C1F;
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
	color: #927659;  /* You can keep the hover effect */
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
  