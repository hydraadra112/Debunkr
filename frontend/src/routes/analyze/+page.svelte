<script lang="ts">
	import { TextLinkPredict } from '$lib/api';
	import { renderChart } from '$lib/chart';
	import { tick } from 'svelte';

	type input = {
		text: string;
	};

	type response = {
		result: string;
		scores: Record<string, number>;
		prob: number;
	};

	let inputText = '';
	let prediction = '';
	let conf_score = 0;
	let wordScores: Record<string, number> = {};

	export async function TextLinkPrediction() {
		try {
			const payload: input = { text: inputText };
			const res = await TextLinkPredict<response, input>('/api/predict-text-link', payload);

			prediction = res.result;
			wordScores = res.scores;
			conf_score = res.prob;

			await tick();

			renderChart(wordScores);
		} catch (err) {
			console.error(err);
			alert('Failed to get prediction.');
		}
	}
</script>

<div>
	<div class="mt-10 flex h-[110vh] flex-col items-center justify-center overflow-hidden p-8">
		<p class=" font-heading primary-color my-4 text-[2rem]">Classify News for Accuracy</p>
		<div
			class="border-c3 z-3 col-2 flex h-full w-[90%] rounded-[2rem] border-1 bg-[#8B7358]/5 shadow-xl backdrop-blur-lg"
		>
			<!-- Input Section -->
			<section class="flex w-full flex-col rounded-lg p-6">
				<h1 class="font-heading text-primary mb-4 self-center text-2xl">Input News Article</h1>
				<!-- Textarea for user input -->
				<textarea
					bind:value={inputText}
					id="user-input"
					placeholder="Type or paste your news article here..."
					class="font-body primary-color/80 mb-4 h-full w-full resize-none rounded-lg border border-gray-300 p-4 text-[1rem]"
				></textarea>
				<div class="flex w-full items-center justify-between gap-4">
					<!-- Upload Button -->
					<button
						id="upload-btn"
						class="font-heading leading-wide primary-color flex cursor-pointer items-center justify-center rounded-full border-[0.1rem] border-[#2E231A] px-2 py-2 text-[1rem] transition hover:bg-[#ffe9d6]"
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
						on:click={TextLinkPrediction}
						id="analyze-btn"
						class="font-heading leading-wide bg-primary-color cursor-pointer rounded-full px-6 py-2 text-[1rem] text-[#F8F5EE] transition hover:bg-[#6e543f]"
					>
						Analyze
					</button>
				</div>
			</section>

			<!-- Center Line Section -->
			<section class="font-body h-full w-[0.1rem] bg-[#927659]"></section>

			<!-- Results Section -->
			<section class="flex w-full flex-col rounded-lg px-6 pt-6">
				{#if !prediction}
					<h1 class="font-heading primary-color mb-4 self-center text-2xl">Analysis Result</h1>
					<p class="mt-6 flex justify-center text-[#6b7280] italic">
						The analysis results will appear here.
					</p>
				{:else}
					<h1 class="font-heading primary-color mb-4 self-center text-2xl">Analysis Result</h1>

					<div class="h-full space-y-6">
						{#if prediction === "Real News"}
							<div id="results-container">
								<h3 class="font-body my-2 text-xl real-news font-bold">The News is Real News</h3>

								<div id="emotions-list" class="flex flex-wrap gap-3">
								<!-- Answers will appear here -->
								<p class="desc-color italic">This content appears to be factual and credible, based on the model's analysis.</p>
								</div>
							</div>
						{:else if prediction === "Fake News"}
							<div id="results-container">
								<h3 class="font-body my-2 text-xl fake-news font-bold">The News is Fake News</h3>

								<div id="emotions-list" class="flex flex-wrap gap-3">
								<!-- Answers will appear here -->
								<p class="desc-color italic">This content is likely misleading or false, based on the model’s evaluation.</p>
								</div>
							</div>
						{/if}
						
						<div id="confidence-container">
							<h3 class="font-body primary-color mb-2 text-xl font-bold">Confidence Level: {conf_score}%</h3>
						</div>

						<div id="response-container">
							<h3 class="font-body primary-color mb-2 text-xl font-bold">Influential Words</h3>

							<div class="flex gap-4">
								<!-- Word list -->
								<div id="visualizations-response" class="w-1/2 overflow-auto">
									{#if Object.keys(wordScores).length > 0}
										<ul class="list-disc pl-5">
											{#each Object.entries(wordScores) as [word, score]}
												<li class="font-body">
													<strong style="color: {score >= 0 ? '#C84A3D' : '#4D7C5A'}">
														{word}
													</strong>
												</li>
											{/each}
										</ul>
									{:else}
										<p class="desc-color italic">
											The influential words and the graph will be shown here.
										</p>
									{/if}
								</div>

								<!-- wordchart -->
								<div class="w-1/2">
									<canvas id="wordChart" width="400" height="300"></canvas>
								</div>
							</div>
						</div>
					</div>

					<div class="bottom-0 flex items-center justify-end gap-2 self-end py-6">
						<section class="font-heading">Status:</section>
						<section class="h-3 w-3 rounded-full bg-[#C84A3D]"></section>
						<section class="font-body">Likely Fake</section>
						<section class="h-3 w-3 rounded-full bg-[#4D7C5A]"></section>
						<section class="font-body">Likely Real</section>
					</div>
				{/if}
			</section>
		</div>
		<div class="mt-2 ml-[22%] flex w-full justify-start">
			<div class="font-body mt-2 text-[1rem] text-[#2E231A]/60 underline">
				When uploading files, ensure that the file size is 25 megabytes (MB) or less.
			</div>
		</div>
	</div>
</div>

<style>
	.primary-color {
		color: var(--primary);
	}

	.desc-color {
		color: #6b7280;
	}

	.bg-primary-color {
		background-color: var(--primary);
	}
	.real-news {
    color: #4D7C5A;
  }

  .fake-news {
    color: #C84A3D;
  }

</style>
