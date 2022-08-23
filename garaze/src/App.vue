<template>
  <div class="wrapper">
    <Nawigacja @kliknaprzyciskuxd="login" />
    <Transition name="fade">
      <Loguj v-if="logowanie == true" />
    </Transition>
    <Arizona />
  </div>
</template>

<script>
import Nawigacja from './components/Nawigacja.vue';
import Loguj from './components/Loguj.vue';
import Arizona from './components/arizona.vue';

export default {
  components: {
    Nawigacja,
    Loguj,
    Arizona,
  },
  data() {
    return {
      logowanie: false,
    };
  },
  methods: {
    login() {
      this.logowanie = !this.logowanie;
    },
  },
};
</script>
<style lang="scss">
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
.wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.fade-enter-active,
.fade-leave-active {
  transition: all 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  transform: translateX(100%);
  opacity: 0;
  @media screen and (max-width: 642px) {
    transform: translateY(-100%);
  }
}
.kloc {
  width: 100%;
  height: 300px;
  background-color: black;
}
.grid {
  width: 80%;
  display: grid;
  background-color: rebeccapurple;
  grid-gap: 10px;
  grid-template-columns: 1fr 1fr;
  margin: 10px;
}
</style>
