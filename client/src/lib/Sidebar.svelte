<script lang="ts">
  import Button from "$lib/components/ui/button/button.svelte";
    import Badge from "$lib/components/ui/badge/badge.svelte";
    import * as Accordion from "$lib/components/ui/accordion";

  </script>


<div class="bg-background h-screen w-[20%] flex flex-col py-8 justify-end">
    <div class="flex flex-col w-[100%] h-2/3 gap-12 align-center items-center">
      
    <div class="hometab h-8 w-[100%]rounded flex items-center "> 
        <svg width="20" height="20" viewBox="0 0  15 15 " fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M7.07926 0.222253C7.31275 -0.007434 7.6873 -0.007434 7.92079 0.222253L14.6708 6.86227C14.907 7.09465 14.9101 7.47453 14.6778 7.71076C14.4454 7.947 14.0655 7.95012 13.8293 7.71773L13 6.90201V12.5C13 12.7761 12.7762 13 12.5 13H2.50002C2.22388 13 2.00002 12.7761 2.00002 12.5V6.90201L1.17079 7.71773C0.934558 7.95012 0.554672 7.947 0.32229 7.71076C0.0899079 7.47453 0.0930283 7.09465 0.32926 6.86227L7.07926 0.222253ZM7.50002 1.49163L12 5.91831V12H10V8.49999C10 8.22385 9.77617 7.99999 9.50002 7.99999H6.50002C6.22388 7.99999 6.00002 8.22385 6.00002 8.49999V12H3.00002V5.91831L7.50002 1.49163ZM7.00002 12H9.00002V8.99999H7.00002V12Z" fill="currentColor" fill-rule="evenodd" clip-rule="evenodd" ></path></svg>
        <a href="/" class="text-2xl font-bold  text-center px-8">Home</a>
    </div>
    <div class="company h-8 w-[100%] text-center rounded "> 
        <a href="/" class="text-2xl text-center">Microsoft™</a>
    </div>
     <div class="explore"></div><Badge variant="outline" class ="text-2xl">Explore Tags</Badge>
    <div class="flex flex-col">
        <div>  <Badge variant="outline" class="bg-pink-500" ><a href="/">#Hackbyte</a></Badge>
            <Badge variant="outline" class="bg-yellow-600"><a href="/">#MLH</a></Badge>
               <Badge variant="outline" class="bg-green-500"><a href="/">#Holidays</a></Badge>
            </div>
      
        <div class="w-[100%] flex ">
            <Badge variant="outline" class="bg-orange-500"><a href="/">#Team</a></Badge>
            <Badge variant="outline" class ="bg-teal-700"><a href="/">#Toxic</a></Badge>
            <Badge variant="outline" class = " bg-blue-700"><a href="/">#WorkEnv</a></Badge>
        </div>
    </div>
    </div>
   
   
    <div class ="flex flex-col  gap-3  align-middle items-left justify-between">
      <Button  href="/login">Login</Button>
      <Button href="/user">User</Button>
      <Button href="/logout">Logout</Button>

    </div>
    
  </div>
  <style>
    .hometab{
        transition: 0.3s;
    }
    .hometab:hover{
         scale: 1.2;
       
    
}
.company{
        transition: 0.3s;
    }
    .company:hover{
        scale:1.2;
    
}

  </style>
