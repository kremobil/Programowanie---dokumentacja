<template>
    <div class="searchWrapper">
        <input id="search" type="text" name="search" :value="value" @input="handleSearch"/>
    </div>
</template>
<script>
export default {
    name: "SearchInput",
    props: {
        value: {
            type: String,
            required: true,
        }
    },
    methods: {
        handleSearch(e) {
            this.$emit('input', e.target.value);
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
</style>