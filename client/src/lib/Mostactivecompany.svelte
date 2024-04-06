<script lang="ts">
    import Badge from "./components/ui/badge/badge.svelte";
</script>

<div class=" h-[40svh] w-[82%] m-3 border rounded-sm flex flex-col gap-2">
    <h1 class="m-2">Top Rated Companies</h1>
    <div class="flex justify-between items-center">
      <Badge class="text-base mx-2 w-full">Google</Badge>
      
    </div>
    <div class="flex justify-between items-center">
        <Badge class="text-base mx-2 w-full">Microsoft</Badge>
        
    </div>
    <div class="flex justify-between items-center">
        <Badge class="text-base mx-2 w-full">YDO</Badge>
    </div> 
</div>