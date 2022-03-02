import Vue from 'vue'
import VueRouter from 'vue-router'

// 页面级组件导入
import login from '../views/login.vue'
import sign from '../views/sign.vue'


Vue.use(VueRouter)

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: login },
  { path: '/sign', component: sign },
]

const router = new VueRouter({
  routes
})

export default router
