<script lang="ts">
    import Search from "./Search.svelte";
    import Topratedcompany from "./Topratedcompany.svelte";
    import CardHeader from "./components/ui/card/card-header.svelte";
    import * as Card from "$lib/components/ui/card";
    import { Button } from "$lib/components/ui/button/index.js";
    import { Textarea } from "$lib/components/ui/textarea/index.js";
    import Mostlikes from "./Mostlikes.svelte";

    let post = {}
    import { Post } from "./store";

    Post.subscribe((e) => {
        post = e;
    });
</script>


<div class="card w-fullrounded-lg ">
    <Card.Root class="border-2 h-[75svh] ">
    <div>
    <CardHeader >
        <h1 class="text-4xl">{post.title}</h1>
    </CardHeader>
    <Card.Content class='text-lg'>
        <p>{post.text}</p>
    </Card.Content>
    </div>
    <Card.Footer class="gap-7 flex flex-col">
        <div class="flex justify-start gap-3">
            <button><img src="./heartunfilled.png" alt="" class="h-[3svh] w-[3.5svw] md:w-[2svw] "></button>
        </div>     
            <div class="grid w-full gap-2">
            <Textarea placeholder="Type your comment here." />
            <Button>Comment</Button>
            </div>
            <div>
            </div>
    </Card.Footer>
</Card.Root>
</div>