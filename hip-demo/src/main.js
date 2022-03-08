import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

import axios from 'axios';

//导入全局样式表
import './assets/css/global.css'

Vue.use(ElementUI);

Vue.config.productionTip = false

Vue.prototype.axios = axios;

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
