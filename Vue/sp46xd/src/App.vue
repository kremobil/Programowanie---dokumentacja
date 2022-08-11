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
    <div class="content">
      <Leftbar class="leftbar"/>
      <div class="site-view">
        <router-view />
      </div>
      <Rightbar />
    </div>
    <div class="footer">
      <div class="footerlinks">
        <a href="http://www.helpline.org.pl/" target="_blank">
          <img src=" http://sp46.netstrefa.pl/GIMNAZJUM16/images/helpline140x49.gif" alt="hlepline.org" />
        </a>
        <a href="http://www.bezpiecznyinternet.org/?s=certyfikat&cat=6&id=1228" target="_blank">
          <img src=" http://sp46.netstrefa.pl/GIMNAZJUM16/images/spd_150x75.gif" alt="strona przyjazna dzieciom" />
        </a>
        <a href="http://www.dzieckowsieci.fdn.pl/" target="_blank">
          <img src="  http://sp46.netstrefa.pl/GIMNAZJUM16/images/dziecko w sieci b.jpg" alt="dzieckow sieci" />
        </a>
        <a href="http://www.116111.pl/" target="_blank">
          <img src=" http://sp46.netstrefa.pl/GIMNAZJUM16/images/TELEFON ZAUFANIA.gif " alt="116111.pl" />
        </a>
      </div>
      <h3>
        SZKOŁA PODSTAWOWA NR 46 W BYDGOSZCZY IM. UNII EUROPEJSKIEJ ul. Kombatantów 2, 85-829
        Bydgoszcz<br /> tel.: 52 361 03 22<br /><br />
        Copyright © Wiktor Fajkowski 2022
      </h3>
    </div>
    <!-- <router-view/> -->
  </div>
</template>

<script>
import Leftbar from './components/leftbar.vue';
import Rightbar from './components/rightbar.vue';

export default {
  components: {
    Leftbar,
    Rightbar,
  },
};
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
  .footer {
    width: 100%;
    display: flex;
    flex-direction: column;
    background-color: #404040;
    border-top: #202020 solid 2px;
    align-items: center;
  }
  .footerlinks {
    width: 100%;
    display: grid;
    justify-content: center;
    grid-gap: 10px;
    padding: 15px 0;
    @media (min-width: 768px) {
      grid-template-columns: 1fr 1fr;
    }
    @media (min-width: 1024px) {
      grid-template-columns: 1fr 1fr 1fr 1fr;
      width: 70%;
    }
  }
  .footer img{
    margin: 0 10%;
    width: 80%;
    height: 100px;
    border: 1px solid #202020;
    border-radius: 10px;
  }
  .footer h3{
    color: white;
    text-align: center;
    margin: 5px 10%;
    font-size: 16px;
  }
  .content {
    width: 100%;
    min-height: 800px;
    display: flex;
    flex-direction: column;
    @media (max-width: 1024px) {
      align-items: center;
    }
    @media (min-width: 1024px) {
      flex-direction: row;
    }
  }
  .site-view {
    transition: all 0.5s;
    width: 100%;
    background-color: #fff;
    padding: 20px 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    @media (min-width: 768px) {
      width: 90%;
      padding: 25px;
    }
    @media (min-width: 1024px) {
      width: 70%;
      background-color: #ddd;
      padding: 25px;
    }
  }
</style>
