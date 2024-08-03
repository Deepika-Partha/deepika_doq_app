<script>
  import { qaStore } from '../../stores.js';

  let searchQuery = '';
  let error = null;
  let data = null;

  async function fetchData(query) {
    try {
      console.log('Fetching data...');
      const response = await fetch('/api/wrapper/', {  
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query })
      });
      if (!response.ok) {
        throw new Error(`HTTP error ${response.status}`);
      }
      data = await response.json();
      console.log("Fetched Data: ", data);
    } catch (err) {
      error = err.message;
    }
  }

  function handleSearch() {
    fetchData(searchQuery);
    searchQuery = ''; // Clear the search box after searching
  }

  // Preprocess data
  $: formattedData = data?.map(item => {
    const parts = item.split(': ');
    return {
      subject: parts[0],
      content: parts.slice(1).join(': ')
    };
  });
</script>



<main class="custom-background">
  <div class="header-image">
    <!-- svelte-ignore a11y-img-redundant-alt -->
    <img src="https://images.squarespace-cdn.com/content/v1/64ba92ff4c24fe41a3c67b1d/1689953074945-9WI8FKUEAOY9HQX8636Q/Sleek+Objects+1.jpg" alt="Header Image">
    <div class="header-text">qBotica</div>
    <div class="doqvault">
      <a href="/doqvault" class="doqvault-button">Redirect to DoqVault</a>
    </div>
  </div>

  <h1>DoqVault</h1>
  <h2>Search below for relevant tickets or click FAQ to view all existing tickets</h2>

  <div class="faq-boxes">
    <a href="/faq" class="faq-button">FAQs</a>
  </div>

  <div class="search-container">
    <input 
      type="text" 
      bind:value={searchQuery}
      placeholder="Search tickets" 
      class="search-input"
    >
    <button on:click={handleSearch} class="go-button">🔍</button>
  </div>

  <div class="answer-box">
      {#if formattedData}
        <div>
          {#each formattedData as { subject, content }, index}
            <div class="ticket-box">
              <p><strong>{subject}</strong></p>
              <p>{content}</p>
            </div>
          {/each}
        </div>
      {:else if error}
        <p class="error-message">Error: {error}</p>
      {/if}
    </div>
  
  
</main>

<style>

@font-face {
  font-family: 'adonis-web';
  font-style: normal;
  font-weight: 400;
  src:url(https://use.typekit.net/pf/ss/qdyr/n4/l?subset_id=2&primer=9f562d6ca39adae019ef00367c3f3deae3c8627f22e3b025ba425fbc2aac6431&fvd=n4&ec_token=BInhlQ%2Bl4i%2FTK2LNzmpe2QC%2Bdl6Qc7iJa15oy7OfSGK%2BY7lwDRam4FlQCIzQGEqAiJZo10MshaDLZWgX%2FckdPK0bOW%2FAfpkj2O5MO1d7Aul7v1RGoa7OBxfdciGAxZqjHAPKKo0fqkxxKF%2F9mM9JjA%3D%3D) format("woff2"),url(https://use.typekit.net/pf/ss/qdyr/n4/d?subset_id=2&primer=9f562d6ca39adae019ef00367c3f3deae3c8627f22e3b025ba425fbc2aac6431&fvd=n4&ec_token=BInhlQ%2Bl4i%2FTK2LNzmpe2QC%2Bdl6Qc7iJa15oy7OfSGK%2BY7lwDRam4FlQCIzQGEqAiJZo10MshaDLZWgX%2FckdPK0bOW%2FAfpkj2O5MO1d7Aul7v1RGoa7OBxfdciGAxZqjHAPKKo0fqkxxKF%2F9mM9JjA%3D%3D) format("woff"),url(https://use.typekit.net/pf/ss/qdyr/n4/a?subset_id=2&primer=9f562d6ca39adae019ef00367c3f3deae3c8627f22e3b025ba425fbc2aac6431&fvd=n4&ec_token=BInhlQ%2Bl4i%2FTK2LNzmpe2QC%2Bdl6Qc7iJa15oy7OfSGK%2BY7lwDRam4FlQCIzQGEqAiJZo10MshaDLZWgX%2FckdPK0bOW%2FAfpkj2O5MO1d7Aul7v1RGoa7OBxfdciGAxZqjHAPKKo0fqkxxKF%2F9mM9JjA%3D%3D) format("opentype");font-weight:400;font-style:normal;}

  @font-face {
  font-family: 'Pontano Sans';
  font-style: normal;
  font-weight: 400;
  src: url(https://fonts.gstatic.com/s/pontanosans/v17/qFdD35GdgYR8EzR6oBLDHa3ayz8NoVgyNIjK.woff2) format('woff2');
  unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
}

/* orange: background-color: #E9CEB0; */

:global(body) {
  background-color: #ffffff; /* Light orange */
  margin: 0;
  padding: 0;
  font-family: 'Pontano Sans', sans-serif;
}

main.custom-background {
  background-color: #E9CEB0; 
  max-width: 100%; 
  margin: 0 auto;
  padding: 20px;
  overflow: hidden;
  height: 12in;
}

main {
  max-width: 100%; /* Ensure main content spans full width */
  margin: 0 auto;
  padding: 20px;
  color: white;
  overflow: hidden;
  /* height: auto; */
} 

.header-image {
  width: 100vw; /* Full viewport width */
  height: 2.3in; /* 2 inches tall */
  overflow: hidden;
  margin: 0; /* Remove any margin to ensure full width */
  position: relative; /* Allows for positioning the image */
}

.header-image img {
  position: absolute; /* Remove the image from the document flow */
  top: 50%; /* Position the image at the center of the container */
  left: 42%;
  width: 100vw; /* Full viewport width */
  height: auto; /* Maintain aspect ratio */
  min-height: 100%; /* Ensure the image covers the height */
  object-fit: cover; /* Cover the container without stretching */
  object-position: center; /* Center the image */
  transform: translate(-50%, -50%); /* Adjust to center the image */
  display: block; /* Remove any extra space below the image */
}

.header-text {
  position: absolute;
  top: 10px;
  left: 10px;
  color: white;
  font-family: 'adonis-web', sans-serif;
  font-size: 2em;
}

.doqvault {
  position: absolute;
  top: 10px;
  right: 130px; /* Adjust this value to move the button left */
}

.doqvault-button {
  width: 2in;
  height: 60px;
  background-color: hsla(22.54, 88.72%, 61.76%, 1);
  border: none;
  border-radius: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  color: white;
  font-size: 1em;
  font-family: 'adonis-web', sans-serif;
  cursor: pointer;
  text-align: center; /* Ensure text is centered horizontally */
  line-height: 1.2;
}

.doqvault-button:hover {
  background-color: rgba(189, 107, 6, 0.81);
}

h1 {
  text-align: center;
  color: rgba(0, 0, 0, 0.954);
  font-family: 'adonis-web', sans-serif;
  font-size: 4em;
  margin-top: 40px;
  margin-bottom: 10px;
}

h2 {
  text-align: center;
  color: black;
  font-size: 1.2em;
  font-family: 'adonis-web', sans-serif;
  font-weight: 200;
  margin-bottom: 30px;
}

.search-container {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
  
}

.search-input {
  width: 450px;
  padding: 10px;
  font-size: 16px;
  border: 2px solid white; /* White border */
  border-radius: 30px 0 0 30px;
  outline: none;
  background-color: #E9CEB0;
  outline: none;
  color: black;
  transition: placeholder-color 0.3s ease; 
}

/* Hide placeholder on hover */


.search-input:hover::placeholder {
  color: transparent; /* Ensure placeholder is hidden on hover */
}

/* Optionally, style the input text color when focused */
.search-input:focus {
  color: black; /* Change text color when input is focused */
}

.go-button {
  background-color: hsla( 22.54,88.72%,61.76% ,1);
  border: 2px solid white;
  border-radius: 0 30px 30px 0;
  color: white;
  padding: 10px 15px;
  font-size: 16px;
  cursor: pointer;
  outline: none;
}

.go-button:hover {
  background-color: rgba(189, 107, 6, 0.81);
}

.answer-box {
  width: 10in;
  min-height: 70px;
  padding: 10px;
  margin: 20px auto; /* Centers horizontally and adds vertical spacing */
  background-color: rgb(255, 255, 255);
  color: black;
  display: block; /* Ensures that the element is treated as a block-level element */
  font-family: 'adnois-web', sans-serif;
}

.error-message {
  color: red;
}

.faq-boxes {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.faq-button {
  width: 1.5in;
  height: 60px;
  background-color: hsla( 22.54,88.72%,61.76% ,1);
  border: none;
  border-radius: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  color: white;
  font-size: 1em;
  font-family: 'adonis-web', sans-serif;
  cursor: pointer;
}

.faq-button:hover {
  background-color: rgba(189, 107, 6, 0.81);
}

.ticket-box:hover {
  background-color: rgba(233, 206, 176, 0.263);
}

.ticket-box {
  border-radius: 5px;
  padding: 10px;
  margin-bottom: 10px;
  background-color: #ffffff;

}

.ticket-box p {
  margin: 0;
  font-family: 'Pontano Sans', sans-serif;
  font-weight: 200;
  font-size: 1em;
}

.ticket-box strong {
  color: #000000;
  font-family: 'Pontano Sans', sans-serif;
  font-weight: bold;
  font-size: 1.2em;
}

.ticket-box p:not(:first-of-type) {
  margin-top: 10px; /* Add space between subject and content */
}
</style>
