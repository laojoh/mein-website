<script>
    import { TypeWriter } from "svelte-typewrite";
    let {text}=$props();
</script>

<TypeWriter texts={[text]} repeat={1} typeSpeed={80} endState={{text: "typed", caret: "hidden"}} blinkDuration={1000}/>