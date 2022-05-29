import Vue from 'vue';
import Router from 'vue-router';
import EventsComponent from '../components/EventsComponent.vue';
import PingComponent from '../components/PingComponent.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Events',
      component: EventsComponent,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: PingComponent,
    },
  ],
});
