import { createRouter, createWebHistory } from 'vue-router'
import freeback from '@/view/freeback'
import AllFrame from '@/view/frame'
import SpellTenWords from '@/view/Spell'
// import Calendar from '../components/calendar.vue'

// 创建路由实例
const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'AllFrame',
      component: AllFrame
    },
    {
      path: '/freeback',
      name: 'Freeback',
      component: freeback
    },
    {
      path: '/spell',
      name: 'Spell',
      component: SpellTenWords
    }
  ]
})

export default router
