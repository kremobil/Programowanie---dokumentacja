<template>
    <div class="inputwrapper">
        <!-- eslint-disable-next-line  -->
        <input type="text" placeholder="napisz coś"/>
        <button>⮞</button>
    </div>
</template>
<script>
export default {

};
</script>
<style lang="scss" scoped>
    .inputwrapper {
        width: 100%;
        background-color: gray;
        padding: 10px;
        margin-top: auto;
        margin-bottom: 0;
        border-radius: 0 0 15px 15px;
    }
    input{
        padding: 10px;
        width: 85%;
        margin: 5px;
        border-radius: 10px;
        border: 2px solid #404040;
    }
    button {
        width: 10px;
        height: 10px;

    }
</style>
