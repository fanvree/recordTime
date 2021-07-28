import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
// import Antd from 'ant-design-vue'
// import {Button} from 'ant-design-vue'
// import DatePicker from 'ant-design-vue/lib/date-picker'; // 加载 JS
// import 'ant-design-vue/lib/date-picker/style/css'; // 加载 CSS
// import 'ant-design-vue/dist/antd.css'
import axios from 'axios'
import VueAxios from 'vue-axios'


import {Layout, Menu, Timeline, Input, InputNumber, Col, Row, Breadcrumb, Switch, Calendar, Badge} from 'ant-design-vue'
import {Button} from 'ant-design-vue'


Vue.use(Button)
// Vue.component(Button.name, Button)

Vue.use(Layout)
// Vue.component(Layout.name, Layout)

Vue.use(Menu)
// Vue.component(Menu.name, Menu)

Vue.use(Timeline)
// Vue.component(Timeline.name, Timeline)

Vue.component(InputNumber.name, InputNumber)

Vue.component(Col.name, Col)

Vue.component(Row.name, Row)

Vue.use(Breadcrumb)

Vue.use(Switch)


Vue.use(Input)

Vue.use(Calendar)

Vue.use(Badge)





Vue.use(VueAxios,axios);
Vue.config.productionTip = false
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
