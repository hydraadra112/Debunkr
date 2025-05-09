<svelte:head>
  <title>Debunkr | About</title>
  <meta content="About this app" />
</svelte:head>

<style>
  /* Define a base font size for rem units */
  :root {
    font-size: 16px; /* Default browser font size */
  }

/* Global Fonts */
body,
	p,
	a,
	h3,
	h4,
	h5,
	h6 {
		font-family: 'LufgaRegular', sans-serif;
	}

  h2{
    font-family: 'LufgaBold', sans-serif;
  }

h1 {
    font-family: 'Attena', cursive;
}



  /* About Us Section Styling */
  .about-hero {
    padding: 5rem 10%; 
    background: url('/ab-bg1.png') center top/cover no-repeat; /* Assuming a specific background for the top */
    color: #3D2C1F; /* Dark brown text color */
    display: flex;
    align-items: center;
    justify-content: flex-start;
    position: relative;
    overflow: hidden; /* To contain the flower and sun */
    height: 55rem;
  }

  .about-text {
    max-width: 37.5rem;
    z-index: 1;
  }

  .about-text h2 {
    font-size: 5rem;
    margin-bottom: 0.625rem;
    line-height: 1;
    font-weight: 1000;
    letter-spacing: .9rem;
    }

  .about-text p {
    font-size: 1.5rem;
    color: #927659;
    line-height: 2rem;
    margin-bottom: 1.25rem;
	letter-spacing: .3rem;
	margin-right: 5rem;
  }

  .sun-about-top-right {
    position: absolute;
    left: 45rem; 
    top: 4rem; 
    max-width: 50rem;
    opacity: 1;
    z-index: 0;
  }

  .flower-about-top-left {
    position: absolute;
    left: 0; 
    top: 55rem;
    transform: translateY(-50%);
    max-width: 30%;
	z-index: 2;
  }


  /*MISSION*/
  .our-mission-section {
    padding: 5rem 5%;
    display: flex;
    align-items: center;
    gap: 2.5rem;
    background-color: #FFFFFF;
    position: relative;
    overflow: hidden;
	height: 60rem;
  }

  .mission-text {
    max-width: 44rem;
    margin-left: 40rem;
  }

  .mission-text h2 {
    font-size: 5rem;
    color: #000000;
    margin-bottom: 3rem;
    font-weight: bold;
    line-height: 1.2rem;
    letter-spacing: .75rem;
  }

  .mission-text p {
    font-size: 1.5rem;
    color: #000000;
    line-height: 2rem;
	letter-spacing: .3rem;
	margin-right: 5rem;
  }

  .mission-image {
    max-width: 50rem;
    position: absolute;
    left: 10%;
  }

  .mission-image img {
    width: 100%;
    height: auto;
  }

  .flower-about-top-right {
    position: absolute;
    right: 0%;
    top: 107rem;
    max-width: 40%;
    z-index: 2;
  }


  /*OUR VISION*/

  .our-values-section {
    padding: 5rem 5%;
    background: url('/ab-bg2.png') center top/cover no-repeat;
    align-items: center;
    overflow: hidden;
    height: 90rem;
    padding-top: 10rem;
  }

  .our-values-section h2 {
    font-size: 5rem;
    color: #2E231A;
    margin-bottom: 8rem;
    font-weight: bold;
    text-align: center;
    letter-spacing: .75rem;
  }

  .value-item {
    display: flex;
    align-items: center;
    gap: 1.5rem;
    max-width: 45rem;
    margin: 0 auto; 
  }

  .value-icon {
    width: 10rem;
    height: auto;
    object-fit: contain;
  }

  .value-text {
    flex: 1;
  }

  .value-text h3 {
    font-size: 1.5rem;
    color: #000000;
    line-height: 2rem;
    margin-bottom: 1.25rem;
	letter-spacing: .3rem;
	margin-right: 5rem;
  font-weight: bold;
  }

  .value-text p {
    font-size: 1.5rem;
    color: #000000;
    line-height: 2rem;
    margin-bottom: 3rem;
	letter-spacing: .3rem;
	margin-right: 5rem;
  }

  .flower-about-bottom-right {
    position: absolute;
    left: 0;
    top: 205rem;
    transform: translateY(-50%);
    max-width: 30%;
	z-index: 2;
  }




/*MEET THE TEAM*/

.meet-the-team {
  padding: 5rem 5%;
  background-color: #FFFFFF;
  position: relative;
  overflow: hidden;
  text-align: center;
}

.team-text {
  max-width: 70%;
  text-align: center;
  margin-bottom: 2rem;
  margin-left: auto;
  margin-right: auto;
}

.meet-the-team h2 {
  font-size: 5rem;
  color: rgb(0, 0, 0);
  margin-bottom: 2rem;
  font-weight: bold;
  letter-spacing: .75rem;
}

