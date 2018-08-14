import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Library from '@/components/library/Library'
import Base from '@/components/Base'
import Home from '@/components/home/Home'

Vue.use(Router)

export default new Router({
  routes: [
    // {
    //   path: '/hello',
    //   name: 'HelloWorld',
    //   component: HelloWorld
    // },    
    {
      path: '/lib',
      name: 'Library',
      component: Library
    },
    {
      path: '/base',
      name: 'Base',
      component: Base,
      children: [
        {
          path: 'home',
          component: Home
        }
      ]
    }
  ]
})
