<script lang="ts">
    import * as Card from "$lib/components/ui/card";
    import { Badge } from "$lib/components/ui/badge";
    import { Heart } from "svelte-radix";
    export let post: any;

</script>
   
<Card.Root class="border-2">
<Card.Header>
    <div class="flex flex-row justify-between">
        <Card.Title class="text-2xl">{post.title}</Card.Title>
        <div class="flex flex-row items-center gap-3">
            <!-- <Heart on:click={} /> -->
            <Badge class="text-lg">{post.organisation}</Badge>
        </div>
    </div>
    <Card.Description>{new Date(post.time).toDateString()}</Card.Description>
</Card.Header>
<Card.Content class='text-lg'>
    <p>{post.text}</p>
</Card.Content>
<Card.Footer class="gap-4">
    {#each post.tags as tag}
        <Badge variant="secondary" class="text-sm">{tag}</Badge>
    {/each}
</Card.Footer>
</Card.Root>