<template>
  <div class="home">
    <h1>Topologie Gwiadzy</h1>
    <h3>
      sposób połączenia urządzeń w sieci komputerowej charakteryzujący się tym,
      że kable sieciowe od wszystkich urządzeń końcowych zbiegają się w jednym
      wspólnym punkcie, zwanym punktem dostępu, w którym znajduje się
      koncentrator lub przełącznik sieciowy.
    </h3>
    <img src="../assets/satr.png" alt="topologia gwiazdy" />
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
