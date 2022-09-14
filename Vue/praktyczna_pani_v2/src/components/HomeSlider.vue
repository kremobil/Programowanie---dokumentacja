<template lang="html">
  <div class="slider-wrapper">
    <transition name="slider">
      <img :src="slides[1]" alt="slide" v-if="currentSlide === 1" />
      <img :src="slides[2]" alt="slide" v-else-if="currentSlide === 2" />
      <img :src="slides[3]" alt="slide" v-else-if="currentSlide === 3" />
    </transition>
    <button class="left" @click="currentSlide--">&lt;</button>
    <button class="right" @click="currentSlide++">&gt;</button>
  </div>
</template>
<script>
export default {
  name: 'HomeSlider',
  data() {
    return {
      slides: {
        1: 'https://images.pexels.com/photos/322207/pexels-photo-322207.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
        2: 'https://images.pexels.com/photos/135620/pexels-photo-135620.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
        3: 'https://images.pexels.com/photos/325876/pexels-photo-325876.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
      },
      currentSlide: 1,
    };
  },
};
</script>
<style lang="scss" scoped>
.slider-wrapper {
  width: 100%;
  position: relative;
}
button {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background-color: #30303085;
  color: white;
  border: 0;
  padding: 1.2rem 1.6rem;
  display: block;
  font-size: 2.4rem;
  transition: all 0.5s;
  font-weight: bold;
  border-radius: 0 0.6rem 0.6rem 0;
  &:hover {
    background-color: #30303095;
    cursor: pointer;
    transform: scale(1.2) translateY(-40%);
  }
}
.right {
  right: 0;
  border-radius: 0.6rem 0 0 0.6rem;
}
img {
  width: 100%;
  height: 100%;
}
.slide-enter-active,
.slide-leave-active {
  transition: opacity 0.5s ease;
}

.slide-enter-from,
.slide-leave-to {
  opacity: 0;
}
</style>
