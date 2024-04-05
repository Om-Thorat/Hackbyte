<script lang="ts">
    import { Button } from "$lib/components/ui/button";
    import Lightswitch from "$lib/Lightswitch.svelte";
</script>
<div>
    <Lightswitch />
    <Button href="/login">Login</Button>
    <Button href="/user">User</Button>
    <Button href="/logout">logout</Button>
</div>