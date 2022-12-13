<template>
  <div class="home">
    <h1>Topologie Drzewa</h1>
    <h3>
      jedna z fizycznych topologii sieci komputerowych charakteryzująca się tym,
      iż jej węzły łączą się bezpośrednio, dynamicznie i niehierarchicznie z jak
      największą liczbą innych węzłów i współpracują ze sobą w celu efektywnego
      trasowania danych.
    </h3>
    <img src="../assets/tree.png" alt="topologia siatki" />
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: 'HomeView',
};
</script>
<style lang="scss" scoped>
.home {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
  padding: 2rem;
}
h1 {
  font-size: 2.8rem;
  color: #0483ff;
}
h3 {
  color: #777;
  margin: 2rem 0;
  font-size: 1.4rem;
  text-align: justify;
  line-height: 1.5;
}
img {
  height: 20rem;
}
</style>
