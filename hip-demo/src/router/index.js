import Vue from 'vue'
import VueRouter from 'vue-router'

// 页面级组件导入
import login from '../views/login.vue'
import sign from '../views/sign.vue'
import mailLeader from '../views/mailLeader.vue'
// 页面内路由组件导入
import mailboxLeader from '../components/mailboxLeader.vue'
import adminLeader from '../components/adminLeader/adminLeader.vue'
import dealexcel from '../components/dealexcel/dealexcel.vue'


Vue.use(VueRouter)

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: login },
  { path: '/sign', component: sign },
  {
    path: '/mailLeader',
    component: mailLeader,
    children: [
      { path: '', redirect: 'mails' },
      { path: 'dealexcel', component: dealexcel },
      { path: 'mails', component: mailboxLeader },
      {
        path: 'admin',
        component: adminLeader,
      },
    ]
  },
  // { path: '/mailUser', component: mailUser },
]

const router = new VueRouter({
  routes
})

export default router
