<script lang="ts">
    import Search from "./Search.svelte";
    import Topratedcompany from "./Topratedcompany.svelte";
    import CardHeader from "./components/ui/card/card-header.svelte";
    import * as Card from "$lib/components/ui/card";
    import { Button } from "$lib/components/ui/button/index.js";
    import { Textarea } from "$lib/components/ui/textarea/index.js";
    import Mostlikes from "./Mostlikes.svelte";
</script>

<div class="h-[100svh] w-[100svw] bg-background flex items-center justify-center gap-5">
    <div class=" bg-slate-800 bg-opacity-45 p-10 w-[60%] gap-10 rounded-sm flex flex-col content-start items-center self-start">
      <Search />
    <div class="card w-fullrounded-lg ">
        <Card.Root class="border-2 h-[75svh] ">
        <div>
        <CardHeader >
            <h1 class="text-4xl">Join the Amazon Conversation</h1>
        </CardHeader>
        <Card.Content class='text-lg'>
            <p>Are you an Amazon enthusiast? Whether you're a seasoned Prime member, an avid Kindle reader, or just someone who loves to shop, this is the place for you. Join us to discuss all things Amazon-related - from the latest deals and products to tips and tricks for making the most out of your Amazon experience.

                Feel free to start new threads, ask questions, share your favorite Amazon finds, or even vent about any issues you've encountered. Let's build a vibrant community where we can connect, learn, and have fun together!
                
                To get started, why not introduce yourself and share what you love most about Amazon? Happy chatting!</p>
        </Card.Content>
        </div>
        <Card.Footer class="gap-7 flex flex-col">
           <div class="flex justify-start gap-3">
                <button><img src="./heartunfilled.png" alt="" class="h-[3svh] w-[2svw] "></button>
                

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
    </div>
    <div class="bg-background h-[100svh] w-[20%] flex flex-col justify-center items-center m-2">
        <Mostlikes />
        <Topratedcompany />
    </div>
  </div>