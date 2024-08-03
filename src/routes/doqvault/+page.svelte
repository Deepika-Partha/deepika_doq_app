<script>
 
</script>

<main class="custom-background">
    <div class="header-image">
        <!-- svelte-ignore a11y-img-redundant-alt -->
        <img src="https://images.squarespace-cdn.com/content/v1/64ba92ff4c24fe41a3c67b1d/1689953074945-9WI8FKUEAOY9HQX8636Q/Sleek+Objects+1.jpg" alt="Header Image">
        <div class="header-text">qBotica</div>
        <div class="header-text2">DoqVault</div>
    </div>
    <div class="button-container">
        <button class="upload-button">Upload Document</button>
    </div>

    <div class="myDocuments-box">
              <div class="docs-box">
              </div>
    </div>

    <div class="myPages-box">
        <div class="pages-box">
            <div class="addPageButton-container">
                <a href="/account" class="addPage-button">Create a Page</a>
            </div>
        </div>
    </div>

</main>

<style>
    @font-face {
      font-family: 'adonis-web';
      font-style: normal;
      font-weight: 400;
      src: url(https://use.typekit.net/pf/ss/qdyr/n4/l?subset_id=2&primer=9f562d6ca39adae019ef00367c3f3deae3c8627f22e3b025ba425fbc2aac6431&fvd=n4&ec_token=BInhlQ%2Bl4i%2FTK2LNzmpe2QC%2Bdl6Qc7iJa15oy7OfSGK%2BY7lwDRam4FlQCIzQGEqAiJZo10MshaDLZWgX%2FckdPK0bOW%2FAfpkj2O5MO1d7Aul7v1RGoa7OBxfdciGAxZqjHAPKKo0fqkxxKF%2F9mM9JjA%3D%3D) format("woff2"), url(https://use.typekit.net/pf/ss/qdyr/n4/d?subset_id=2&primer=9f562d6ca39adae019ef00367c3f3deae3c8627f22e3b025ba425fbc2aac6431&fvd=n4&ec_token=BInhlQ%2Bl4i%2FTK2LNzmpe2QC%2Bdl6Qc7iJa15oy7OfSGK%2BY7lwDRam4FlQCIzQGEqAiJZo10MshaDLZWgX%2FckdPK0bOW%2FAfpkj2O5MO1d7Aul7v1RGoa7OBxfdciGAxZqjHAPKKo0fqkxxKF%2F9mM9JjA%3D%3D) format("woff"), url(https://use.typekit.net/pf/ss/qdyr/n4/a?subset_id=2&primer=9f562d6ca39adae019ef00367c3f3deae3c8627f22e3b025ba425fbc2aac6431&fvd=n4&ec_token=BInhlQ%2Bl4i%2FTK2LNzmpe2QC%2Bdl6Qc7iJa15oy7OfSGK%2BY7lwDRam4FlQCIzQGEqAiJZo10MshaDLZWgX%2FckdPK0bOW%2FAfpkj2O5MO1d7Aul7v1RGoa7OBxfdciGAxZqjHAPKKo0fqkxxKF%2F9mM9JjA%3D%3D) format("opentype");
      font-weight: 400;
      font-style: normal;
    }
    
    @font-face {
      font-family: 'Pontano Sans';
      font-style: normal;
      font-weight: 400;
      src: url(https://fonts.googleapis.com/css2?family=Pontano+Sans:wght@400;700) format('woff2');
      unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
    }
    
    :global(body) {
      background-color: #ffffff;
      margin: 0;
      padding: 0;
      font-family: 'Pontano Sans', sans-serif;
    }
    
    main.custom-background {
      background-color: #E9CEB0;
      display: flex;
      flex-direction: column;
      align-items: center;
      max-width: 100%;
      margin: 0 auto;
      padding: 2vh 1vw;
      overflow: hidden;
      height: 120vh;
    }
    
    .header-image {
      width: 91vw;
      height: 30vh;
      overflow: hidden;
      margin: 0 auto;
      position: relative;
      display: flex;
      justify-content: center;
      align-items: center;
      text-align: center;
    }
    
    .header-image img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    
    .header-text {
      position: absolute;
      top: 2vh;
      left: 2vw;
      color: white;
      font-family: 'adonis-web', sans-serif;
      font-size: 2vw;
    }
    
    .header-text2 {
      position: absolute;
      top: 7vh;
      left: 30vw;
      color: white;
      font-family: 'adonis-web', sans-serif;
      font-size: 7vw;
    }
    
    .button-container {
      display: flex;
      justify-content: center;
      width: 100%;
      margin-top: 4vh;
    }

    .upload-button {
        background-color: hsla( 22.54,88.72%,61.76% ,1);
        border: none;
        border-radius: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
        color: white;
        font-size: 1.2em;
        font-family: 'adonis-web', sans-serif;
        cursor: pointer;
        height: 60px;
        width: 200px;
        padding: 40px;

    }

    .upload-button:hover {
      background-color: rgba(189, 107, 6, 0.81);
    }

    .myDocuments-box {
    width: 10in;
    min-height: 200px;
    padding: 20px;
    margin: 40px auto; 
    background-color: rgb(255, 255, 255);
    color: black;
    display: block; 
    font-family: 'adnois-web', sans-serif;
    /* display: none; */
  }

  .myPages-box {
    width: 10in;
    min-height: 200px;
    padding: 10px;
    background-color: rgb(255, 255, 255);
    color: black;
    display: block; 
    font-family: 'adnois-web', sans-serif;
    /* display: none; */
  }

  .addPageButton-container {
      display: flex;
      width: 100%;
      margin-top: 1.5vh;
      margin-bottom: 1.5vh;
      margin-left: 1.5vh;
    }

    .addPage-button {
        background-color: hsla(22.54, 88.72%, 61.76%, 1);
        border: none;
        border-radius: 20px;
        display: flex;
        align-items: center;
        justify-content: center; 
        color: white;
        font-size: 1.2em;
        font-family: 'adonis-web', sans-serif;
        cursor: pointer;
        padding: 60px 20px;
        max-width: 100%;
        max-height: 100%;
        box-sizing: border-box;
        text-align: center; 
        width: auto; 

    }

    .addPage-button:hover {
      background-color: rgba(189, 107, 6, 0.81);
    }

</style>

    