.meet-the-team p {
    font-size: 1.5rem;
    color: #000000;
    line-height: 2rem;
    margin-bottom: 3rem;
    letter-spacing: .3rem;
    margin-right: 0
}

.team-content {
  display: flex; 
  flex-wrap: wrap; 
  justify-content: center;
  gap: 2rem;
  max-width: 80rem;
  margin: 0 auto;
}

.team-member {
  display: flex;
  flex-direction: column;
  align-items: center; 
  text-align: center; 
}

.team-member.solo {
  width: 100%; 
}

.member-name {
  margin-top: 1rem;
  font-size: 1.2rem;
}

.member-role {
  margin-bottom: 2rem;
  font-size: 1.2rem;
}

.member-role p {
  color: #927659;
  font-size: 1rem;
}

.team-member h3 {
  color: #927659;
  font-size: 1.5rem;
    line-height: 2rem;
	letter-spacing: .3rem;
}

.pic1 {
  max-width: 30rem;
  height: auto;
  border-radius: 1rem;
}

.pic2 {
  max-width: 30rem; 
  height: auto;
  border-radius: 1rem;
}

</style>

<section>
	<img class="flower-about-top-left" src="/img6.png" alt="Decorative Flower">
  <img class="flower-about-top-right" src="/img7.png" alt="Decorative Flower">
  <img class="flower-about-bottom-right" src="/img6.png" alt="Decorative Flower">

<section class="about-hero">
  <div class="about-text">
    <h2>ABOUT US</h2>
    <p>Debunkr helps you detect fake news with the power of AI, promoting a more informed and critical society.</p>
  </div>
  <img class="sun-about-top-right" src="/sun.png" alt="Decorative Sun">
</section>

<section class="our-mission-section">
  
  <div class="mission-image">
    <img src="/mission-pic.png" alt="Our Mission Illustration">
  </div>
  <div class="mission-text">
    <h2>OUR MISSION</h2>
    <p>At Debunkr, our mission is to combat the spread of misinformation and promote a more informed, critical-thinking society. We are committed to providing people with the tools they need to verify news articles, claims, and information sources — empowering them to make better decisions and contribute to a safer, more transparent digital world.</p>
  </div>
</section>

<section class="our-values-section">
  <h2>OUR VALUES</h2>
  <div class="value-item">
    <img class="value-icon" src="/transparency.png" alt="Transparency Icon">
    <div class="value-text">
      <h3>Transparency</h3>
      <p>We believe everyone deserves clear, honest, and open access to the truth.</p>
    </div>
  </div>
  <div class="value-item">
    <img class="value-icon" src="/accuracy.png" alt="Accuracy Icon">
    <div class="value-text">
      <h3>Accuracy</h3>
      <p>We are committed to using powerful AI technology to deliver reliable and precise results.</p>
    </div>
  </div>
  <div class="value-item">
    <img class="value-icon" src="/empowerment.png" alt="Empowerment Icon">
    <div class="value-text">
      <h3>Empowerment</h3>
      <p>We want to equip individuals with the confidence to question, verify, and make informed decisions.</p>
    </div>
  </div>
  <div class="value-item">
    <img class="value-icon" src="/responsibility.png" alt="Responsibility Icon">
    <div class="value-text">
      <h3>Responsibility</h3>
      <p>We recognize our role in helping build a healthier information environment, one fact at a time.</p>
    </div>
  </div>
</section>

<section class="meet-the-team">
  <div class="team-text">
    <h2>MEET THE TEAM</h2>
    <p>A passionate group of innovators, developers, and media advocates working together to bring truth back to the forefront.</p>
  </div>
  <div class="team-content">
    <div class="team-member">
      <img class="pic1" src="/falco.png" alt="Cha">
      <h3 class="member-name">Chariz Dianne Falco</h3>
      <div class="member-role">
        <p>UI/UX Designer</p>
      </div>
    </div>
    <div class="team-member">
      <img class="pic1" src="/encanto.png" alt="Mark">
      <h3 class="member-name">Mark Andrei Encanto</h3>
      <div class="member-role">
        <p>UI/UX Designer</p>
      </div>
    </div>
    </div>
    <div class="team-content">
      <div class="team-member">
        <img class="pic1" src="/deocampo.png" alt="Che">
        <h3 class="member-name">Cherilyn Marie Deocampo</h3>
        <div class="member-role">
          <p>UI/UX Designer</p>
        </div>
      </div>
      <div class="team-member">
        <img class="pic1" src="/torre.png" alt="Jeph">
        <h3 class="member-name">Jephone Israel Jireh Torre</h3>
        <div class="member-role">
          <p>UI/UX Designer</p>
        </div>
      </div>
      </div>
      <div class="team-content">
        <div class="team-member">
          <img class="pic1" src="/carado.png" alt="Manns">
          <h3 class="member-name">John Manuel Carado</h3>
          <div class="member-role">
            <p>UI/UX Designer</p>
          </div>
        </div>
      </div>
</section>
</section>