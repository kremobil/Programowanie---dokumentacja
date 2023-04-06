<template>
  <div class="home">
    <h1>Topologie sieciowe</h1>
    <h3>
      model układu połączeń różnych elementów sieci komputerowej. Określenie
      topologia sieci może odnosić się do konstrukcji fizycznej albo logicznej
      sieci. Topologia fizyczna opisuje sposoby fizycznej realizacji sieci
      komputerowej, jej układu przewodów, medium transmisyjnych.
    </h3>
    <img src="../assets/topologia-magistrali.jpg" alt="topologia magistrali" />
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
