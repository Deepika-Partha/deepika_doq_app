<script>
  import "../app.css";
  import { onMount } from "svelte";
  import { slide } from "svelte/transition";
  import { LayoutDashboard, LibraryBig, Layers3, Boxes } from "lucide-svelte";
import { ArrowRight } from "lucide-svelte";

  let completionStatus = "incomplete";
  let isNavOpen = false;

  export async function load({ url }) {
  if (url.pathname === '/') {
    return {
      status: 301,
      redirect: '/courses'
    };
  }
}

  const toggleNav = () => {
    isNavOpen = !isNavOpen;
  };
</script>

<style>
  .tooltip {
    position: relative;
    display: inline-block;
  }

  .tooltip .tooltiptext {
    visibility: hidden;
    width: 120px;
    background-color: #555;
    color: #fff;
    text-align: center;
    border-radius: 6px;
    padding: 5px;
    position: absolute;
    z-index: 1;
    left: 125%;
    top: 50%;
    transform: translateY(-50%);
    opacity: 0;
    transition: opacity 0.3s;
  }

  .tooltip:hover .tooltiptext {
    visibility: visible;
    opacity: 1;
  }
</style>

<div class="flex h-screen">

  <div
    class={`bg-gray-900 text-white h-screen p-4 transition-all duration-300 ${isNavOpen ? "w-64" : "w-16"}`}
    transition:slide
  >

 


    <div class="flex flex-col items-center mb-6">

      <button
      class="p-2 rounded-md hover:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-white"
      on:click="{toggleNav}"
    >
    <ArrowRight />
      <!-- Add your menu icon here -->
    </button>


      
    

  
    </div>


    


    <nav class={`${isNavOpen ? "flex flex-col gap-4" : "space-y-4"}`}>

      <div class="flex items-center gap-2">
          <Boxes class="text-orange-500/80" />
          {#if isNavOpen}
            <span> Quorum </span>
          {/if}
        </div>
        

    


      <a
        href="/courses"
        class={`flex gap-4 rounded-md hover:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-white tooltip ${isNavOpen ? "flex items-center gap-2" : "justify-center"}`}
      >
        <LibraryBig />
        {#if isNavOpen}
          <span>Courses</span>
        {:else}
          <span class="tooltiptext">Courses</span>
        {/if}
      </a>

      <a
      href="/doqvault"
      class={`flex gap-4 rounded-md hover:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-white tooltip ${isNavOpen ? "flex items-center gap-2" : "items-center justify-center"}`}
    >
      <LayoutDashboard />
      {#if isNavOpen}
        <span>DoqVault</span>
      {:else}
        <span class="tooltiptext">Doqvault</span>
      {/if}
    </a>
    </nav>
  </div>


  <div class="flex-1 overflow-y-auto">
    <!-- Your main content goes here -->
    <slot></slot>
    <div class="w-full max-w-6xl mx-auto py-12 px-4 md:px-6">
      <!-- ... -->
    </div>
  </div>
</div>
