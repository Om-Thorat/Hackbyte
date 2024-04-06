<script lang="ts">
    import * as Command from "$lib/components/ui/command";
    let inp = "";
    let Orgs:Array<any> = [];
    let Sl:Array<any> = [];
    async function getOrgs() {
        let r = await fetch("/AllOrganisations")
        Orgs = await r.json();
        Sl = Orgs;
        console.log(Orgs);
    }
    getOrgs();
    $: Sl = Orgs.filter((o) => o.organisation.toLowerCase().includes(inp.toLowerCase()));
  </script>
   
  <Command.Root class="w-[45vw] border-2 border-white rounded-lg">
    <Command.Input value={inp} placeholder="Type a command or search..." />
    <Command.List>
      <Command.Empty>No results found.</Command.Empty>
      <Command.Separator />
      <Command.Group heading="Companies">
        {#each Sl as elem}
            <Command.Item>{elem.organisation}</Command.Item>
        {/each}
      </Command.Group>
    </Command.List>
  </Command.Root>