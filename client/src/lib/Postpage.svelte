<script>
    import Navbar from "./Navbar.svelte";
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
<div class="w-[45svw] h-[100svh] flex justify-center my-60 gap-3 flex-col">
    {#each posts as post}
        <Postcard {post} />
    {/each}
</div>
