<template>
  <div id="app">
    <fixed-header>
      <div class="navbar">
        <h1>¥Time-Is-Money$</h1>
        <nav id="nav">
          <router-link to="/">About</router-link> |
          <router-link to="/data">Data</router-link> |
          <router-link to="/simulator">Simulator</router-link>
        </nav>
      </div>
    </fixed-header>
    <router-view />
    <Footer />
  </div>
</template>

<script>
import Footer from "@/components/Footer.vue";
import FixedHeader from "vue-fixed-header";

export default {
  name: "App",
  components: {
    Footer,
    FixedHeader
  }
};
</script>

<style lang="scss">
@import "node_modules/bootstrap/scss/bootstrap";
@import "node_modules/bootstrap-vue/src/index.scss";

html {
  font-size: 16px;
}

body {
  background-color: black;
  width: 100%;
  padding: 0px;
}

.mb-50 {
  margin-bottom: 50px;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: white;
}

.navbar {
  z-index: 1;
  h1 {
    text-align: initial;
    margin: 0.65rem;
    font-size: 2em;
  }
}

.form-group--error {
  label {
    color: #f04124;
  }

  input {
    border: 1px solid #f79483 !important;
  }
  border-color: #f79483;
}

.error {
  color: #f57f6c;
}

#nav {
  padding: 0.65rem;
  font-size: 1em;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}

.navbar.vue-fixed-header--isFixed {
  position: fixed;
  left: 0;
  top: 0;
  width: 100vw;
  background-color: black;
}
</style>
