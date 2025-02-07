import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min';
// import 'bootstrap-dark-5/dist/css/bootstrap-dark.min.css'; // Dark theme

// Create a global axios instance
const app = createApp(App);
app.config.globalProperties.$axios = axios;

app.use(router).mount('#app');
