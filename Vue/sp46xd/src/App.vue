<template>
  <div class="wrapper">
    <router-link to="/">
      <img src="./assets/sp46logo.png" alt="Logo Szkoły" class="logo"/>
    </router-link>
    <div class="mainmenu">
      <router-link to="/" class="option">Dziennik elektroniczny</router-link>
      <router-link to="/" class="option">Plan lekcji</router-link>
      <router-link to="/" class="option">Szkolny FB</router-link>
      <router-link to="/" class="option">Doradztwo zawodowe</router-link>
      <router-link to="/" class="option">Klasy językowe</router-link>
      <router-link to="/" class="option">E-twinning</router-link>
      <router-link to="/" class="option">Realizowane projekty</router-link>
      <router-link to="/" class="option">Edu(R)Ewolucja</router-link>
      <router-link to="/" class="option">Sukcesy</router-link>
      <router-link to="/" class="option">Pedagog szkolny</router-link>
      <router-link to="/" class="option">Informacje dla rodziców</router-link>
      <router-link to="/" class="option">Informator dla klas 8</router-link>
      <router-link to="/" class="option">Wyprawka Pierwszaka</router-link>
      <router-link to="/" class="option">Rekrutacja 2022/2023</router-link>
      <router-link to="/" class="option">Szkoła kompetencji</router-link>
      <router-link to="/" class="option">Zadanie Planowanie</router-link>
    </div>
    <!-- <router-view/> -->
  </div>
</template>

<script>

</script>

<style lang="scss">
  @import url('https://fonts.googleapis.com/css2?family=Mukta+Malar:wght@200;400;600;700&display=swap');

  * {
    box-sizing: border-box;
  }
  body {
    margin: 0 !important;
    font-family: 'Mukta Malar', sans-serif;
  }
  .wrapper  {
    display: flex;
    flex-direction: column;
    width: 100%;
    align-items: center;
    justify-content: flex-start;
  }
  .logo {
    transition: all 0.5s;
    width: 100%;
    @media (min-width: 600px) {
      width: 500px;
    }
    @media (min-width: 1921px) {
      width: 700px;
    }
  }
  .mainmenu {
    border-top: #1a2f68 solid 2px;
    border-bottom: #1a2f68 solid 2px;
    width: 100%;
    background-color: #213c84;
    padding: 10px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-gap: 10px;
    @media (min-width: 768px) {
      grid-template-columns: 1fr 1fr 1fr 1fr;
    }
    @media (min-width: 1260px) {
      grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr;
    }
  }
  .option{
    width: 80%;
    margin: 0 10%;
    border-radius: 3px;
    padding: 5px;
    background-color: #f3dc02;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    color: #202020;
    text-decoration: none;
    font-weight: 600;
    border: #beab00 solid 1px;
    transition: all 0.5s;
  }
  .option:hover {
    background-color: #beab00;
    border: #928400 solid 1px;
  }
</style>
