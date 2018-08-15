import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Library from '@/components/library/Library'
import Basic from '@/components/base/Basic'
import About from '@/components/base/About'
import Login from '@/components/user/Login'
import Register from '@/components/user/Register'
import Home from '@/components/home/Home'
import BlogList from '@/components/blog/BlogList'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/lib',
      name: 'Library',
      component: Library
    },
    {
      path: '/',
      name: 'basic',
      component: Basic,
      redirect: '/home',
      children: [
        {
          path: 'home',
          name: 'home',
          component: Home
        },
        {
          path: 'bloglist',
          name: 'bloglist',
          component: BlogList
        },
        {
          path: 'about',
          name: 'about',
          component: About
        },
        {
          path: 'login',
          name: 'login',
          component: Login
        },
        {
          path: 'register',
          name: 'register',
          component: Register
        }
      ]
    }
  ]
})
