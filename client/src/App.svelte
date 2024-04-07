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
  import Review from "$lib/Review.svelte";
  let Lstate = "Home"
  import Postinfo from "$lib/Postinfo.svelte";
    import Sideresponsive from "$lib/Sideresponsive.svelte";
  import Badge from "$lib/components/ui/badge/badge.svelte";
  import * as Accordion from "$lib/components/ui/accordion";
  import { onMount } from "svelte";
  import { SOrg, state } from "$lib/store";
  import Separator from "$lib/components/ui/separator/separator.svelte";

  let Org = "None";
  async function Getuser() {
    const response = await fetch("/user");
    const data = await response.text();
    if (data === "No") {
      //
    } else {
      let tmp = JSON.parse(data);
      Org = tmp.userinfo.email.split("@")[1].split(".")[0];
      SOrg.set(Org);
    }
  }
  onMount(Getuser);
  state.subscribe((e)=>{Lstate=e});
</script>

<ModeWatcher />
<div class="h-[100svh] w-[100svw] bg-background flex items-center justify-center gap-5">
  <div
  class="bg-background hidden md:flex h-screen w-[20%] flex-col py-8 justify-end ml-5 noScroll"
>
  <div class="flex flex-col w-[100%] h-3/4 gap-12 align-center items-center">
    <img alt="Classified logo" src="/Classified.svg" class="scale-150" />
    <Separator class="bg-slate-300" />
    <div class="flex flex-col gap-12 items-center">
    <div class="hometab h-8 rounded flex items-center">
      <Button variant="outline" on:click={()=>state.set("Home")} class="rounded-full border-cyan-50 border-2 p-6 text-xl font-bold text-center" on:click={() => state.set("Home")}>
      Home</Button>
    </div>
    <div class="hometab h-8 text-center rounded">
      <Button variant="outline" on:click={()=>state.set("orgpost")} class="rounded-full border-cyan-50 border-2 p-6 font-bold text-xl text-center">{Org.toUpperCase()}™</Button>
    </div>
    <div class="hometab h-8 text-center rounded">
      <Button
      variant="outline"
        class=" hometab text-xl font-bold rounded-full border-cyan-50 border-2 p-6 w-32"
        on:click={() => state.set("post")}>Post</Button
      >
    </div>
    </div>
    <div class="explore"></div>
    <Badge variant="outline" class="rounded-full px-8 py-2 text-2xl">Explore Tags</Badge>
    <div class="flex flex-col gap-1">
      <div class="flex gap-1">
        <Badge variant="outline" class="bg-pink-500"
          ><a href="/">Hackbyte</a></Badge
        >
        <Badge variant="outline" class="bg-yellow-600"
          ><a href="/">MLH</a></Badge
        >
        <Badge variant="outline" class="bg-green-500"
          ><a href="/">Holidays</a></Badge
        >
      </div>

      <div class="flex gap-1">
        <Badge variant="outline" class="bg-orange-500"
          ><a href="/">Team</a></Badge
        >
        <Badge variant="outline" class="bg-teal-700"
          ><a href="/">Toxic</a></Badge
        >
        <Badge variant="outline" class=" bg-blue-700"
          ><a href="/">WorkEnv</a></Badge
        >
      </div>
    </div>
  </div>
  <div
    class=" w-[100%] h-1 bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 my-4"
  ></div>
  <div class="flex flex-col gap-3 align-middle items-left justify-between">
    {#if Org !== "None"}
      <Button href="/login" class="hidden">Login</Button>
      <Button href="/logout">Logout</Button>
    {:else}
      <Button href="/login">Login</Button>
      <Button href="/logout" class="hidden">Logout</Button>
    {/if}
  </div>
</div>
  
  <div class=" bg-slate-800 bg-opacity-45 p-10 w-[80%] md:w-[60%] gap-10 rounded-sm flex flex-col content-start items-center self-start">
    <Sideresponsive />
    <Search />
    {#if Lstate === "Home"}
      <Postpage furl="/posts" />
    {:else if Lstate === "orgpost"}
      <Postpage furl="/OrgPosts" />
    {:else if Lstate === "seepost"}
      <Postinfo />
    {:else if Lstate === "post"}
        <Makepost />
    {:else if Lstate === "review"}
        <Review />
    {/if}
  </div>
  <div class="bg-background hidden md:flex h-[100svh] w-[20%] flex flex-col justify-center items-center m-2">
    <Mostactivecompany />
    <Topratedcompany />
  </div>
</div>
