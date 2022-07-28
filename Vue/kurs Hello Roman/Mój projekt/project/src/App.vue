<template>
<!-- eslint-disable -->
  <div :class="[{flexStart: step === 1}, 'wrapper']">
    <div class="lds-dual-ring" v-if="step === 1 && loading"></div>
    <transition name="slide">
      <img src="./assets/logo.png" class="logo" v-if="step === 1">
    </transition>
    <transition name="fade">
      <Bg v-if="step === 0"/>
    </transition>
    <Claim v-if="step === 0"/>
    <SearchInput @input="handleSearch" :dark="step === 1"/>
    <div class="results"  v-if="results && !loading && step === 1 && results.length > 0">
      <item :myvar='item' v-for="item in results" :key="item.data[0].nasa_id" @click.native="handleModalOpen(item)" />
    </div>
    <h2 class="errorMessage"  v-else-if="results.length === 0 && step === 1">Sorry we cand find it.<br />try something elese.</h2>
    
  </div>
  
  <Modal v-if="modalOpen" @closeModal="modalOpen = false" :data="modalData"/>
</template>

<script>
import axios from 'axios';
import debounce from 'lodash.debounce';
import Claim from '@/components/Claim.vue';
import SearchInput from '@/components/SearchInput.vue';
import Bg from '@/components/bg.vue';
import item from '@/components/item.vue';
import Modal from '@/components/modal.vue';

const API = 'https://images-api.nasa.gov/search?q=';

export default {
  name: 'HomeView',
  components: {
    Claim,
    SearchInput,
    Bg,
    item,
    Modal,
  },
  data() {
    return {
      loading: false,
      step: 0,
      searchValue: '',
      results: [],
      modalOpen: false,
      modalData: {},
    };
  },
  methods: {
    handleModalOpen(modalitem) {
      this.modalOpen = true;
      this.modalData = {
        title: modalitem.data[0].title,
        description: modalitem.data[0].description,
        url: modalitem.links[0].href,
      };
    },
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
  .errorMessage {
    text-align: center;
    color: rgb(255, 52, 52);
    margin-top: 70px;
    font-size: 25px;
  }
.lds-dual-ring {
  position: fixed;
  display: block;
  width: 80px;
  height: 80px;
  margin: calc(50vh - 40px) calc(50vw - 40px);
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #1e3d4a;
  border-color: #1e3d4a transparent #1e3d4a transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

</style>
