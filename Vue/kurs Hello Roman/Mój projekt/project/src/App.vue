<template>
  <div class="wrapper">
    <Bg />
    <Claim />
    <SearchInput v-model="searchValue" @input="handleSearch"/>
  </div>
</template>

<script>
  import axios from 'axios';
  import debounce from 'lodash.debounce';
  import Claim from '@/components/Claim.vue';
  import SearchInput from '@/components/SearchInput.vue';
  import Bg from '@/components/bg.vue';

  const API = 'https://images-api.nasa.gov/search?q=';

  export default {
    name: "HomeView",
    components: { 
      Claim,
      SearchInput,
      Bg,
    },
    data() {
        return {
            searchValue: "",
            results: [],
        };
    },
    methods: {
        handleSearch: debounce(function searchResponse() {
            axios.get(`${API}${this.searchValue}&media_type=image`)
                .then((response) => {
                console.log(this.searchValue)
                this.results = response.data.collection.items;
                console.log(this.results);
                this.results.length = 20;
            })
                .catch((error) => {
                console.log(error);
            });
        }, 500),
    },
    components: { Claim, SearchInput, Bg }
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
  .wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 0px;
    padding: 30px;
    width: 100%;
    height: 100vh;
    justify-content: center;
  }
</style>
