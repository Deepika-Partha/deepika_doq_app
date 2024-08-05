<script>
  import { goto } from '$app/navigation';

  let pineconeKey = '';
  let hubspotKey = '';
  let dictionary = {};
  let message = ''; // Variable to hold validation messages
  let messageType = ''; // Variable to differentiate between error and success messages

  async function fetchTickets(hubspotKey, pineconeKey) {
    try {  

      document.getElementById('loading-indicator').style.display = 'block';
      
      // Remove existing error container if present before making a new request
      const existingErrorContainer = document.getElementById('error-container');
      if (existingErrorContainer) {
          existingErrorContainer.remove();
      }

      const response = await fetch('https://doq-vault-app2.onrender.com/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
         
        body: JSON.stringify({ hubspotKey: hubspotKey, pineconeKey: pineconeKey })
      });

      if (!response.ok) {
        throw new Error('Invalid key was provided ' + response.statusText);
      }

      const data = await response.json();
      console.log(data);

      // Hide loading indicator
      document.getElementById('loading-indicator').style.display = 'none';

      goto('/doqQuery');

      // In case the data returned is needed
      return data;

    } catch (error) {
      console.error('Error occurred:', error.message);

      // Hide loading indicator
      document.getElementById('loading-indicator').style.display = 'none';

      // Error container: This is positioned at the bottom of the user's screen
      const errorContainer = document.createElement('div');
      errorContainer.id = 'error-container'; // ID to identify the container, this helps clear error message if error is resolved
      errorContainer.style.position = 'fixed';
      errorContainer.style.bottom = '0';
      errorContainer.style.left = '0';
      errorContainer.style.width = '100%';
      errorContainer.style.backgroundColor = '#ce2c30';
      errorContainer.style.color = 'white';
      errorContainer.style.textAlign = 'center';
      errorContainer.style.padding = '10px';
      errorContainer.style.zIndex = '1000';
      errorContainer.innerText = `Error: ${error.message}`;
      document.body.appendChild(errorContainer);
    }
  }

  function handleSubmit() {
    message = '';
    messageType = '';

    let errors = [];

    //  Validations to ensure user information is provided
    if (!pineconeKey.trim()) {
      errors.push("Pinecone Key. ");
    }

    if (!hubspotKey.trim()) {
      errors.push("HubSpot key. ");
    }

    if (errors.length > 0) {
      message = "Form submission failed. Review the following information: " + errors.join(' ');
      messageType = 'error';
      return;
    }

    // IMPORTANT: The keys get stored in a dictionary called dictionary
    dictionary = {
      pineconeKey: pineconeKey,
      hubspotKey: hubspotKey,
    };

    sessionStorage.setItem('dictionary', JSON.stringify(dictionary));
    console.log(dictionary); 

    fetchTickets(dictionary.hubspotKey, dictionary.pineconeKey);
  }
</script>

