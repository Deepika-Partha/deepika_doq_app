<script>
   import { Label } from "$lib/components/ui/label/";
  import { Textarea } from "$lib/components/ui/textarea/";
  import { Button } from "$lib/components/ui/button/";
  import { Avatar } from "$lib/components/ui/avatar/";
  import Youtube from "svelte-youtube-embed";
  import { createEventDispatcher } from 'svelte';

  export let video_data;
  export let currentVideoIndex;

  const dispatch = createEventDispatcher();

  let completionStatus = Array(video_data.length).fill("incomplete");

  const handleCompletion = () => {
    if (completionStatus[currentVideoIndex] === "incomplete") {
      completionStatus[currentVideoIndex] = "partial";
    } else if (completionStatus[currentVideoIndex] === "partial") {
      completionStatus[currentVideoIndex] = "completed";
    }
  };

  const handleNextVideo = () => {
    dispatch('nextVideo');
  };

    const handlePreviousVideo = () => {
    dispatch('previousVideo');
    };
  
    const comments = [
      {
        username: "@iamwillpursell",
        avatar: "/placeholder.svg",
        timestamp: "5 months ago",
        content: "I really love the ecosystem Vercel is creating. The way each component can be added and modified with ease really makes these tools attractive.",
      },
      {
        username: "@HackSoft",
        avatar: "/placeholder.svg",
        timestamp: "2 months ago",
        content: "We are more than excited to leverage all the new stuff, building better products for our clients ✨",
      },
      {
        username: "@greed7513",
        avatar: "/placeholder.svg",
        timestamp: "6 days ago",
        content: "does anyone know which monospace are they using when showing code?",
      },
      {
        username: "@shadcn",
        avatar: "/placeholder.svg",
        timestamp: "1 day ago",
        content: "The Vercel team has done an amazing job with their component library. It's so easy to use and customize.",
      },
      {
        username: "@vercelbot",
        avatar: "/placeholder.svg",
        timestamp: "3 hours ago",
        content: "We're so glad you're enjoying the Vercel ecosystem! Let us know if you have any other feedback or questions.",
      },
    ];
  </script>
  
  <div class="w-full max-w-6xl mx-auto py-12 px-4 md:px-6">
    <div class="space-y-8">
      <div class="rounded-xl overflow-hidden">
        <Youtube id={video_data[currentVideoIndex].link} />
      </div>
      <div>
      <div class="text-2xl mb-2"> {video_data[currentVideoIndex].title} </div>
      <div>{video_data[currentVideoIndex].text} </div>
    </div>
      <div class="flex justify-between">
        <Button
  type="button"
  class={`px-4 py-2 border-2 border-black/10 rounded-xl rounded-md transition-colors ${
    completionStatus[currentVideoIndex] === "incomplete"
      ? "bg-white text-black hover:bg-gray-200"
      : completionStatus[currentVideoIndex] === "partial"
      ? "bg-yellow-500 text-white hover:bg-yellow-600"
      : "bg-green-500 text-white hover:bg-green-600"
  }`}
  on:click={handleCompletion}
>
  {completionStatus[currentVideoIndex] === "incomplete"
    ? "Complete"
    : completionStatus[currentVideoIndex] === "partial"
    ? "Partial"
    : "Completed"}
</Button>


{#if video_data.length > 1}
<div class="flex space-x-2">
    <Button
      type="button"
      class="px-4 py-2 border-2 border-black/10 rounded-md transition-colors bg-white text-gray-900 hover:bg-gray-200"
      disabled={currentVideoIndex === 0}
      on:click={handlePreviousVideo}
    >
      Previous Video
    </Button>
    <Button
      type="button"
      class={`px-4 py-2 border-2 border-black/10 rounded-md transition-colors ${
        completionStatus[currentVideoIndex] === "completed"
          ? "bg-white text-gray-900 hover:bg-gray-200"
          : "bg-gray-400 text-white cursor-not-allowed"
      }`}
      disabled={completionStatus[currentVideoIndex] !== "completed"}
      on:click={handleNextVideo}
    >
      Next Video
    </Button>
  </div>

  {/if}
      </div>
    </div>


    <div class="space-y-8 mt-10 hidden">
      <div>
        <h2 class="text-2xl font-bold mb-4">Comments</h2>
        <form class="bg-gray-100 dark:bg-gray-800 rounded-lg p-6 space-y-4">
          <div class="space-y-2">
            <Label htmlFor="comment">Comment</Label>
            <Textarea id="comment" placeholder="Enter your comment" class="min-h-[100px]" />
          </div>
          <Button type="submit" class="w-full">Submit</Button>
        </form>
      </div>
      <div class="space-y-4 max-h-[400px] overflow-auto">
        {#each comments as comment}
          <div class="text-sm flex items-start gap-4">
            <Avatar class="w-10 h-10 border">
              <img src={comment.avatar} alt={comment.username} />
              <span slot="fallback">{comment.username.slice(0, 2)}</span>
            </Avatar>
            <div class="grid gap-1.5">
              <div class="flex items-center gap-2">
                <div class="font-semibold">{comment.username}</div>
                <div class="text-gray-500 text-xs dark:text-gray-400">{comment.timestamp}</div>
              </div>
              <div>{comment.content}</div>
            </div>
          </div>
        {/each}
      </div>
    </div>
  </div>

  