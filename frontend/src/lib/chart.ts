import Chart from 'chart.js/auto';
import { onMount } from 'svelte';

let chart: Chart | null = null;

	export function renderChart(scores: Record<string, number>) {
		const labels: string[] = [];
		const data: number[] = [];
		const backgroundColors: string[] = [];

		for (const [word, score] of Object.entries(scores)) {
			labels.push(word);
			data.push(score);
			backgroundColors.push(score > 0 ? '#C84A3D' : '#4D7C5A'); // Red = Fake, Green = Real
		}

		if (chart) {
			chart.destroy();
		}

		chart = new Chart(document.getElementById('wordChart') as HTMLCanvasElement, {
			type: 'bar',
			data: {
				labels: labels,
				datasets: [
					{
						label: 'Word Influence Score',
						data: data,
						backgroundColor: backgroundColors,
						borderRadius: 5
					}
				]
			},
			options: {
				indexAxis: 'y',
				scales: {
					x: {
						beginAtZero: true,
						grid: {
							color: '#e2e8f0'
						},
						ticks: {
							callback: function (tickValue: string | number) {
								const num = typeof tickValue === 'string' ? parseFloat(tickValue) : tickValue;
								return Math.abs(num).toFixed(2);
							}
						}
					},
					y: {
						grid: {
							color: '#e2e8f0'
						}
					}
				},
				plugins: {
					legend: { display: false },
					tooltip: {
						callbacks: {
							label: function (context: any) {
								const label = context.dataset.label || '';
								const value = context.parsed.x;
								return `${label}: ${Math.abs(value).toFixed(2)}`;
							}
						}
					}
				}
			}
		});
	}