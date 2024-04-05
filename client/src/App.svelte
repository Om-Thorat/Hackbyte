<script lang="ts">
  import Isloggedin from "$lib/Isloggedin.svelte";
  import Lightswitch from "$lib/Lightswitch.svelte";
  import { Button } from "$lib/components/ui/button";
  import { ModeWatcher } from "mode-watcher";
</script>
<ModeWatcher />
<Isloggedin />
<main class="min-h-[100svh] w-screen bg-background flex justify-center items-center gap-5">
  <Lightswitch />
  <Button href="/login">Login</Button>
  <Button href="/user">User</Button>
  <Button href="/logout">logout</Button>
</main>