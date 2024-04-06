<script lang="ts">
  import Isloggedin from "$lib/Isloggedin.svelte";
  import Navbar from "$lib/Navbar.svelte";
  import Postcard from "$lib/Postcard.svelte";
  import Postpage from "$lib/Postpage.svelte";
  import Search from "$lib/Search.svelte";
  import Button from "$lib/components/ui/button/button.svelte";
  import { ModeWatcher } from "mode-watcher";
  import Sidebar from  "$lib/Sidebar.svelte";
  import Mostactivecompany from "$lib/Mostactivecompany.svelte";
  import Topratedcompany from "$lib/Topratedcompany.svelte";
  import Makepost from "$lib/Makepost.svelte";

  let Lstate = "Home"
  import {state} from "$lib/store";

  state.subscribe((e)=>{Lstate=e});
</script>

<ModeWatcher />
<div class="h-[100svh] w-[100svw] bg-background flex items-center justify-center gap-5">
  <Sidebar/>
  <div class=" bg-slate-800 bg-opacity-45 p-10 w-[60%] gap-10 rounded-sm flex flex-col content-start items-center self-start">
    <Search />
    {#if Lstate === "Home"}
      <Postpage />
    {:else if Lstate === "post"}
        <Makepost />
    {/if}
  </div>
  <div class="bg-background h-[100svh] w-[20%] flex flex-col justify-center items-center m-2">
    <Mostactivecompany />
    <Topratedcompany />
  </div>
</div>