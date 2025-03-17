import { defineStore } from 'pinia'

export const useAppStore = defineStore('app', {
  state: () => ({
    theme: localStorage.getItem('easychat-theme') || 'system', // 'light', 'dark', or 'system'
    settings: JSON.parse(localStorage.getItem('easychat-settings')) || {
      theme: 'system',
      language: 'en',
      notifications: true
    }
  }),
  actions: {
    setTheme(theme) {
      this.theme = theme
      localStorage.setItem('easychat-theme', theme)
      this.applyTheme()
    },
    
    applyTheme() {
      const theme = this.theme
      const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches
      
      // Remove existing theme classes
      document.documentElement.classList.remove('light-theme', 'dark-theme')
      
      if (theme === 'dark' || (theme === 'system' && prefersDark)) {
        document.documentElement.classList.add('dark-theme')
      } else {
        document.documentElement.classList.add('light-theme')
      }
    },
    
    saveSettings(settings) {
      this.settings = settings
      localStorage.setItem('easychat-settings', JSON.stringify(settings))
      
      // Apply theme if it has changed
      if (settings.theme !== this.theme) {
        this.setTheme(settings.theme)
      }
    },
    
    initializeTheme() {
      this.applyTheme()
      
      // Listen for system preference changes
      window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
        if (this.theme === 'system') {
          this.applyTheme()
        }
      })
    }
  },
  getters: {
    isFirstApp: (state) => state.currentApp === 'first',
    isSecondApp: (state) => state.currentApp === 'second'
  }
})
