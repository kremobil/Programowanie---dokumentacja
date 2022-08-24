<template>
  <div class="wrapper">
    <nav>
      <router-link to="/" class="logo">
        <img src="./assets/logo_title.png" alt="logo" />
      </router-link>
      <div class="nav-lins">
        <font-awesome-icon
          icon="fa-regular fa-circle-user"
          class="icon"
          @click="showSideaccount"
        />
        <font-awesome-icon
          icon="fa-solid fa-cart-shopping"
          class="icon"
          @click="showSidebasket"
        />
        <font-awesome-icon
          icon="fa-solid fa-bars"
          class="icon"
          @click="showSidemenu"
        />
      </div>
      <transition name="sidebar">
        <div
          class="sidebar"
          v-if="sidebar.menu || sidebar.basket || sidebar.account"
        >
          <div class="options" v-if="sidebar.menu">
            <router-link
              :to="option.route"
              class="sidebarnav"
              v-for="option in menu"
              :key="option.title"
            >
              {{ option.title }}
            </router-link>
          </div>
          <BasketSidebar v-if="sidebar.basket" />
        </div>
      </transition>
    </nav>
  </div>
</template>

<script>
import BasketSidebar from './components/BasketSidebar.vue';

export default {
  name: 'app',
  methods: {
    showSidemenu() {
      this.sidebar.menu = !this.sidebar.menu;
      this.sidebar.basket = false;
      this.sidebar.account = false;
    },
    showSidebasket() {
      this.sidebar.menu = false;
      this.sidebar.basket = !this.sidebar.basket;
      this.sidebar.account = false;
    },
    showSideaccount() {
      this.sidebar.menu = false;
      this.sidebar.basket = false;
      this.sidebar.account = !this.sidebar.account;
    },
  },
  data() {
    return {
      sidebar: {
        menu: false,
        basket: false,
        account: false,
      },
      menu: [
        { title: 'Strona Główna', route: '/' },
        { title: 'Kategorie', route: '/categories' },
        { title: 'O nas', route: '/about' },
        { title: 'Kontakt', route: '/contact' },
      ],
    };
  },
  components: { BasketSidebar },
};
</script>

<style lang="scss">
$gray: #2a3442;
$main-pink: #e6345b;
$mid-light: #a5a5a5;
$light: #d9d9d9;
$green: #748400;

* {
  box-sizing: border-box;
  padding: 0;
  margin: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  display: flex;
  align-items: center;
  width: 100%;
  flex-direction: column;
}
.wrapper {
  width: 100%;
}
nav {
  background-color: $light;
  display: flex;
  align-items: center;
  justify-content: space-around;
  height: 8vh;

  .icon {
    margin: 0 20px;
    height: 3vh;
    color: $main-pink;
    transition: all 0.5s;

    @media (min-width: 768px) {
      margin: 0 30px;
    }

    @media (min-width: 1024px) {
      margin: 0 50px;
    }

    &:hover {
      color: $gray;
      cursor: pointer;
    }
  }
}
.logo {
  img {
    height: 6vh;
  }
}
.sidebar {
  position: absolute;
  width: 100%;
  height: 92vh;
  background-color: $mid-light;
  top: 8vh;
  right: 0;
  display: flex;
  padding: 20px;
  justify-content: center;
  @media (min-width: 1024px) {
    width: 35%;
  }
  .options {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    width: 80%;
    @media (min-width: 768px) {
      width: 60%;
    }
  }
  .sidebarnav {
    text-decoration: none;
    color: $gray;
    font-size: 24px;
    border: 2px solid $main-pink;
    border-radius: 5px;
    padding: 5px 20px;
    transition: all 0.5s;
    background-color: $main-pink;
    color: $light;
    @media (min-width: 768px) {
      padding: 15px 30px;
    }

    &:hover {
      transform: scale(1.1);
    }
  }
}

//transition sidebar
.sidebar-enter-active {
  transition: all 0.5s linear;
}

.sidebar-leave-active {
  transition: all 0.5s linear;
}

.sidebar-enter-from,
.sidebar-leave-to {
  opacity: 0;
  @media (min-width: 1024px) {
    transform: translateX(100%);
  }
}
</style>
