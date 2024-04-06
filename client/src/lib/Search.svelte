<script lang="ts">
    import * as Command from "$lib/components/ui/command";
    import Button from "$lib/components/ui/button/button.svelte";
    let inp = "";
    let Orgs:Array<any> = [];
    let Sl:Array<any> = [];
    let Slp:Array<any> = [];
    async function getOrgs() {
        let r = await fetch("/AllOrganisations")
        Orgs = await r.json();
    }
    getOrgs();

    async function searchPost(inp:string){
      Sl = Orgs.filter((o) => o.organisation.toLowerCase().includes(inp.toLowerCase()));
      let r = await fetch(`/search?q=${inp}`);
      let data = await r.json();
      console.log(Slp,inp);
      Slp = data;
    }
    
    $: searchPost(inp)
  </script>
   
  <Command.Root class="w-[45vw] border-2 border-white rounded-lg">
    <Command.Input bind:value={inp} placeholder="Type a command or search..." />
      {#if inp !== ''}
        <Command.List>
          <Command.Separator />
          {#if Slp.length > 0}
            <span class="font-bold ml-2">Posts</span>
            <div class="flex flex-col w-full">
              {#each Slp as elem}
                <Button variant="link" class="w-full">{elem.title}</Button>
              {/each}
            </div>
          {/if}
          <Command.Separator />
          {#if Sl.length > 0}
            <span class="font-bold ml-2">Organisation</span>
            <div class="flex flex-col w-full">
              {#each Sl as elem}
                <Button variant="link" class="w-full">{elem.organisation}</Button>
              {/each}
            </div>
          {/if}
        </Command.List>
      {/if}
  </Command.Root>