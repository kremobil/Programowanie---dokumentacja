<template>
  <div class="home">
    <h1>Topologie Pierścienia</h1>
    <h3>
      jedna z fizycznych topologii sieci komputerowych. Komputery połączone są
      za pomocą jednego nośnika informacji w układzie zamkniętym – okablowanie
      nie ma żadnych zakończeń. W ramach jednego pierścienia można stosować
      różnego rodzaju łącza.
    </h3>
    <img src="../assets/ring.png" alt="topologia pierścienia" />
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
