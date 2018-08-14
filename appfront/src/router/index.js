import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Library from '@/components/library/Library'
import basic from '@/components/basic'
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
      path: '/',
      name: 'basic',
      component: basic,
      children: [
        {
          path: 'home',
          component: Home
        }
      ]
    }
  ]
})
