import Vue from "vue";
import VueRouter from "vue-router";
import Simulator from "../views/Simulator.vue";
import Data from "../views/Data.vue";
import About from "../views/About.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "About",
    component: About
  },
  {
    path: "/simulator",
    name: "Simulator",
    component: Simulator
  },
  {
    path: "/data",
    name: "Data",
    component: Data
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
