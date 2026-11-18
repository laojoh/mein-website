import { env as priv } from '$env/dynamic/private';
import { env as pub } from '$env/dynamic/public';

// Desmos key: DESMOS_API_KEY or PUBLIC_DESMOS_API_KEY, whichever is set. Read at request
// time on the server, so it works with either name. It still reaches the browser —
// Desmos keys are meant to be public.
export function load() {
	return { desmosKey: priv.DESMOS_API_KEY || pub.PUBLIC_DESMOS_API_KEY || null };
}
