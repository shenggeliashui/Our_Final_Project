import Vue from 'vue'
import Router from 'vue-router'
import freeback from '@/freeback'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/'
      // name: 'calendar',
      // component: calendar
    },
    {
      path: '/freeback',
      name: 'Freeback',
      component: freeback
    }
  ]
})
