<script lang="ts">
    import { Button } from "$lib/components/ui/button";
    import Lightswitch from "$lib/Lightswitch.svelte";
</script>

<style>
 .navbar{
    position:fixed;
    top: 30px;
    padding: 10px;
    left :8%;
    display: flex;
    z-index: 1000;
   
 }

</style>

<div class="navbar flex justify-end bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 p-4 rounded-lg w-5/6 opacity-75">
    <div class="flex space-x-4 ">
        <Button href="/login">Login</Button>
        <Button href="/user">User</Button>
        <Button href="/logout">Logout</Button>
        <Lightswitch />
    </div>
</div>
   
