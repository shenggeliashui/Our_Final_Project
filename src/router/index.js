import Vue from 'vue'
import Router from 'vue-router'
import freeback from '@/view/freeback'
import Frame from '@/view/frame'
// import Calendar from '../components/calendar.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Frame',
      component: Frame
    },
    {
      path: '/freeback',
      name: 'Freeback',
      component: freeback
    }
  ]
})
