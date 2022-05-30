import Vue from 'vue';
import Router from 'vue-router';
import EventManager from '../components/EventManager.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Events',
      component: EventManager,
    },
  ],
});
