import Vue from 'vue';
import Router from 'vue-router';
import Events from '../components/Events.vue';
import Ping from '../components/Ping.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Events',
      component: Events,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
});
