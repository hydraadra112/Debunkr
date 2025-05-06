// src/lib/api.ts

const BASE_URL = "http://localhost:8000";

/**
 * Calls a FastAPI endpoint and parses the JSON response.
 * @template T
 * @param {string} path - The relative API path (e.g., "/api/hello")
 * @returns {Promise<T>}
 */

export async function callFastAPI<T>(path: string): Promise<T> {
	const res = await fetch(`${BASE_URL}${path}`);
	if (!res.ok) throw new Error(`Error ${res.status}: ${res.statusText}`);
	return res.json();
}

export async function TextLinkPredict<T, U>(path: string, data: U): Promise<T> {
	const res = await fetch(`${BASE_URL}${path}`, {
		method: "POST",
		headers: {
			"Content-Type": "application/json"
		},
		body: JSON.stringify(data)
	});
	if (!res.ok) throw new Error(`Error ${res.status}: ${res.statusText}`);
	return res.json();
}
