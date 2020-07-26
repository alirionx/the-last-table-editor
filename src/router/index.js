import Vue from 'vue'
import VueRouter from 'vue-router'
import Tables from '../views/Tables.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Tables',
    component: Tables
  },
  {
    path: '/configure',
    name: 'Configure',
    component: () => import('../views/Configure.vue')
  },
  {
    path: '/config/tableparas/:id',
    name: 'Tableparas',
    component: () => import('../views/TableParas.vue')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
