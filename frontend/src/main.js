import Vue from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
import VuePaginate from "vue-paginate";
import Vuelidate from "vuelidate";

Vue.use(Vuelidate);
Vue.use(VuePaginate);

// Install BootstrapVue
Vue.use(BootstrapVue);
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin);

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");

if ("serviceWorker" in navigator) {
  navigator.serviceWorker
    .register("./service-worker.js")
    .then(function(registration) {
      console.log("Service Worker Registered!");
      return registration;
    })
    .catch(function(err) {
      console.error("Unable to register service worker.", err);
    });
}