<main class="custom-background">

  <div id="loading-indicator" class="loading-indicator">
    <img src="/spinner.gif" alt="Loading..." />
  </div>

  <div class="header-image">
    <!-- svelte-ignore a11y-img-redundant-alt -->
    <img src="https://images.squarespace-cdn.com/content/v1/64ba92ff4c24fe41a3c67b1d/1689953074945-9WI8FKUEAOY9HQX8636Q/Sleek+Objects+1.jpg" alt="Header Image">
     
    <div class="header-text">qBotica</div>
    <div class="header-text2">Connect to HubSpot</div>

    <div class="doqvault">
      <a href="/doqvault" class="doqvault-button">Redirect to DoqVault</a>
    </div>
  </div>

  <h1>Enter the required information below to allow DoqVault to access tickets from your own personal Hubspot account.</h1>

  {#if message}
    <div class={messageType === 'error' ? 'error-message' : 'success-message'}>
      {message}
    </div>
  {/if}

  <div class="header-container">
    <h2>Pinecone API Key</h2>
  </div>
  
  <div class="pinecone-container">
    <input 
      type="password" 
      bind:value={pineconeKey}
      class="pinecone-input"
    />
  </div>

  <div class="hubspot-container">
    <h4>Hubspot API Key</h4>
  </div>

  <div class="hubspot-container">
    <input 
      type="password" 
      bind:value={hubspotKey}
      class="hubspot-input"
    />
  </div>

  <div class="center-button-wrapper">
    <button on:click={handleSubmit} class="submit-button">SEND</button>
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
    src: url(https://fonts.googleapis.com/css2?family=Pontano+Sans:wght@400;700) format('woff2');
    unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
  }
  
  /* Deepika's chosen background-color: #E9CEB0; */
  
  :global(body) {
    background-color: #ffffff; 
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
    height: 15in;
  }
  
  main {
    max-width: 100%; 
    margin: 0 auto;
    padding: 20px;
    color: white;
    overflow: hidden;
    /* height: auto; */
  } 
  
  .header-image {
    width: 100vw; 
    height: 6in; 
    overflow: hidden;
    margin: 0;
    position: relative; 
  }
  
  .header-image img {
    position: absolute; 
    top: 50%; 
    left: 42%;
    width: 100vw; 
    height: auto; 
    min-height: 100%; 
    object-fit: cover;
    object-position: center; 
    transform: translate(-50%, -50%); 
    display: block; 
  }
  
  .header-text {
    position: absolute;
    top: 10px;
    left: 10px;
    color: white;
    font-family: 'adonis-web', sans-serif;
    font-size: 2em;
  }

  .header-text2 {
    position: absolute;
    top: 250px;
    left: 300px;
    color: white;
    font-family: 'adonis-web', sans-serif;
    font-size: 5em;
  }
  
  .doqvault {
    position: absolute;
    top: 10px;
    right: 130px; 
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
    text-align: center;
    line-height: 1.2;
  }
  
  .doqvault-button:hover {
    background-color: rgba(189, 107, 6, 0.81);
  }
    
  h1 {
    text-align: center;
    color: black;
    font-family: 'Pontano Sans', sans-serif;
    font-weight: 10;
    font-size: 18px;
    letter-spacing: 1px;
    margin-top: 120px; 
    margin-bottom: 100px;
    width: 650px;
    margin-left: auto; 
    margin-right: auto; 
    line-height: 2;
  }
  
  .header-container {
    display: flex; 
    align-items: baseline;
    font-size: 1em;
    font-weight: 100;
    margin-bottom: 10px;
    margin-left: 360px;
  }
  
  h2 {
    color: rgba(0, 0, 0, 0.954);
    font-family: 'Pontano Sans', sans-serif;
    margin: 0; 
    font-size: 1em;
    font-weight: 100;
    margin-right: 0px; 
    margin-top: 30px;
  }
  
  .pinecone-container {
    display: flex;
    justify-content: center;
    align-items: baseline; 
    font-size: 1em;
    font-weight: 100;
    margin-bottom: 10px;
    margin-left: .08in;
    color: black;  
    /* width: 50vw;  */
  }
  
  .pinecone-input {
    width: 627px;
    height: 60px;
    padding: 10px;
    font-size: 16px;
    font-family: 'Pontano Sans', sans-serif;
    font-weight: 100;
    border: 1px solid rgb(0, 0, 0); 
    border-radius: 30px;
    outline: none;
    background-color: #E9CEB0;
    color: black;
    transition: placeholder-color 0.3s ease; 
  }
  
  .pinecone-input:hover {
    background-color: rgba(255, 255, 255, 0.5); 
  }
  
  h4 {
    font-size: 1em;
    font-weight: 100;
    margin-right: 520px; 
    margin-top: 30px;
  }
  
  .hubspot-container {
    display: flex;
    justify-content: center;
    align-items: baseline; 
    font-size: 1em;
    font-weight: 100;
    margin-bottom: 10px;
    margin-left: .08in;
    color: black;  
    /* width: 50vw;  */
  }

  .hubspot-input {
    width: 627px;
    height: 60px;
    padding: 10px;
    font-size: 16px;
    font-family: 'Pontano Sans', sans-serif;
    font-weight: 100;
    border: 1px solid rgb(0, 0, 0); 
    border-radius: 30px;
    outline: none;
    background-color: #E9CEB0;
    color: black;
    transition: placeholder-color 0.3s ease; 
  }

  .hubspot-input:hover {
    background-color: rgba(255, 255, 255, 0.5);
  }
  
  .submit-button {
    width: 1.4in;
    height: 85px;
    background-color: rgb(0, 0, 0);
    border-radius: 50px;
    color: white;
    padding: 10px 15px;
    cursor: pointer;
    outline: none;
    margin-top: 20px;
    font-family: 'Pontano Sans', sans-serif;
    font-weight: 10;
    font-size: 18px;
    letter-spacing: 0.15em;
  }
  
  .center-button-wrapper {
    display: flex;
    justify-content: center;
    margin-left: -5in;
  }
  
  .submit-button:hover {
    background-color: rgba(189, 107, 6, 0.81);
  }
  
  .error-message::before {
    content: " ⓘ "; 
    position: absolute;
    left: 15px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 20px;
  }
  
  .error-message {
    color: white;
    background-color: #ce2c30;
    text-align: center;
    margin-top: 10px;
    font-family: 'Pontano Sans', sans-serif;
    font-size: 17px;
    font-weight: 10;
    padding: 10px 50px 50px 40px;
    border-radius: 25px; 
    width: 590px;
    height: 70px;
    margin-left: auto;
    margin-right: auto; 
    margin-block-start: 1em;
    margin-block-end: 3em;
    position: relative;
  }
  
  .success-message {
      color: green;
      text-align: center;
      margin-top: 10px;
      font-size: 18px;
    }

  .loading-indicator {
  position: fixed;
  top: calc(50% + 20px);
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 1000;
  display: none; /* Initially hidden */
}

.loading-indicator img {
  width: 150px; /* Adjust as needed */
  height: auto;
}
  

</style>