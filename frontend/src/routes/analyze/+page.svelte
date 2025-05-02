<body class="overflow-x-hidden">
	<div class="flex h-[100vh] w-full flex-col items-center justify-center p-8">
		<p class="font-heading my-4 text-[2rem]">Classify News for Accuracy</p>
		<main
			class="border-c3 z-3 col-2 flex h-full w-[80%] rounded-[2rem] border-1 bg-[#8B7358]/5 shadow-xl backdrop-blur-lg"
		>
			<!-- Input Section -->
			<section class="flex w-full flex-col rounded-lg p-6">
				<h1 class="font-heading text-primary mb-4 self-center text-2xl">Input News Article</h1>
				<!-- Textarea for user input -->
				<textarea
					id="user-input"
					placeholder="Type or paste your news article here..."
					class="font-body mb-4 h-full w-full resize-none rounded-lg border border-gray-300 p-4 text-[1rem] text-[#2E231A]/80"
				></textarea>
				<div class="flex w-full items-center justify-between gap-4">
					<!-- Upload Button -->
					<button
						id="upload-btn"
						class="font-heading leading-wide flex cursor-pointer items-center justify-center rounded-full border-[0.1rem] border-[#2E231A] px-2 py-2 text-[1rem] text-[#2E231A] transition hover:bg-[#ffe9d6]"
					>
						<img
							src="/ep_upload-filled.png"
							alt="Upload Icon"
							class="mr-2 inline-block"
							width="20"
							height="20"
						/>
						Upload Document
					</button>

					<!-- Analyze Button -->
					<button
						id="analyze-btn"
						class="font-heading leading-wide cursor-pointer rounded-full bg-[#2E231A] px-6 py-2 text-[1rem] text-[#F8F5EE] transition hover:bg-[#6e543f]"
					>
						Analyze
					</button>
				</div>
			</section>

			<!-- Center Line Section -->
			<section class="font-body h-full w-[0.1rem] bg-[#927659]"></section>

			<!-- Results Section -->
			<section class="flex w-full flex-col rounded-lg px-6 pt-6">
				<h1 class="font-heading mb-4 self-center text-2xl text-[#2E231A]">Analysis Result</h1>
				<div class="h-full space-y-6">
					<div id="results-container">
						<h3 class="font-body my-2 text-xl text-[#2E231A]">The News is Likely</h3>
						<div id="emotions-list" class="flex flex-wrap gap-3">
							<!-- Answers will appear here -->
							<p class="text-[#2E231A]/60 italic">Analysis Description</p>
						</div>
					</div>
					<div id="confidence-container">
						<h3 class="font-body mb-2 text-xl text-[#2E231A]">Confidence Level</h3>
						<div id="confidence-list" class="flex flex-wrap gap-3">
							<!-- Answers will appear here -->
							<p class="text-[#2E231A]/60 italic">Confidence Level Description</p>
						</div>
					</div>
					<div id="response-container">
						<h3 class="font-body mb-2 text-xl text-[#2E231A]">Visualizations</h3>
						<div id="visualizations-response" class="text-gray-600">
							<!-- Response will appear here -->
							<p class="text-[#2E231A]/60 italic">
								the Influential words and the graphs will be shown here
							</p>
						</div>
					</div>
				</div>
				<div class="bottom-0 flex items-center justify-end gap-2 self-end py-6">
					<section class="font-heading">Status:</section>
					<section class="bg-error h-3 w-3 rounded-full"></section>
					<section class="font-body">Likely Fake</section>
					<section class="bg-sucess h-3 w-3 rounded-full"></section>
					<section class="font-body">Likely Real</section>
				</div>
			</section>
		</main>
		<div class="mt-2 ml-[22%] flex w-full justify-start">
			<div class="font-body mt-2 text-[1rem] text-[#2E231A]/60 underline">
				When uploading files, ensure that the file size is 25 megabytes (MB) or less.
			</div>
		</div>
	</div>
</body>
