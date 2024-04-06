<script>
    import Postcard from "./Postcard.svelte";

    let posts = [];

    async function fetchPosts() {
        try {
            const response = await fetch('/posts');
            posts = await response.json();
        } catch (error) {
            console.error('Error fetching posts:', error);
        }
    }

    fetchPosts();
</script>

<!-- <Navbar /> -->
<div class="w-[45svw] h-[80svh] overflow-y-scroll overflow-hidden flex justify-start gap-3 flex-col">
    {#each posts as post}
        <Postcard {post} />
        <Postcard {post} />
    {/each}
</div>
