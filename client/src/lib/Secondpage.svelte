<script>
    import Search from "./Search.svelte";
    import { Button } from "$lib/components/ui/button/index.js";


</script>

<div class="h-[100svh] w-[100svw] bg-background flex items-center justify-center ">
    <div class="bg-background h-[100svh] w-[20%]">
         <button href="/login">Login</button>
         
    </div>
    <div class=" bg-gray-800 h-[95svh] w-[60%] rounded-sm m-1">
        <Search />
    </div>
    <div class="bg-background h-[100svh] w-[20%] flex flex-col justify-center items-center">
        <div class=" h-[40svh] w-[75%] m-3 border rounded-sm">
            <h1 class="m-2">Some Leaderboard Title</h1>
            <div class="flex">
            <img src="./google-g-2015-logo-png-transparent.png" alt="" class="h-[3svh] w-[1.75svw] m-1">
             <h2>stars</h2>
            </div> 
            <div class="flex">
                <img src="./google-g-2015-logo-png-transparent.png" alt="" class="h-[3svh] w-[1.75svw] m-1">
                <h2>stars</h2>
            </div> 
            <div class="flex">
                <img src="./google-g-2015-logo-png-transparent.png" alt="" class="h-[3svh] w-[1.75svw] m-1">
                <h2>stars</h2>
            </div> 
            <div class="flex">
                <img src="./google-g-2015-logo-png-transparent.png" alt="" class="h-[3svh] w-[1.75svw] m-1">
                <h2>stars</h2>
            </div> 
        </div>
        <div class=" h-[40svh] w-[75%] m-3 border rounded-sm">
            <h1 class="m-2">Some Leaderboard Title</h1>
            <div class="flex">
                <img src="./google-g-2015-logo-png-transparent.png" alt="" class="h-[3svh] w-[1.75svw] m-1">
                 <h2>stars</h2>
                </div> 
                <div class="flex">
                    <img src="./google-g-2015-logo-png-transparent.png" alt="" class="h-[3svh] w-[1.75svw] m-1">
                    <h2>stars</h2>
                </div> 
                <div class="flex">
                    <img src="./google-g-2015-logo-png-transparent.png" alt="" class="h-[3svh] w-[1.75svw] m-1">
                    <h2>stars</h2>
                </div> 
                <div class="flex">
                    <img src="./google-g-2015-logo-png-transparent.png" alt="" class="h-[3svh] w-[1.75svw] m-1">
                    <h2>stars</h2>
                </div> 
        </div>
    </div>

</div>