<template>
    <div class="searchWrapper">
        <input id="search" type="text" name="search" v-model="searchValue" @input="handleSearch"/>
    </div>
</template>
<script>
export default {
    
}
</script>
<style lang="scss" scoped>
    .searchWrapper {
        display: flex;
        flex-direction: column;
        width: 250px;
    }
    input {
        margin-top: 50px;
        height: 30px;
        border: 0;
        border-bottom: 1px solid black;
        background: none;
    }
</style>