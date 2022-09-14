<template>
  <div class="home">
    <HomeSlider />
  </div>
</template>

<script>
import HomeSlider from '../components/HomeSlider.vue';
// @ is an alias to /src

export default {
  name: 'HomeView',
  components: { HomeSlider },
};
</script>

<style lang="scss">
.home {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
