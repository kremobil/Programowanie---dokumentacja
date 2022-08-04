<template lang="html">
  <div class="rightwrapper">
    <div class="rightlink">
      <div class="title">Linia Dzieciom</div>
      <div class="link-content">
        <a href="http://sp46.netstrefa.pl/images/infolinia_1.png" target="_blank">
          <img src="../assets/infolinia_1.png" alt="infolninia przeciw depresji"/>
        </a>
      </div>
    </div>
    <div class="rightlink">
      <div class="title">Szkolny Bookcrossing</div>
      <div class="link-content">
        <a href="https://padlet.com/agnieszkabulinska87/9iaudvf3egew" target="_blank">
          <img src="../assets/pp.png" alt="Bookcrossing"/>
        </a>
      </div>
    </div>
    <div class="rightlink">
      <div class="title">Jedz na zdrowie</div>
      <div class="link-content">
        <a href="https://padlet.com/smacznywf/tqn7y32whqwj" target="_blank">
          <img src="../assets/zzzd.png" alt="zdrowe żywienie"/>
        </a>
      </div>
    </div>
    <div class="rightlink">
      <div class="title">Oswoić polski</div>
      <div class="link-content">
        <a href="https://oswoicpolski.blogspot.com/" target="_blank">
          <img src="../assets/blo.png" alt="Blog"/>
        </a>
      </div>
    </div>
    <div class="rightlink">
      <div class="title">LA dla każdego</div>
      <div class="link-content">
        <a href="https://www.lekkoatletykadlakazdego.pl//'" target="_blank">
          <img src="../assets/ldk.png" alt="Lekko ateltyka dla każdego"/>
        </a>
      </div>
    </div>
    <div class="rightlink">
      <div class="title">Kyokushin Karate</div>
      <div class="link-content">
        <a href="https://bydgoszczkarate.pl/'" target="_blank">
          <img src="../assets/bydgoszcz-karate.png" alt="Lekko ateltyka dla każdego"/>
        </a>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  // eslint-disable-next-line
  name: 'rightbar',
};
</script>
<style lang="scss" scoped>
  .rightwrapper {
    display: none;
    @media (min-width: 1024px) {
      width: 15%;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 10px;
      background-color: #808080;
      border-left: #505050 solid 1px;
    }
  }
  .rightlink {
    display: none;
    @media (min-width: 1024px) {
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      margin-top: 15px;
    }
  }
  .rightlink .title{
    width: 100%;
    background-color: #ccc;
    border: 1px solid #808080;
    padding: 5px 20px;
    color: #303030;
    border-radius: 10px;
    letter-spacing: 1px;
    font-weight: 600;
    text-transform: uppercase;
    font-size: 14px;
    transform: scaleX(1.2);
    text-align: right;
    @media (min-width: 1600px) {
      transform: scaleX(1.15);
      font-size: 20px;
    }
  }
  .rightlink .link-content{
    width: 75%;
    padding: 10px;
    margin-top: 15px
  }
  .rightlink img{
    width: 100%;
    height: auto;
  }
</style>
