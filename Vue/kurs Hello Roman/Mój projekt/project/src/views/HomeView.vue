<template>
  <div class="wrapper">
    <Claim />
    <SearchInput />
  </div>
</template>

<script>
import axios from 'axios';
import debounce from 'lodash.debounce';
import Claim from '@/components/Claim.vue';
import SearchInput from '@/components/SearchInput.vue';

const API = 'https://images-api.nasa.gov/search?q=';

export default {
    name: "HomeView",
    components: { 
      Claim,
      SearchInput,
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
                this.results = response.data.collection.items;
                console.log(this.results);
                this.results.length = 20;
            })
                .catch((error) => {
                console.log(error);
            });
        }, 500),
    },
    components: { Claim, SearchInput }
};
</script>

<style lang="scss" scoped>
  .wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 0px;
    padding: 30px;
    width: 100%;
    height: 100vh;
    justify-content: center;
    background-image: url('../assets/background.jpg');
    background-repeat: no-repeat;
    background-size: cover;
    background-position: 80% 0%;
  }
</style>
