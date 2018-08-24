import Vue from 'vue'
import Router from 'vue-router'
import Basic from '@/components/base/Basic'
import About from '@/components/base/About'
import Login from '@/components/user/Login'
import Register from '@/components/user/Register'
import Home from '@/components/home/Home'
import Tech from '@/components/blog/Tech'
import Life from '@/components/blog/Life'
import Blog from '@/components/blog/Blog'

Vue.use(Router)

export default new Router({
  routes: [
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
          path: 'tech',
          name: 'tech',
          component: Tech
        },
        {
          path: 'life',
          name: 'life',
          component: Life
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
        },
        {
          path: 'blog/:id',
          name: 'blog',
          component: Blog
        }
      ]
    }
  ]
})
