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
<div class="w-[45svw] h-[80svh] overflow-y-scroll overflow-hidden flex justify-start gap-3 flex-col noScroll">
    {#each posts as post}
        <Postcard {post} />
    {/each}
</div>

<style>
    .noScroll{
      scrollbar-width: 0px;
    }
</style>