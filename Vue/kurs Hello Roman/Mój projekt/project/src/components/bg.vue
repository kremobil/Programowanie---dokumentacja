<template>
    <div class="backgroundimage"></div>
</template>

<script>
    export default {
        name: 'bg',
    };
</script>

<style lang="scss">
    .backgroundimage {
        position: fixed;
        width: 100%;
        height: 100vh;
        background-image: url('../assets/background.jpg');
        background-repeat: no-repeat;
        background-size: cover;
        background-position: 80% 0%;
        z-index: -1;
    }
    .backgroundimage::after {
        content: '';
        background: rgba($color: #000000, $alpha: 0.2);
        position: absolute;
        top: 0;
        left: 0;
        z-index: 1;
        width: 100%;
        height: 100vh;
    }
</style>