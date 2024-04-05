<script lang="ts">
  import Isloggedin from "$lib/Isloggedin.svelte";
  import Navbar from "$lib/Navbar.svelte";
  import Postpage from "$lib/Postpage.Svelte";
  import { ModeWatcher } from "mode-watcher";
  
</script>

<Navbar />
<ModeWatcher />
<!-- <Isloggedin /> -->
<Postpage />