<script>
    import Postcard from "./Postcard.svelte";
    import { Post,state } from "./store";
    let posts = [];

    async function fetchPosts() {
        try {
            const response = await fetch('/posts');
            posts = await response.json();
        } catch (error) {
            console.error('Error fetching posts:', error);
        }
    }

    function Inpost(p){
        Post.set(p);
        state.set("seepost");
    }

    fetchPosts();
</script>

<!-- <Navbar /> -->
<div class=" w-[70svw] md:w-[45svw]  h-[80svh] overflow-y-scroll overflow-hidden flex justify-start gap-3 flex-col noScroll">
    {#each posts as post}
    <div on:click={()=>{Inpost(post)}} class="contents">
        <Postcard  {post} />
    </div>
    {/each}
</div>

<style>
    .noScroll{
      scrollbar-width: 0px;
    }
</style>