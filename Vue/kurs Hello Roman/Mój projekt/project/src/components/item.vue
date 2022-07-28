<template>
    <div :style="style" class="image">
    </div>
</template>
<script>
export default {
  // eslint-disable-next-line
    name: 'item',
  data() {
    return {
      photo: this.myvar.links[0].href,
      title: this.myvar.data[0].title,
    };
  },
  computed: {
    style() {
      return `background-image: url("${this.photo}")`;
    },
  },
  props: {
    myvar: {
      type: Object,
      required: true,
    },
  },
};
</script>
<style lang="scss" scoped>
    .image {
        width: 125px;
        height: 125px;
        background-size: cover;
        background-repeat: no-repeat;
        border-radius: 2%;
        @media (min-width: 400px) {
          width: 200px;
          height: 200px;
        }
        @media (min-width: 1366px) {
          width: 300px;
          height: 300px;
        }
    }
</style>
