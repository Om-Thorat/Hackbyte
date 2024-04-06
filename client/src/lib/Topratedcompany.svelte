<script lang="ts">
    import Badge from "./components/ui/badge/badge.svelte";
</script>

<div class=" h-[40svh] w-[82%] m-3 border rounded-sm gap-2 flex flex-col">
    <div><h1 class="m-2">Most Active Companies</h1></div>
    <div class="flex justify-between items-center">
      <Badge class="text-base mx-2">Google</Badge>
      <h2 class="text-lg text-green-600"> 9.8 </h2>
      <h2 class="text-slate-500 text-xs italic mr-2">rated by 2k users</h2>
    </div>
    <div class="flex justify-between items-center">
        <Badge class="text-base mx-2">Microsoft</Badge>
        <h2 class="text-lg text-yellow-600"> 5.6 </h2>
        <h2 class="text-slate-500 text-xs italic mr-2">rated by 2k users</h2>
    </div>
    <div class="flex justify-between items-center">
        <Badge class="text-base mx-2">YDO</Badge>
        <h2 class="text-lg text-red-600"> 2.3 </h2>
        <h2 class="text-slate-500 text-xs italic mr-2">rated by 2k users</h2>
    </div> 
</div>