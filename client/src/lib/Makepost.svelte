<script lang="ts">
  import { Button } from "$lib/components/ui/button/index.js";
  import * as Card from "$lib/components/ui/card/index.js";
  import * as Select from "$lib/components/ui/select/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
  import { Label } from "$lib/components/ui/label/index.js";
  import { SOrg } from "./store";
  import Textarea from "./components/ui/textarea/textarea.svelte";

  let Org = "";
  SOrg.subscribe((v) => (Org = v));
  let title = "";
  let Postto = "world";
  let body = "";
  let tags = "";

  async function submit() {
    const url =
      "/addpost?title=" +
      encodeURIComponent(title) +
      "&body=" +
      encodeURIComponent(body) +
      "&type=" +
      encodeURIComponent(Postto) +
      "&tags=" +
      encodeURIComponent(tags.split(" ").join("%"));
    const response = await fetch(url);
    if (response.ok) {
      // Handle successful response
    } else {
      // Handle error response
    }
  }
</script>

<Card.Root class="w-[45vw]">
  <Card.Header>
    <Card.Title>Create Post</Card.Title>
    <Card.Description>Share your thoughts!</Card.Description>
  </Card.Header>
  <Card.Content>
    <form>
      <div class="grid w-full items-center gap-4">
        <div class="flex flex-col space-y-1.5">
          <Label for="Title">Title</Label>
          <Input id="Title" bind:value={title} placeholder="A catchy title." />
        </div>
        <div class="flex flex-col space-y-1.5">
          <Label for="Postto">Post to</Label>
          <Select.Root on:selectedchange={(e) => (Postto = e.detail.value)}>
            <Select.Trigger id="Postto">
              <Select.Value placeholder="Select" />
            </Select.Trigger>
            <Select.Content>
              <Select.Item value="world" label="world">world</Select.Item>
              <Select.Item value={Org} label={Org}>{Org}</Select.Item>
            </Select.Content>
          </Select.Root>
        </div>
        <div class="flex flex-col space-y-1.5">
          <Label for="Body">Body</Label>
          <Textarea
            id="Body"
            bind:value={body}
            placeholder="Type a message here."
          />
        </div>
        <div class="flex flex-col space-y-1.5">
          <Label for="Tags">Tags</Label>
          <Input
            id="Tags"
            bind:value={tags}
            placeholder="Type your tags here."
          />
        </div>
      </div>
    </form>
  </Card.Content>
  <Card.Footer class="flex justify-between">
    <Button variant="outline">Cancel</Button>
    <Button on:click={submit}>Submit</Button>
  </Card.Footer>
</Card.Root>
