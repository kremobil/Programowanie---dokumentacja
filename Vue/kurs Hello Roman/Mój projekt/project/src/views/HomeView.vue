<template>
  <div class="wrapper">
    <div class="search">
      <!-- eslint-disable-next-line -->
      <label for="search">Wyszukaj w Nasa</label>
      <input type="text" id="search" name="search" v-model="searchValue" @input="handleSearch">
    </div>
  </div>
</template>

<script>
import axios from 'axios';

const API = 'https://images.-api.nasa.gov/search?q=';

export default {
  name: 'HomeView',
  data() {
    return {
      searchValue: '',
    };
  },
  methods: {
    handleSearch() {
      axios.get(`${API}${this.searchValue}&media_type=image`)
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },
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
