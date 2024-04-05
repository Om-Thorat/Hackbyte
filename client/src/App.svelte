<script lang="ts">
  import Isloggedin from "$lib/Isloggedin.svelte";
  import { Button } from "$lib/components/ui/button";
  import { ModeWatcher } from "mode-watcher";
</script>
<ModeWatcher />
<Isloggedin />
<main class="min-h-[100svh] w-screen bg-background  gap-5">
  <Button href="/login">Login</Button>
  <Button href="/user">User</Button>
  <Button href="/logout">logout</Button>
</main>