<template lang="html">
  <div class="leftbarwrapper">
    <div class="leftmenu">
      <router-link :to="option.router" class="leftoption" v-for="option in menu.content"
      :key="option.title">
        {{option.title}}
      </router-link>
    </div>
    <div class="leftlink">
      <div class="title">Bip</div>
      <div class="link-content">
        <a href="http://bip.edu.bydgoszcz.pl/sp46/" target="_blank">
          <img src=" http://sp46.netstrefa.pl/images/bip.jpg" alt="Bip"/>
        </a>
      </div>
    </div>
    <div class="leftlink">
      <div class="title">Edu(R)Ewolucja</div>
      <div class="link-content">
        <a href="https://www.edurewolucja.pl//" target="_blank">
          <img src="../assets/eduRewolucja.png" alt="Edu(r)Ewolucja"/>
        </a>
      </div>
    </div>
    <Transition name="fade">
      <div class="mobile-leftmenu" v-if="menu.show">
        <router-link :to="option.router" class="mobile-leftoption" v-for="option in menu.content"
        :key="option.title" @click="hidenav">
          {{option.title}}
        </router-link>
        <a href="https://www.edurewolucja.pl//" class="mobile-leftoption mobilelink" target="_blank" @click="hidenav">Edu(R)Ewolucja</a>
        <a href="http://bip.edu.bydgoszcz.pl/sp46/" class="mobile-leftoption mobilelink" target="_blank" @click="hidenav">Bip</a>
        <a href="http://sp46.netstrefa.pl/images/infolinia_1.png" class="mobile-leftoption mobilelink" target="_blank" @click="hidenav">Linia Dzieciom</a>
        <a href="https://padlet.com/agnieszkabulinska87/9iaudvf3egew" class="mobile-leftoption mobilelink" target="_blank" @click="hidenav">Szkolny Bookcrossing</a>
        <a href="https://padlet.com/smacznywf/tqn7y32whqwj" class="mobile-leftoption mobilelink" target="_blank" @click="hidenav">Jedz na zdrowie</a>
        <a href="https://oswoicpolski.blogspot.com/" class="mobile-leftoption mobilelink" target="_blank" @click="hidenav">Oswoić polski | Blog</a>
        <a href="https://www.lekkoatletykadlakazdego.pl//'" class="mobile-leftoption mobilelink" target="_blank" @click="hidenav">LA dla każdego</a>
        <a href="https://bydgoszczkarate.pl/'" class="mobile-leftoption mobilelink" target="_blank" @click="hidenav">Kyokushin Karate</a>
      </div>
    </Transition>
    <button class="mobile-expand" @click="shownav" v-if="!menu.show">Rozwiń ᐯ</button>
    <button class="mobile-expand" @click="shownav" v-else>Ukryj ᐱ</button>
  </div>
</template>
<script>
export default {
  // eslint-disable-next-line
  name: 'leftbarwrapper',
  data() {
    return {
      menu: {
        show: false,
        content: [
          { title: 'Aktualność', router: '/' },
          { title: 'O szkole', router: '/' },
          { title: 'Kadra', router: '/' },
          { title: 'Zajrzyjcie do Naszych klas', router: '/' },
          { title: 'Dokumenty szkolne', router: '/' },
          { title: 'Kalendarz roku szkolnego', router: '/' },
          { title: 'Legitymacja szkolna', router: '/' },
          { title: 'Obiady', router: '/' },
          { title: 'Samorząd szkolny', router: '/' },
          { title: 'Rada rodziców', router: '/' },
          { title: 'Ubezpieczenie', router: '/' },
          { title: 'Zajęcia dodatkowe', router: '/' },
          { title: 'Bookcrossing', router: '/' },
          { title: 'Wychowanie do życia w rodzinie', router: '/' },
          { title: 'Świetlica', router: '/' },
          { title: 'Kontakt', router: '/' },
          { title: 'Deklaracja dostępności', router: '/' },
          { title: 'RODO', router: '/' },
        ],
      },
    };
  },
  methods: {
    shownav() {
      this.menu.show = !this.menu.show;
    },
    hidenav() {
      this.menu.show = false;
    },
  },
};
</script>
<style lang="scss" scoped>
  .leftbarwrapper {
    width: 100%;
    padding: 10px;
    background-color: #808080;
    border-right: #505050 solid 1px;
    flex-direction: column;
    align-items: center;
    display: flex;
    @media (min-width: 1024px) {
      width: 15%;
    }
  }
  .mobile-expand {
    width: 80%;
    font-size: 20px;
    padding: 5px 10px;
    background-color: #444;
    color: white;
    border: 1px solid #222;
    border-radius: 3px;
    transition: all 0.5s;
    cursor: pointer;
    @media (min-width: 1024px) {
      display: none;
    }
    &:hover {
      background-color:  #333;
      border: 1px solid #111;
    }
  }
  .mobile-leftmenu {
    display: flex;
    flex-direction: column;
    width: 100%;
    align-items: center;
    @media (min-width: 768px) {
      display: grid;
      grid-template-columns: 1fr 1fr;
    }
  }
  .leftmenu{
    display: none;
    @media (min-width: 1024px) {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
  }
  .leftoption{
    text-decoration: none;
    border-top: #222 dashed 1px;
    color: #222;
    width: 90%;
    padding: 10px;
    text-align: center;
    font-weight: 600;
    transition: all 0.5s;
    &:first-child {
      border: none;
    }
    &:hover{
      background-color: #999;
      box-shadow: 0 0 10px 5px #999;
    }
  }
  .mobile-leftoption {
    width: 80%;
    border-top: #222 dashed 1px;
    padding: 8px;
    font-weight: 400;
    text-align: center;
    color: #222;
    text-decoration: none;
    transition: all 0.5s;
    &:hover{
      background-color: #666;
      box-shadow: 0 0 8px 4px #666;
    }
    &:first-child{
      border: none;
    }
    &:last-child{
      margin-bottom: 10px;
    }
    @media (min-width: 768px) {
      width: 90%;
      margin: 0 5%;
      &:nth-child(2){
        border-top: none;
      }
    }
    @media (min-width: 1024px) {
      display: none;
    }
  }
  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.5s ease;
  }

  .fade-enter-from,
  .fade-leave-to {
    opacity: 0;
  }
  .leftlink {
    display: none;
    @media (min-width: 1024px) {
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      margin-top: 15px;
    }
  }
  .leftlink .title{
    width: 100%;
    background-color: #ccc;
    border: 1px solid #808080;
    padding: 5px 20px;
    color: #303030;
    border-radius: 10px;
    letter-spacing: 1px;
    font-weight: 600;
    text-transform: uppercase;
    font-size: 14px;
    transform: scaleX(1.2);
    @media (min-width: 1600px) {
      transform: scaleX(1.15);
      font-size: 20px;
    }
  }
  .leftlink .link-content{
    width: 75%;
    padding: 10px;
    margin-top: 15px
  }
  .leftlink img{
    width: 100%;
  }
  .mobilelink{
    background-color: #213c84;
    font-weight: 600;
    border: 1px solid #142450;
    border-radius: 5px;
    margin-top: 15px;
    margin-bottom: 0;
    color: white;
    &:hover{
      background-color: #142450;
      border-color: #0a132b;
    }
    @media (min-width: 768px) {
      margin-bottom: 10px;
    }
  }
</style>
