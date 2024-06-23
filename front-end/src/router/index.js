import { createRouter, createWebHistory } from 'vue-router'
import FreeBackShow from '@/view/FreeBack'
import AllFrame from '@/view/frame'
import SpellWords from '@/view/SpellTenWords'
import HomeShow from  '@/view/HomeShow'
// import Calendar from '../components/calendar.vue'

// 创建路由实例
const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'HomeShow',
      component: HomeShow
    },
    {
      path: '/freeback',
      name: 'FreeBackShow',
      component: FreeBackShow
    },
    {
      path: '/Spell',
      name: 'Spell',
      component: SpellWords
    }
  ]
})

export default router
