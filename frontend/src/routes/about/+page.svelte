<svelte:head>
	<title>Debunkr | About</title>
	<meta content="About this app" />
</svelte:head>

<style>
	p,
	h3 {
		font-family: 'LufgaRegular', sans-serif;
	}

	h2 {
		font-family: 'LufgaBold', sans-serif;
	}

</style>

<section class="relative overflow-hidden">
	<div style="position: absolute; top: 5rem; right: 5rem; width: 45rem; height: auto; z-index: 50;">
		<img class="w-full h-full" src="/sun.svg" alt="Decorative Sun">
	</div>
	<img class="absolute top-[45rem] left-0 translate-y-[-20%] max-w-[25%] z-20" src="/img6.png" alt="Decorative Flower Between 1 & 2">
	<img class="absolute top-[113rem] right-0 translate-y-[-30%] max-w-[25%] z-20" src="/img7.png" alt="Decorative Flower Between 2 & 3">
	<img class="absolute top-[194rem] left-0 -translate-y-1/4 max-w-[25%] z-20" src="/img6.png" alt="Decorative Flower Bottom Left">

	<section class="py-20 px-10 md:px-[10%] bg-[url('/bg1.png')] bg-center bg-top bg-cover bg-no-repeat text-darkBrown flex items-center justify-start h-[55rem]">
		<div class="max-w-[37.5rem] z-10">
			<h2 class="text-5xl mb-1.5 leading-none font-extrabold tracking-[0.9rem]">ABOUT US</h2>
			<p class="text-xl text-lightBrown leading-8 mb-5 tracking-[0.3rem] mr-12">Debunkr helps you detect fake news with the power of AI, promoting a more informed and critical society.</p>
		</div>
	</section>

	<section class="py-20 px-5 md:px-[5%] flex items-center gap-10 bg-white relative overflow-hidden h-[60rem]">
		<div class="max-w-[50rem] absolute left-[10%]">
			<img src="/mission-pic.png" alt="Our Mission Illustration" class="w-full h-auto">
		</div>
		<div class="max-w-[44rem] ml-[40rem]">
			<h2 class="text-5xl text-black mb-12 font-bold leading-[1.2rem] tracking-[0.75rem]">OUR MISSION</h2>
			<p class="text-xl text-black leading-8 tracking-[0.3rem] mr-12">At Debunkr, our mission is to combat the spread of misinformation and promote a more informed, critical-thinking society. We are committed to providing people with the tools they need to verify news articles, claims, and information sources — empowering them to make better decisions and contribute to a safer, more transparent digital world.</p>
		</div>
	</section>

	<section class="py-20 px-5 md:px-[5%] bg-[url('/ab-bg2.png')] bg-center bg-top bg-cover bg-no-repeat items-center overflow-hidden h-[90rem] pt-24">
		<h2 class="text-5xl text-darkBrown mb-32 font-bold text-center tracking-[0.75rem]">OUR VALUES</h2>
		<div class="max-w-[45rem] mx-auto">
			<div class="flex items-center gap-6 mb-0">
				<img class="w-24 h-auto object-contain" src="/transparency.svg" alt="Transparency Icon">
				<div class="flex-1">
					<h3 class="text-xl text-black leading-8 mb-3 tracking-[0.3rem] mr-12 font-bold">Transparency</h3>
					<p class="text-xl text-black leading-8 mb-8 tracking-[0.3rem] mr-12">We believe everyone deserves clear, honest, and open access to the truth.</p>
				</div>
			</div>
			<div class="flex items-center gap-6 mb-0">
				<img class="w-24 h-auto object-contain" src="/accuracy.svg" alt="Accuracy Icon">
				<div class="flex-1">
					<h3 class="text-xl text-black leading-8 mb-3 tracking-[0.3rem] mr-12 font-bold">Accuracy</h3>
					<p class="text-xl text-black leading-8 mb-8 tracking-[0.3rem] mr-12">We are committed to using powerful AI technology to deliver reliable and precise results.</p>
				</div>
			</div>
			<div class="flex items-center gap-6 mb-0">
				<img class="w-24 h-auto object-contain" src="/empowerment.svg" alt="Empowerment Icon">
				<div class="flex-1">
					<h3 class="text-xl text-black leading-8 mb-3 tracking-[0.3rem] mr-12 font-bold">Empowerment</h3>
					<p class="text-xl text-black leading-8 mb-8 tracking-[0.3rem] mr-12">We want to equip individuals with the confidence to question, verify, and make informed decisions.</p>
				</div>
			</div>
			<div class="flex items-center gap-6 mb-0">
				<img class="w-24 h-auto object-contain" src="/responsibility.svg" alt="Responsibility Icon">
				<div class="flex-1">
					<h3 class="text-xl text-black leading-8 mb-3 tracking-[0.3rem] mr-12 font-bold">Responsibility</h3>
					<p class="text-xl text-black leading-8 mb-8 tracking-[0.3rem] mr-12">We recognize our role in helping build a healthier information environment, one fact at a time.</p>
				</div>
			</div>
		</div>
	</section>

	<section class="py-20 px-5 md:px-[5%] bg-white relative overflow-hidden text-center">
		<div class="max-w-[70%] mx-auto mb-8">
			<h2 class="text-5xl text-black mb-5 font-bold tracking-[0.75rem]">MEET THE TEAM</h2>
			<p class="text-xl text-black leading-8 mb-12 tracking-[0.3rem]">A passionate group of innovators, developers, and media advocates working together to bring truth back to the forefront.</p>
		</div>
		<div class="flex flex-wrap justify-center gap-8 max-w-[80rem] mx-auto">
			<div class="flex flex-col items-center text-center">
				<img class="max-w-[30rem] h-auto rounded-lg" src="/falco.png" alt="Cha">
				<h3 class="mt-4 text-xl text-lightBrown leading-8 tracking-[0.3rem]">Chariz Dianne Falco</h3>
				<div class="mt-2 mb-5 text-xl">
					<p class="text-lightBrown text-sm">UI/UX Designer</p>
				</div>
			</div>
			<div class="flex flex-col items-center text-center">
				<img class="max-w-[30rem] h-auto rounded-lg" src="/encanto.png" alt="Mark">
				<h3 class="mt-4 text-xl text-lightBrown leading-8 tracking-[0.3rem]">Mark Andrei Encanto</h3>
				<div class="mt-2 mb-5 text-xl">
					<p class="text-lightBrown text-sm">UI/UX Designer</p>
				</div>
			</div>
		</div>
		<div class="flex flex-wrap justify-center gap-8 max-w-[80rem] mx-auto mt-8">
			<div class="flex flex-col items-center text-center">
				<img class="max-w-[30rem] h-auto rounded-lg" src="/deocampo.png" alt="Che">
				<h3 class="mt-4 text-xl text-lightBrown leading-8 tracking-[0.3rem]">Cherilyn Marie Deocampo</h3>
				<div class="mt-2 mb-5 text-xl">
					<p class="text-lightBrown text-sm">UI/UX Designer</p>
				</div>
			</div>
			<div class="flex flex-col items-center text-center">
				<img class="max-w-[30rem] h-auto rounded-lg" src="/torre.png" alt="Jeph">
				<h3 class="mt-4 text-xl text-lightBrown leading-8 tracking-[0.3rem]">Jephone Israel Jireh Torre</h3>
				<div class="mt-2 mb-5 text-xl">
					<p class="text-lightBrown text-sm">UI/UX Designer</p>
				</div>
			</div>
		</div>
		<div class="flex flex-wrap justify-center gap-8 max-w-[80rem] mx-auto mt-8">
			<div class="flex flex-col items-center text-center">
				<img class="max-w-[30rem] h-auto rounded-lg" src="/carado.png" alt="Manns">
				<h3 class="mt-4 text-xl text-lightBrown leading-8 tracking-[0.3rem]">John Manuel Carado</h3>
				<div class="mt-2 mb-5 text-xl">
					<p class="text-lightBrown text-sm">UI/UX Designer</p>
				</div>
			</div>
		</div>
	</section>
</section>