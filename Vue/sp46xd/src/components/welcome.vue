<template lang="html">
  <div class="welcomewrapper">
    <h2>Witamy!</h2>
    <p>Witaj na stronie Szkoły Podstawowej Nr 46 im. Unii Europejskiej z Oddziałami
       Dwujęzycznymi w Bydgoszczy</p>
  </div>
</template>
<script>
export default {
  // eslint-disable-next-line
  name: "welcome",
};
</script>
<style lang="scss" scoped>
  .welcomewrapper {
    width: 100%;
    padding: 10px;
    background-color: #f3dc02;
    border: #beab00 solid 1px;
    border-radius: 10px;
    text-align: center;
    h2{
      color: #202020;
      margin: 0;
      font-size: 28px;
      letter-spacing: 2px;
      font-weight: 700;
    }
    p{
      margin: 0;
      font-size: 18px;
      color: #213c84;
    }
  }
</style>
