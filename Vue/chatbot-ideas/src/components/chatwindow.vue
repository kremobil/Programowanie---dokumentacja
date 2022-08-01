<template lang="html">
    <div class="mainchatwrapper">
        <div class="massage" :class="{ opsite: opsite }">
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Natus ex id ad dolore
        </div>
        <div class="massage" :class="{ opsite: opsoite }">
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Natus ex id ad dolore
        </div>
    </div>
</template>
<script>
export default {
  // eslint-disable-next-line
    name: "chatwindow",
  data() {
    return {
      opsoite: true,
    };
  },
};
</script>
<style lang="scss" scoped>
    .mainchatwrapper {
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }
    .massage {
        max-width: 80%;
        background-color: #606060;
        margin: 10px;
        padding: 10px;
        color: white;
        border-radius: 15px 15px 15px 0;
    }
    .opsite {
        max-width: 80%;
        background-color: aqua;
        margin: 10px;
        padding: 10px;
        color: #606060;
        border-radius: 15px 15px 0 15px;
        align-self: flex-end;
    }
</style>
