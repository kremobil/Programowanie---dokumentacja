<template lang="html">
  <div class="sidebar-basket-wrapper">
    <div class="ItemContainer" v-for="Item in BasketContent" :key="Item.name">
      <img src="../assets/psy1.png" :alt="Item.name" />
      <div class="item-info">
        <h2>Maseczka {{ Item.name }}</h2>
        <h3>{{ Math.floor(Item.price * Item.ammount * 100) / 100 }} zł</h3>
      </div>
      <div class="item-ammount">
        <font-awesome-icon
          icon="fa-solid fa-minus"
          class="item-icon"
          @click="Item.ammount--"
        />
        <h2>{{ Item.ammount }}</h2>
        <font-awesome-icon
          icon="fa-solid fa-plus"
          class="item-icon"
          @click="Item.ammount++"
        />
      </div>
    </div>
    <div class="total-price">{{ calcTotal() }}</div>
  </div>
</template>
<script>
export default {
  name: 'BasketSidebar',
  data() {
    return {
      BasketContent: [
        {
          name: 'psy',
          imgUrl: '../assets/psy1.png',
          price: 23.99,
          ammount: 1,
        },
        {
          name: 'koty',
          imgUrl: '../assets/psy1.png',
          price: 23.99,
          ammount: 1,
        },
        {
          name: 'zebry',
          imgUrl: '../assets/psy1.png',
          price: 23.99,
          ammount: 1,
        },
        {
          name: 'zebry',
          imgUrl: '../assets/psy1.png',
          price: 23.99,
          ammount: 1,
        },
        {
          name: 'zebry',
          imgUrl: '../assets/psy1.png',
          price: 23.99,
          ammount: 1,
        },
      ],
    };
  },
  methods: {
    calcTotal() {
      // eslint-disable-next-line
      for (let item of this.BasketContent) {
        // eslint-disable-next-line
        console.log(item);
      }
    },
  },
};
</script>
<style lang="scss" scoped>
.sidebar-basket-wrapper {
  display: flex;
  flex-direction: column;
  width: 90%;
  height: 80%;
  overflow: auto;
  @media (max-width: 768px) {
    width: 100%;
  }
}
.ItemContainer {
  width: 100%;
  height: 20%;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  padding: 15px;
  border-bottom: 2px dashed #2b3543;

  &:last-child {
    border: none;
  }
  img {
    height: 100%;
  }
  .item-info {
    display: flex;
    flex-direction: column;
    margin: 0 20px;

    h2,
    h3 {
      margin: 5px 0;
    }
    h3 {
      color: #748400;
    }
  }
  .item-ammount {
    display: flex;
    align-items: center;
    font-size: 24px;
    margin: 0 0 0 auto;
    .item-icon {
      margin: 0 10px;
      transition: all 0.5s;
      &:first-child {
        &:hover {
          color: #fb3333;
          transform: scale(1.25);
          cursor: pointer;
        }
      }
      &:hover {
        color: #748400;
        transform: scale(1.25);
        cursor: pointer;
      }
    }
    @media (max-width: 768px) {
      font-size: 16px;
    }
  }
  @media (max-width: 768px) {
    font-size: calc(100vh / 100);
  }
  text-align: left;
}
</style>
