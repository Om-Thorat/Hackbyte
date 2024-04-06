<script lang="ts">
  import Isloggedin from "$lib/Isloggedin.svelte";
  import Navbar from "$lib/Navbar.svelte";
  import Postcard from "$lib/Postcard.svelte";
  import Postpage from "$lib/Postpage.svelte";
  import Search from "$lib/Search.svelte";
  import Button from "$lib/components/ui/button/button.svelte";
  import { ModeWatcher } from "mode-watcher";
  import Sidebar from  "$lib/Sidebar.svelte";

  

  
</script>

<ModeWatcher />
<div class="h-[100svh] w-[100svw] bg-background flex items-center justify-center">
 
  <Sidebar/>

    
  <div class=" bg-slate-500 p-10 mt-28 w-[60%] gap-10 rounded-sm flex flex-col justify-start items-center">
    <Search />
    <Postpage />
  </div>
  <div class="bg-background h-[100svh] w-[20%] flex flex-col justify-center items-center"><span>hellu</span>
      <div class=" h-[40svh] w-[70%] m-3 ">
          <h1>Some Leaderboard Title</h1>
      </div>
      <div class=" h-[40svh] w-[70%] m-3 ">
          <h1>Some Leaderboard Title</h1>
      </div>
  </div>

</div>