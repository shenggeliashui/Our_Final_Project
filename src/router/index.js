import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import UserLogin from '../components/UserLogin.vue';

const routes = [
  {
    path: '/',
    name: 'Login',
    component: UserLogin
  },
  {
    path: '/home',
    name: 'HomePage',
    component: HomePage
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
