import type { Question } from '$lib/sat';

// Client-only: the question bank is ~800KB of JSON and progress lives in localStorage.
export const ssr = false;

export async function load({ fetch }) {
	const res = await fetch('/sat/questions.json');
	const questions: Question[] = await res.json();
	return { questions };
}
