<script lang="ts">
  import Button from "$lib/components/ui/button/button.svelte";
  </script>


<div class="bg-background h-screen w-[20%] flex flex-col py-8 justify-end bg-green-500 mt-4">
    <div class="flex flex-col w-[100%] h-2/3 bg-orange-500 gap-12 align-center ">
      <Button href="/home">Home</Button>
      <Button href="/about">About</Button>
      <Button href="/contact">Contact</Button>
    </div>
    <div class ="flex flex-col  gap-3  align-middle items-left justify-between  ">
      <Button  href="/login">Login</Button>
      <Button href="/user">User</Button>
      <Button href="/logout">Logout</Button>
    </div>
  </div>
