import { createRouter, createWebHistory } from 'vue-router'
import FreeBackShow from '@/view/FreeBack'
import AllFrame from '@/view/frame'
import SpellWords from '@/view/SpellTenWords'
import HomeShow from  '@/view/HomeShow'
import CalendarL from '../components/calendar.vue'
import MemoryShow from '@/view/Memory'
import FinishMemoShow from '@/view/FinishMemo'

// 创建路由实例
const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path:'/MemoryShow',
      name:'MemoryShow',
      component:MemoryShow
    },
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
    },
    {
      path:'/FinishMemoShow',
      name:'FinishMemoShow',
      component:FinishMemoShow
    }
  ]
})

export default router
