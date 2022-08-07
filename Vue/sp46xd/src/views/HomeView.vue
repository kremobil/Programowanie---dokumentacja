<template>
  <div class="home">
    <Welcome />
    <img alt="Vue logo" src="../assets/logo.png">
    <router-link to="/about">About</router-link>
  </div>
</template>

<script>
import Welcome from '@/components/welcome.vue';
// @ is an alias to /src

export default {
  name: 'HomeView',
  components: {
    Welcome,
  },
};
</script>

<style lang="scss" scoped>
  .home {
    transition: all 0.5s;
    width: 100%;
    @media (min-width: 1024px) {
      width: 90%;
    }
  }
</style>
