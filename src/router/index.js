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
    path: '/table/:id',
    name: 'Table',
    component: () => import('../views/Table.vue')
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
    path: '/config/tableconfig/:id',
    name: 'Tableconfig',
    component: () => import('../views/TableConfiguration.vue')
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
