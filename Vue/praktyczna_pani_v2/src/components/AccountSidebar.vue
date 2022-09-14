<template lang="html">
  <div class="Account-sidebar-wrapper">
    <Transition name="menu">
      <form v-if="loginPageState === 'login'">
        <h2>Logowanie</h2>
        <!-- eslint-disable-next-line -->
        <label for="email">E-mail</label>
        <input
          type="email"
          name="email"
          id="email"
          placeholder="Podaj aders email"
        />
        <!-- eslint-disable-next-line -->
        <label for="password">Hasło</label>
        <input
          type="password"
          name="password"
          id="password"
          placeholder="Podaj hasło"
        />
        <button class="switch-form" @click="loginPageState = 'register'">
          Nie masz konta zarejstruj się
        </button>
        <button type="submit">Zaloguj</button>
      </form>
      <form v-else-if="loginPageState === 'register'">
        <h2>Rejestracja</h2>
        <!-- eslint-disable-next-line -->
        <label for="email">E-mail</label>
        <input
          type="email"
          name="email"
          id="email"
          placeholder="Podaj aders email"
        />
        <!-- eslint-disable-next-line -->
        <label for="email">Potwierdź e-mail</label>
        <input
          type="email"
          name="email-repeat"
          id="email-repeat"
          placeholder="Podaj aders email"
        />
        <!-- eslint-disable-next-line -->
        <label for="password">Hasło</label>
        <input
          type="password"
          name="password"
          id="password"
          placeholder="Podaj hasło"
        />
        <!-- eslint-disable-next-line -->
        <label for="password">Potwierdź Hasło</label>
        <input
          type="password"
          name="password-repeat"
          id="password-repeat"
          placeholder="Podaj hasło"
        />
        <!-- eslint-disable-next-line -->
        <label for="name">Imię i nazwisko</label>
        <input
          type="text"
          name="identity"
          id="identity"
          placeholder="Podaj imie i nazwisko"
        />
        <button
          class="switch-form"
          @click="loginPageState = 'login'"
          type="button"
        >
          Masz konto? Zaloguj się.
        </button>
        <button type="submit">Zarejstruj</button>
      </form>
    </Transition>
  </div>
</template>
<script>
export default {
  data() {
    return {
      loginPageState: 'login',
    };
  },
};
</script>
<style lang="scss" scoped>
@import '../styles/vars';
.Account-sidebar-wrapper {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: relative;
}
form {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translateX(-50%) translateY(-50%);
  width: 80%;
  height: 92vh;
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  @media (min-width: 1024px) {
    width: 60%;
  }
  @media screen and (min-width: 768px) {
    width: 50%;
  }
  h2 {
    font-size: 2.4em;
    padding: 3rem;
  }
  label {
    color: $main-pink;
    font-size: 1.6rem;
    font-weight: 600;
    text-align: left;
    align-self: flex-start;
  }
  input,
  button {
    background: none;
    border: none;
    border-bottom: $main-pink 3px solid;
    color: $gray;
    text-align: center;
    padding: 0.8rem 1rem;
    font-size: 1.6rem;
    width: 100%;
    outline: none;
  }
  input {
    margin: 0 0 4rem 0;
    transition: box-shadow 0.5s;
    &:focus {
      box-shadow: 0 0.8rem 0.6rem -0.4rem $main-pink-shadow;
    }
  }
  button {
    background-color: $main-pink;
    border-radius: 0.4rem;
    color: white;
    font-weight: 700;
    transition-property: box-shadow, transform;
    transition-duration: 0.5s;
    border: none;
    &:hover {
      box-shadow: 0 1rem 1.5rem 0.2rem $main-pink-shadow;
      transform: scale(1.1);
      cursor: pointer;
    }
    @media screen and (min-width: 1024px) {
      padding: 1.2rem 2.4rem;
    }
  }
  p {
    font-size: 1.4rem;
    padding: 1rem;
    transition: transform 0.5s;
    &:hover {
      transform: scale(1.1);
      cursor: pointer;
      text-shadow: 0.1rem 0.1rem 0.2rem $main-pink-shadow;
    }
    @media screen and (min-width: 1024px) {
      margin-top: 8rem;
    }
  }
  .switch-form {
    background: none;
    color: $gray;
    &:hover {
      box-shadow: none;
    }
  }
}
.menu-enter-active,
.menu-leave-active {
  transition-property: transform, opacity;
  transition: 0.5s linear;
}

.menu-enter-from,
.menu-leave-to {
  opacity: 0;
  transform: translateX(100%) translateY(-50%);
}
</style>
