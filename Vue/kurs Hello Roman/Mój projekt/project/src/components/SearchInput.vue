<template>
    <div class="searchWrapper">
         <!-- eslint-disable-next-line -->
        <input id="search" type="text" name="search" v-model="inputvalue" @input="handleSearch" :class="{ dark: dark }"/>
    </div>
</template>
<script>
/* eslint-disable */ 
export default {
    name: "SearchInput",
    props: {
        dark: {
            type: Boolean,
            default: false,
        }
    },
    data() {
        return {
            inputvalue: "",
        }
    },
    methods: {
        handleSearch(e) {
            console.log(this.inputvalue);
            this.$emit('input', this.inputvalue);
        },
    },
}
</script>
<style lang="scss" scoped>
    .searchWrapper {
        display: flex;
        flex-direction: column;
        width: 250px;
        @media (min-width: 1024px) {
            width: 400px;
        }
    }
    input {
        margin-top: 50px;
        height: 30px;
        border: 0;
        border-bottom: 1px solid white;
        background: none;
        transition: box-shadow .5s;
        color: #fff;
        text-align: center;
        font-size: 18px;
        font-weight: 300;
        @media (min-width: 1024px) {
            margin-top: 80px;
        }
    }
    input:focus {
        outline: none;
        box-shadow: 0 10px 15px -10px rgba(255, 255, 255, 0.5);
        @media (min-width: 1024px) {
            box-shadow: 0 15px 20px -10px rgba(255, 255, 255, 0.6);
        }
    }

    .dark {
        color: #1e3d4a;
        border-bottom-color: #1e3d4a;
    }
    .dark:focus {
        box-shadow: 0 10px 15px -10px rgba(#1e3d4a, 0.5);
        @media (min-width: 1024px) {
            box-shadow: 0 15px 20px -10px rgba(#1e3d4a, 0.6);
        }
    }
</style>