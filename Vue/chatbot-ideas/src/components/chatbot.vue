<template>
  <div class="chatbot">
    <Transition name="slide-up">
      <!-- eslint-disable-next-line -->
      <div v-if="show" class="icon" :class="{ hidden: !show}" @click="show = false">
        <img src="../assets/messenger.png" alt="messenger icon"/>
      </div>
      <div v-else class="opend" :class="{ hidden: show}">
        <Transition name="fade">
          <div class="chatcontainer">
            <!-- eslint-disable-next-line -->
            <div class="hedder" v-if="!show">Chat Bot<div class="close" @click="show = true"></div></div>
            <Chatwindow />
            <ChatbotInput class="flexend"/>
          </div>
        </Transition>
      </div>
    </Transition>
  </div>
</template>

<script>
import Chatwindow from './chatwindow.vue';
import ChatbotInput from './chatbotInput.vue';

export default {
  // eslint-disable-next-line
    name: "chatbot",
  data() {
    return {
      show: true,
    };
  },
  components: { Chatwindow, ChatbotInput },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  img {
    width: 50px;
    height: 50px;
  }
  .chatbot {
    position: fixed;
    right: 30px;
    bottom: 30px;
  }
  .icon {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 75px;
    height: 75px;
    border-radius: 50%;
    background-color: rgb(0, 110, 255);
    cursor: pointer;
  }
  .opend{
    display: flex;
    align-items: center;
    flex-direction: column;
    position: fixed;
    width: 100%;
    height: 100vh;
    top: 0;
    left: 0;
    border-radius: 15px;
    background-color: azure;
    box-shadow: 10px 10px 25px -5px rgba(0, 0, 0, 0.5);
    @media (min-width: 768px) {
      width: 400px;
      height: 700px;
      right: 0;
      bottom: 0;
      top: auto;
      left: auto;
      position: absolute;
    }
  }
  .chatcontainer {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    flex-direction: column;
  }
  .hedder{
    background-color: rgb(0, 110, 255);
    width: 100%;
    text-align: center;
    color: azure;
    padding: 15px;
    font-size: 24px;
    font-weight: 700;
    letter-spacing: 1px;
    @media (min-width: 768px) {
      border-radius: 15px;
    }
  }
  .close{
    position: absolute;
    width: 30px;
    height: 6px;
    background-color: #303030;
    border-radius: 20%;
    top: 28px;
    right: 20px;
    cursor: pointer;
    transition: all 0.5s;
    &:hover{
      background-color: #666;
      box-shadow: 0 0 10px 1px rgba(white, .4);
    }
  }
  .slide-up-enter-active,
  .slide-up-leave-active {
    transition: all 0.5s ease-out;
  }

  .slide-up-enter-from{
    opacity: 0;
    width: 75px;
    height: 75px;
    background-color: rgb(0, 110, 255);
    position: absolute;
    right: 0;
    bottom: 0;
  }
  .slide-up-leave-to {
    opacity: 0;
    @media (min-width: 768px) {
      // position: absolute;
      // right: 0;
      // bottom: 0;
      // width: 75px;
      // height: 75px;
      // background-color: rgb(0, 110, 255);
      // border-radius: 25px;
      // opacity: 1;
      transform: translateX(100px);
    }
  }
  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.5s ease;
  }

  .fade-enter-from,
  .fade-leave-to {
    display: none;
  }
  .hidden {
    display: none;
  }
</style>
