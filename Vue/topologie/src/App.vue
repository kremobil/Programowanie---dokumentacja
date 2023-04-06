<template>
  <div class="wrapper">
    <header class="title">
      <img src="./assets/logo-no-background.png" alt="web topologies logo" />
    </header>
    <section class="content">
      <nav>
        <h1>Spis treści</h1>
        <div class="links">
          <router-link to="/">Topologie</router-link>
          <router-link to="/mag">Magistrala</router-link>
          <router-link to="/pir">Pierścień</router-link>
          <router-link to="/gwi">Gwiazda</router-link>
          <router-link to="/drz">Drzewo</router-link>
          <router-link to="/sia">Siatka</router-link>
        </div>
      </nav>
      <router-view />
    </section>
  </div>
</template>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Roboto', sans-serif;
}
a {
  font-size: 1.4rem;
  text-decoration: none;
  color: #343434;
}
.content {
  width: 25%;
  height: 80vh;
}
.wrapper {
  width: 100%;
  height: 100vh;
}
.title {
  width: 100%;
  height: 20vh;
  background: linear-gradient(rgb(85, 230, 255), transparent);
  padding: 2rem;
  display: flex;
  justify-content: center;
  position: relative;
  img {
    max-width: 50%;
    border: 0.3rem solid #0483ff;
    padding: 1rem 3rem;
  }
  /* &::after {
    width: 90%;
    height: 0.2rem;
    position: absolute;
    content: '';
    background-color: #0483ff;
    bottom: -0.5rem;
  } */
}
.content {
  width: 100%;
  height: 80vh;
  display: flex;
  align-items: center;
}
nav {
  width: 25%;
  border-right: 0.2rem solid #0483ff;
  height: 70vh;
  padding: 1rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  .links {
    height: 55vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-evenly;
    a {
      position: relative;
      outline: none;
      border: none;
      &::before,
      &::after {
        width: 0;
        height: 0.2rem;
        background-color: rgba(#0483ff, 0.5);
        content: '';
        position: absolute;
        left: 50%;
        top: 0;
        transform: translate(-50%, -150%);
        transition: width 0.5s;
      }
      &:hover::before,
      &:hover::after,
      &:focus::before,
      &:focus::after {
        width: 150%;
      }
      &::after {
        top: 100%;
        transform: translate(-50%, 50%);
      }
    }
  }
  h1 {
    font-size: 2.2rem;
    color: #0483ff;
    letter-spacing: 0.2rem;
  }
}
</style>
