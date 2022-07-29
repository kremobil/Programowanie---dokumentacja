<template>
    <div class="outerWrapper">
        <div class="innerWrapper">
            <div class="photo">
                <img :src="data.url" :alt="data.title" />
            </div>
            <div class="decription">
                <h2 class="title">{{data.title}}</h2>
                <p class="description" v-if="data.description.length <= 500">
                    {{data.description}}
                </p>
            </div>
        </div>
        <!-- eslint-disable-next-line -->
        <div class="close" @click="$emit('closeModal')"></div>
    </div>
</template>
<script>
export default {
  // eslint-disable-next-line
  name: 'modal',
  props: {
    data: {
      type: Object,
      required: true,
    },
  },
};
</script>
<style lang="scss" scoped>
    .outerWrapper {
        background-color: #f6f6f6;
        width: 100%;
        position: fixed;
        height: 100%;
        top: 0;
        left: 0;

        @media (min-width: 1024px) {
            width: 70%;
            height: 60%;
            left: 0;
            right: 0;
            top: 0;
            bottom: 0;
            margin: auto;
            border-radius: 15px;
            box-shadow: 5px 5px 25px 15px rgba($color: #444, $alpha: .7);
        }
    }
    .innerWrapper {
        background-color: #f6f6f6;
        display: flex;
        height: 100%;
        padding: 50px;
        justify-content: center;
        align-items: center;
        flex-direction: column;

        @media (min-width: 1024px) {
            border-radius: 15px;
            flex-direction: row;

            .photo {
                min-width: 50%;
                margin-right: 20px;

                img {
                    max-height: 50vh;
                }
            }
        }
    }

    .photo{
        width: 100%;
        height: auto;

    }

    img{
        width: 100%;
        border-radius: 3%;
    }

    .description{
        color: #333;
    }

    .close{
        position: absolute;
        width: 30px;
        height: 30px;
        right: 0;
        top: 0;
        padding: 30px;
        cursor: pointer;
        &::before,
        &::after {
            position: absolute;
            content: '';
            width: 20px;
            top: 30px;
            right: 20px;
            height: 2px;
            background-color: black;
            display: block;
        }

        &::before {
            transform: rotate(45deg);
        }

        &::after {
            transform: rotate(-45deg);
        }
    }
</style>
