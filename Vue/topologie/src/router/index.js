import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import MagistralTopology from '../views/MagistralTopology.vue';
import RingTopology from '../views/RingTopology.vue';
import StarTopology from '../views/StarTopology.vue';
import TreeTopology from '../views/TreeTopology.vue';
import GridTopology from '../views/GridTopology.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/mag',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: MagistralTopology,
  },
  {
    path: '/pir',
    component: RingTopology,
  },
  {
    path: '/gwi',
    component: StarTopology,
  },
  {
    path: '/drz',
    component: TreeTopology,
  },
  {
    path: '/sia',
    component: GridTopology,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
