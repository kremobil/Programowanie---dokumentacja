<template>
  <div class="wrapper">
    <div class="search">
      <!-- eslint-disable-next-line -->
      <label for="search">Wyszukaj w Nasa</label>
      <input type="text" id="search" name="search" v-model="searchValue" @input="handleSearch">
    </div>
    <div class="images">
      <a v-for="item in results" :key="item.data[0].nasa_id" :href="item.links[0].href">
        <img :src="item.links[0].href" :alt="item.data[0].description"/>
      </a>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import debounce from 'lodash.debounce';

const API = 'https://images-api.nasa.gov/search?q=';

export default {
  name: 'HomeView',
  data() {
    return {
      searchValue: '',
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
  }
  .search {
    display: flex;
    flex-direction: column;
    width: 250px;
  }
  label {
    font-family: Montserrat, sans-serif;
  }
  input {
    height: 30px;
    border: 0;
    border-bottom: 1px solid black;
  }
</style>
