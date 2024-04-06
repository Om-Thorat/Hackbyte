<script lang="ts">
    import Button from "./components/ui/button/button.svelte";
    import * as Sheet from "$lib/components/ui/sheet/index.js";
    import { Input } from "$lib/components/ui/input/index.js";
    import { Label } from "$lib/components/ui/label/index.js";
    import Sidebar from "./Sidebar.svelte";
    import Mostactivecompany from "./Mostactivecompany.svelte";
    import Topratedcompany from "./Topratedcompany.svelte";

  </script>
   
<Sheet.Root>
    <Sheet.Trigger asChild let:builder>
      <Button builders={[builder]} variant="outline" class="bg-opacity-10 md:hidden w-[3svw] h-[3svh] px-2 py-1 rounded-md gap-2 outline outline-2 flex flex-col justify-center">
        <div class="w-[90%] bg-white  h-[3px]"></div>
        <div class="w-[75%] bg-white h-[3px]"></div>
        <div class="w-[60%] bg-white h-[3px]"></div>
    </Button>
    </Sheet.Trigger>
    <Sheet.Content side="left">
      <Sheet.Header>
        <Sheet.Title>NavBar</Sheet.Title>
       </Sheet.Header >
       <div class="flex justify-center w-full">
       <Sidebar />
    </div> 
        <!-- <Mostactivecompany />
        <Topratedcompany /> -->
    </Sheet.Content>
  </Sheet.Root>
