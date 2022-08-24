<template lang="html">
  <div class="container">
    <img src="../assets/logo.png" alt="" class="logo" />
    <img src="../assets/icon.png" alt="" class="icon" />
    <nav class="glowny">
      <router-link to="/"> Strona głowna </router-link>
      <router-link to="/"> Przeglądaj </router-link>
      <router-link to="/"> O nas </router-link>
      <button @click="logoj">Zaloguj</button>
    </nav>
  </div>
</template>
<script>
export default {
  name: 'NawigacjaStrony',
  methods: {
    logoj() {
      this.$emit('kliknaprzyciskuxd');
    },
  },
};
</script>
<style lang="scss" scoped>
$czarny: #1e1e1e;
.container {
  width: 100%;
  display: flex;
  height: 12vh;
  justify-content: space-between;
  padding: 10px 50px;
  align-items: center;
  @media screen and (max-width: 642px) {
    padding: 10px;
  }
}
.logo,
.icon {
  height: 8vh;
}
.logo {
  transition: 0.5s all;
  @media screen and (max-width: 642px) {
    display: none;
  }
}
.icon {
  display: none;
  @media screen and (max-width: 642px) {
    display: block;
  }
}
.glowny {
  a,
  button {
    transition: 0.5s all;
    text-decoration: none;
    color: $czarny;
    font-size: 24px;
    margin: 0 15px;
    @media (max-width: 1110px) {
      font-size: 14px;
      margin: 0 10px;
    }
    @media screen and (max-width: 642px) {
      font-size: 10px;
      margin: 0 5px;
    }
  }

  button {
    background-color: #fee5d4;
    padding: 15px 20px;
    border-radius: 5px;
    border: none;
    &:hover {
      background-color: #ffd2b4;
      cursor: pointer;
    }
    @media screen and (max-width: 642px) {
      padding: 10px;
    }
  }
}
</style>
