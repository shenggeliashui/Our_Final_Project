import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
// import store from './store'; // 如果使用 Vuex

createApp(App)
  .use(router)
  // .use(store) // 如果使用 Vuex
  .mount('#app');

