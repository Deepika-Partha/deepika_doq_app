<script>

import progress from "$lib/data/progress";

    const python_courses = [
      {
        title: "Python Crash Course",
        description: "Install VS Code, Learn the buiding blocks of Python",
        link: "/courses/python1",
      },
      {
        title: "Introduction to Python 3 Programming Tutorial",
        description: "Got through the motions of Python programming, building a Tic Tac Toe game",
        link: "/courses/python2",
      },
      {
        title: "Data Analysis with Python",
        description: "Learn how to analyze and visualize data using Python and popular libraries like Pandas, Numpy and Matplotlib.",
        link: "/courses/python3",
      },
      {
        title: "Neural Networks",
        description: "Great visual explanation of how neural networks work, building up to transformers and attention models.",
        link: "/courses/nn",
      },

      {
        title: "Deploy FastAPI on Vercel",
        description: "Deploy your python code as an API using FastAPI, hosted on Vercel.",
        link: "https://www.youtube.com/watch?v=8R-cetf_sZ4",
      }
    ];


    const webdev_courses = [
      {
        title: "Learn HTML and CSS",
        description: "Deep but quick course with lots of good examples projects.",
        link: "https://v1.scrimba.com/learn/htmlandcss",
      },
      {
        title: "Learn Javascript",
        description: "Learn the basics of Javascript and how to build interactive web pages.",
        link: "https://v1.scrimba.com/learn/learnjavascript",
      },
     
      {
        title: "Svelte Tutorial for Beginners",
        description: "Learn how to build web applications using Svelte javascript framework.",
        link: "https://www.youtube.com/watch?v=zojEMeQGGHs&list=PL4cUxeGkcC9hlbrVO_2QFVqVPhlZmz7tO",
      },

      {
        title: "Learn Tailwind CSS",
        description: "Learn to rapidly build custom designs for your frontend.",
        link: "https://v2.scrimba.com/learn-tailwind-css-c010",
      },

      {
        title: "SvelteKit & Supabase",
        description: "Learn how to integrate a database and add authentication to your app with Supabase",
        link: "/courses/supabase",
      },

      {
        title: "Intro to AI Engineering",
        description: "A crash course on building web apps powered by generative AI.",
        link: "https://v1.scrimba.com/learn/introtoaiengineering",
      },
    ]


    const optional_courses = [
      {
        title: "Git and GitHub for Beginners",
        description: "Learn how to commit changes and push to GitHub from VS Code.",
        link: "https://www.youtube.com/watch?v=RGOj5yH7evk",
      },
      {
        title: "LangChain Crash Course",
        description: "Learn RAG, vector stores, and creating agents with 2 projects.",
        link: "https://www.youtube.com/watch?v=lG7Uxts9SXs",
      },
    ]

  </script>
  


  <div class="container mx-auto px-4 py-12">
    <h1 class="text-4xl font-bold text-center mb-12">Courses</h1>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
      <div>
        <h2 class="text-xl font-bold mb-6 flex justify-center">Python/ML</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          {#each python_courses as course}
            <div class="bg-white rounded-lg shadow-lg overflow-hidden transition-all duration-300 ease-in-out transform hover:-translate-y-1 hover:shadow-xl">
              <a href={course.link} class="block p-6">
                <h3 class="text-xl font-bold mb-2 text-gray-800 hover:text-primary transition-colors duration-300">{course.title}</h3>
                <p class="text-gray-600">{course.description}</p>
              </a>
            </div>
          {/each}
        </div>
      </div>
      <div>
        <h2 class="text-xl font-bold mb-6 flex justify-center">Web Development</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          {#each webdev_courses as course}
            <div class="bg-white rounded-lg shadow-lg overflow-hidden transition-all duration-300 ease-in-out transform hover:-translate-y-1 hover:shadow-xl">
              <a href={course.link} class="block p-6">
                <h3 class="text-xl font-bold mb-2 text-gray-800 hover:text-primary transition-colors duration-300">{course.title}</h3>
                <p class="text-gray-600">{course.description}</p>
              </a>
            </div>
          {/each}
        </div>
      </div>
    </div>

    <h2 class="text-2xl font-bold text-center mb-8">Optional</h2>
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
      {#each optional_courses as course}
        <div class="bg-white rounded-lg shadow-lg overflow-hidden transition-all duration-300 ease-in-out transform hover:-translate-y-1 hover:shadow-xl">
          <a href={course.link} class="block p-6">
            <h3 class="text-xl font-bold mb-2 text-gray-800 hover:text-primary transition-colors duration-300">{course.title}</h3>
            <p class="text-gray-600">{course.description}</p>
          </a>
        </div>
      {/each}
    </div>

    <div class="mt-16">
      <h2 class="text-2xl font-bold text-center mb-8">Progress</h2>
      <div class="flex justify-center space-x-8">
        {#each progress as intern}
          <div class="flex flex-col items-center">
            <div class="w-8 h-32 bg-gray-200 rounded-lg relative">
              <div class="absolute bottom-0 left-0 right-0 bg-blue-500 rounded-lg transition-all duration-500 ease-in-out" style="height: {intern.progress}%"></div>
            </div>
            <div class="mt-2 text-center">
              <p class="text-lg font-semibold">{intern.name}</p>
              <p class="text-gray-600">{intern.progress}%</p>
            </div>
          </div>
        {/each}
      </div>
    </div>
  </div>


  <div class="absolute bottom-0 bg-gray-100 py-4 mt-12 w-full">
    <p class="bottom-0 text-center text-gray-600">Complete more courses! ʕ•ᴥ•ʔ</p>
  </div>