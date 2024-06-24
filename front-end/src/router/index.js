import { createRouter, createWebHistory } from 'vue-router'
import FreeBackShow from '@/view/FreeBack'
import SpellWords from '@/view/SpellTenWords'
import HomeShow from  '@/view/HomeShow'
import MemoryShow from '@/view/Memory'
import FinishMemoShow from '@/view/FinishMemo'
import UserLogin from '../components/UserLogin.vue';
import RegisterUser from '../components/RegisterUser.vue'; // 导入注册组件
import UserProfile from '../view/UserProfile.vue';

// 创建路由实例
const routes =[
    {
      path: '/',
      name: 'Login',
      component: UserLogin
    },
    {
      path:'/MemoryShow',
      name:'MemoryShow',
      component:MemoryShow
    },
    {
      path: '/HomeShow',
      name: 'HomeShow',
      component: HomeShow
    },
    {
      path: '/freeback',
      name: 'FreeBackShow',
      component: FreeBackShow
    },
    {
      path: '/register',
      name: 'Register',
      component: RegisterUser // 添加注册路由
    },
    {
      path: '/profile',
      name: 'UserProfile',
      component: UserProfile
    },
    {
      path: '/Spell',
      name: 'Spell',
      component: SpellWords
    },
    {
      path:'/FinishMemoShow',
      name:'FinishMemoShow',
      component:FinishMemoShow
    }
  ];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

// 如果路由需要身份验证（meta: { requiresAuth: true }）并且没有令牌，用户将被重定向到登录页面。
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token');
  if (to.matched.some(record => record.meta.requiresAuth) && !token) {
    next('/');
  } else {
    next();
  }
});

export default router;

