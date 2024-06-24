import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import VTooltip from 'v-tooltip'
import './components/global.css'

const app = createApp(App)
app.use(router)
// app.use(VTooltip)
app.directive('tooltip', VTooltip.directive)
app.config.productionTip = false

app.mount('#app')
