<template lang="html">
  <div class="postwrapper">
    <div class="postdata">
      <div class="posttitle">{{item.title}}</div>
      <div class="postinfo">📅 {{item.upload}} 👩 {{item.author}}</div>
    </div>
    <div class="postcontent">
      <div class="texts" v-if="item.tekst">
        {{item.textContent}}
      </div>
      <div class="images">
        <a v-for="image in item.imgurl" :key="image" :href="image" target="_blank">
          <img :src="image" :alt="'image link: ' + image"/>
        </a>
      </div>
      <div class="videos"></div>
    </div>
  </div>
</template>

<script>
export default {
  // eslint-disable-next-line
  name: 'post',
  // eslint-disable-next-line
  props: ['item',]
};
</script>

<style lang="scss" scoped>
  .postwrapper {
    transition: all 0.5s;
    width: 100%;
    margin: 50px 0;
    background-color: #bbb;
    @media (min-width: 768px) {
      border-radius: 15px;
      margin: 25px 0;
    }
  }
  .postdata {
    width: 100%;
    background-color: #666;
    @media (min-width: 768px) {
      border-radius: 10px;
    }
  }
  .postinfo {
    width: 100%;
    padding: 5px 20px;
    letter-spacing: 1px;
    color: white;
  }
  .posttitle{
    width: 100%;
    background-color: #303030;
    padding: 10px;
    color: #fff;
    font-size: 20px;
    letter-spacing: 0.7px;
    border: 1px #222 solid;
    @media (max-width: 768px) {
      border-left: none;
      border-right: none;
    }
    @media (min-width: 768px) {
      border-radius: 10px;
    }
  }
  .postcontent {
    padding: 15px;
    display: flex;
    flex-direction: column;
    align-items: center;
    img{
      width: 100%;
      border-radius: 10px;
      transition: all 0.5s;
    }
    .texts{
      padding: 15px;
      text-align: justify;
      color: #222;
      font-size: 16px;
      @media (min-width: 768px) {
        font-size: 18px;
      }
    }
    .images{
      margin-top: 30px;
      transition: all 0.5s;
      display: grid;
      grid-gap: 25px;
      img:hover{
        opacity: 0.8;
        box-shadow: 0 0 8px 4px rgba($color: #000000, $alpha: 0.4);
      }
      width: 100%;
      @media (min-width: 768px) {
        width: 75%;
      }
    }
  }
</style>
