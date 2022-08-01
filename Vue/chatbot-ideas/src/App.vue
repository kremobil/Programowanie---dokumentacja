<template>
  <div class="wrapper">
    <h1>Przykładowa strona</h1>
    <div class="menu">
      <div class="menuoption">
        Strona Główna
      </div>
      <div class="menuoption">
        Cennik
      </div>
      <div class="menuoption">
        O nas
      </div>
    </div>
    <div class="content">
      <Chatbot/>
    </div>
    <div class="footer">
      &copy; Wiktor Fajkowski 2022
    </div>
  </div>
</template>

<script>
import Chatbot from './components/chatbot.vue';

export default {
  name: 'App',
  components: {
    Chatbot,
  },
};
</script>

<style lang="scss">
  * {
    box-sizing: border-box;
  }
  body {
    margin: 0;
  }
  .wrapper {
    display: flex;
    width: 100%;
    height: 100vh;
    justify-content: flex-start;
    flex-direction: column;
    align-items: center;
  }
  .menu {
    width: 100%;
    padding: 10px;
    background-color: #505050;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: space-around;
    font-size: 24px;
    text-align: center;
    cursor: pointer;
    @media (min-width: 768px) {
      flex-direction: row;
      justify-content: space-around;
      align-items: center;
    }
  }
  .menuoption {
    padding: 10px 40px;
    background-color: azure;
    border-radius: 3px;
    transition: all 0.5s;
    margin: 10px 25px;

    @media (min-width: 768px) {
      margin: 0;
    }

    @media (min-width: 1024px) {
      letter-spacing: 1px;
      padding: 15px 60px;
      font-size: 28px;
    }
  }
  .menuoption:hover{
    background-color: rgb(128, 255, 255);
    box-shadow: 5px 5px 15px -5px rgba(azure, .8);
  }
  .content {
    width: 100%;
    min-height: 800px;
    background-color: rgba(black, .3);
    transition: all 0.5s;
    @media (min-width: 768px) {
      width: 80%;
      box-shadow: 0px 0px 50px 3px rgba(black, .3);
      z-index: 0;
    }
  }
  .footer {
    width: 100%;
    background-color: #303030;
    color:white;
    text-align: center;
    padding: 30px;
    transition: all 0.5s;
    @media (min-width: 768px) {
      padding: 50px;
      font-size: 24px;
    }
  }
</style>
