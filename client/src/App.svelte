<script lang="ts">
  import Isloggedin from "$lib/Isloggedin.svelte";
  import { Button } from "$lib/components/ui/button";
  
</script>
 
<Isloggedin />
<main class="min-h-[100svh] w-screen bg-background flex justify-center items-center gap-5">
  <Button href="/login">Login</Button>
  <Button href="/user">User</Button>
</main>