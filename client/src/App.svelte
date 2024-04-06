<script lang="ts">
  import Isloggedin from "$lib/Isloggedin.svelte";
  import Navbar from "$lib/Navbar.svelte";
  import Postcard from "$lib/Postcard.svelte";
  import Postpage from "$lib/Postpage.svelte";
  import Search from "$lib/Search.svelte";
  import { ModeWatcher } from "mode-watcher";
  
</script>

<ModeWatcher />
<!-- <Isloggedin /> -->

<main class="flex flex-col h-[100svh] w-screen justify-center items-center gap-4">
<!-- <Navbar /> -->
<!-- <Search /> -->
<Postpage />
<!-- <Postpage /> -->
</main>