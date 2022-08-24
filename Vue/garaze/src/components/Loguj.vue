<template lang="html">
  <div class="login">
    <h2>Zaloguj</h2>
    <!-- eslint-disable-next-line -->
    <input type="text" placeholder="Nazwa" />
    <!-- eslint-disable-next-line -->
    <input type="password" placeholder="Hasło" />
    <input type="submit" value="Zaloguj" />
  </div>
</template>
<script>
export default {
  name: 'LogujUzytkownik',
};
</script>
<style lang="scss">
$czarny: #1e1e1e;
.login {
  width: 20%;
  height: 50vh;
  background-color: #d9d9d9;
  position: absolute;
  right: 2%;
  border-radius: 5px;
  display: flex;
  flex-direction: column;
  color: $czarny;
  letter-spacing: 1px;
  align-items: center;
  justify-content: space-around;
  transition: all 0.5s;
  top: 12vh;
  @media screen and (max-width: 1100px) {
    width: 55%;
  }
  @media screen and (max-width: 642px) {
    width: 96%;
  }

  input {
    width: 60%;
    text-align: center;
    padding: 5px;
    background: none;
    border: none;
    border-bottom: 2px solid $czarny;
    color: $czarny;
    font-size: 18px;
    transition: all 0.5s;
    &[type='submit'] {
      border: none;
      background-color: #fee5d4;
      border-radius: 5px;
      color: $czarny;
      padding: 15px;
      &:hover {
        background-color: #ffd2b4;
        cursor: pointer;
      }
    }
    &:focus {
      outline: none;
      box-shadow: 0px 5px 2px -1px #1e1e1e50;
    }
  }
}
</style>
