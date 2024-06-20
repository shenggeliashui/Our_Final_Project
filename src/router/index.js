import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import UserLogin from '../components/UserLogin.vue';
import RegisterUser from '../components/RegisterUser.vue'; // 导入注册组件

const routes = [
  {
    path: '/',
    name: 'Login',
    component: UserLogin
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterUser // 添加注册路由
  },
  {
    path: '/home',
    name: 'HomePage',
    component: HomePage,
    meta: { requiresAuth: true }
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token');
  if (to.matched.some(record => record.meta.requiresAuth) && !token) {
    next('/');
  } else {
    next();
  }
});

export default router;
