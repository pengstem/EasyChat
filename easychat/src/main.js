import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import SecondApp from './components/SecondApp.vue'

// First application instance
const app1 = createApp(App)
app1.mount('#app')

// Second application instance
const app2 = createApp(SecondApp)
app2.mount('#app2')
