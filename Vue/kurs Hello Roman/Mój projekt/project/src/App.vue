<template>
<!-- eslint-disable -->
  <div :class="[{flexStart: step === 1}, 'wrapper']">
    <transition name="slide">
      <img src="./assets/logo.png" class="logo" v-if="step === 1">
    </transition>
    <transition name="fade">
      <Bg v-if="step === 0"/>
    </transition>
    <Claim v-if="step === 0"/>
    <SearchInput @input="handleSearch" :dark="step === 1"/>
    <div class="results"  v-if="results && !loading && step === 1">
      <item :myvar='item' v-for="item in results" :key="item.data[0].nasa_id" />
      {{ item }}
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import debounce from 'lodash.debounce';
import Claim from '@/components/Claim.vue';
import SearchInput from '@/components/SearchInput.vue';
import Bg from '@/components/bg.vue';
import item from '@/components/item.vue';

const API = 'https://images-api.nasa.gov/search?q=';

export default {
  name: 'HomeView',
  components: {
    Claim,
    SearchInput,
    Bg,
    item,
  },
  data() {
    return {
      loading: false,
      step: 0,
      searchValue: '',
      results: [],
    };
  },
  methods: {
    handleSearch: debounce(function searchResponse(inputvalue) {
      this.loading = true;
      axios.get(`${API}${inputvalue.originalTarget.value}&media_type=image`)
        .then((response) => {
          this.results = response.data.collection.items;
          // console.log(`${API}${inputvalue.originalTarget.value}&media_type=image`);
          // console.log(this.results);
          // this.results.length = 20;
          this.loading = false;
          this.step = 1;
        })
        .catch((error) => {
          console.log(error);
        });
    }, 500),
  },
};
</script>

<style lang="scss">
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;800&display=swap');

  body {
    font-family: 'Montserrat', sans-serif;
    margin: 0;
    padding: 0;
  }
  * {
    box-sizing: border-box;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }
  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.5s ease;
  }

  .fade-enter-from,
  .fade-leave-to {
    opacity: 0;
  }
  .slide-enter-active,
  .slide-leave-active {
    transition: margin-top 0.5s ease;
  }

  .slide-enter-from,
  .slide-leave-to {
    margin-top: -50px;
  }

  .wrapper {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 0px;
    padding: 30px;
    width: 100%;
    height: 100vh;
    justify-content: center;

    &.flexStart {
      justify-content: flex-start;
    }
  }

  .logo {
    position: absolute;
    top: 40px;
  }
  .results{
    margin-top: 50px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-gap: 20px;

    @media (min-width: 768px) {
      grid-template-columns: 1fr 1fr 1fr;
    }
    @media (min-width: 1024px) {
      grid-template-columns: 1fr 1fr 1fr 1fr;
    }
  }
</style>
