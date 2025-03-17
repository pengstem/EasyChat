import { createApp } from 'vue'
import { createPinia } from 'pinia'
import router from './router'
import './style.css'
import EasyChatApp from './EasyChatApp.vue'

const link = document.createElement('link')
link.rel = 'stylesheet'
link.href = 'https://fonts.googleapis.com/icon?family=Material+Icons'
document.head.appendChild(link)

const app = createApp(EasyChatApp)
const pinia = createPinia()

app.use(pinia)
app.use(router)

// Initialize theme system
import { useAppStore } from './stores/appStore'
app.mount('#app')

// Initialize theme after app is mounted
const appStore = useAppStore()
appStore.initializeTheme()