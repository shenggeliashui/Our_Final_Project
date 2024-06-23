import { createApp } from 'vue'
//import HomePage from './components/HomePage.vue'
import router from './router'
import App from './App'

const app = createApp(App)

app.use(router)

app.mount('#App')