<script lang="ts">
  import { Button } from "$lib/components/ui/button";
  import Lightswitch from "$lib/Lightswitch.svelte";
  import Sidebar from "./Sidebar.svelte";
  import Review from "./Review.svelte";
  import { Slider } from "$lib/components/ui/slider";
  import Postpage from "./Postpage.svelte";
  import { Forg } from "./store";
  let Org = "";
  Forg.subscribe((e) => {
    Org = e;
  });
</script>

<div
  class="bg-slate-800 bg-opacity-45 p-10 h-screen gap-10 rounded-sm flex flex-col content-start items-center self-start"
>
  <div
    class="bg-background rounded-sm flex items-center flex-col content-start self-start w-[100%] h-screen"
  >
    <div class=" h-[40%] w-[85%] z-99 my-11 rounded-md flex">
      <div class="flex flex-col w-[50%] h-[100%]">
        <img
          src="/image.png"
          alt=""
          class="google h-[100%] w-[100%] z-99 items-center rounded-md flex flex-col justify-center position-absolute"
        />
        <h1 class="text-3xl font-bold text-center">{Org.organisation}</h1>
        <div
          class="  bg-slate-800 bg-opacity-45 h-[100%] w-[100%] z-99 items-center rounded-md flex flex-col justify-center"
        >
          <p class="text-base font-bold">Overall Rating :</p>
          <p class="text-green-500">9/10</p>
          <p>220 people rated</p>
        </div>
      </div>
      <div
        class=" flex flex-col h-[100%] w-[50%] bg-slate-800 bg-opacity-45 align-center justify-center rounded-md text-left p-11 gap-1"
      >
        <ul>Job security</ul>
        <Slider class="bg-red-500" value={[78]} max={100} step={1} />
        <ul>Work Environment</ul>
        <Slider class="bg-red-500" value={[57]} max={100} step={1} />
        <ul>Job satisfaction</ul>
        <Slider class="bg-red-500" value={[46]} max={100} step={1} />
        <ul>Maternity/Paternity</ul>
        <Slider class="bg-red-500" value={[72]} max={100} step={1} />
        <ul>Leave Management</ul>
        <Slider class="bg-red-500" value={[66]} max={100} step={1} />
        <ul>Job Security</ul>
        <Slider class="bg-red-500" value={[88]} max={100} step={1} />
      </div>
    </div>
  </div>
  <Postpage furl={`/getorgposts?org=${Org.organisation}`} />
</div>
