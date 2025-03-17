import { defineStore } from 'pinia'

export const useThemeStore = defineStore('theme', {
  state: () => ({
    savedTheme: localStorage.getItem('easychat-theme') || 'system',
    currentTheme: localStorage.getItem('easychat-theme') || 'system',
    
    settings: JSON.parse(localStorage.getItem('easychat-settings')) || {
      theme: 'system',
      language: 'en',
    },
    hasUnsavedChanges: false
  }),
  
  getters: {
    effectiveTheme: (state) => {
      const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches
      
      if (state.currentTheme === 'system') {
        return prefersDark ? 'dark' : 'light'
      }
      return state.currentTheme
    },
    isThemeModified: (state) => {
      return state.currentTheme !== state.savedTheme
    }
  },
  
  actions: {
    previewTheme(theme) {
      this.currentTheme = theme
      this.hasUnsavedChanges = this.isThemeModified
      this.applyTheme()
    },
    
    applyTheme() {
      document.documentElement.classList.remove('light-theme', 'dark-theme')
      const themeToApply = this.effectiveTheme
      document.documentElement.classList.add(`${themeToApply}-theme`)
    },
    
    cancelChanges() {
      this.currentTheme = this.savedTheme
      this.hasUnsavedChanges = false
      this.applyTheme()
    },
    
    saveTheme() {
      this.savedTheme = this.currentTheme
      localStorage.setItem('easychat-theme', this.currentTheme)
      this.hasUnsavedChanges = false
    },
    
    saveSettings(settings) {
      this.settings = { ...settings }
      localStorage.setItem('easychat-settings', JSON.stringify(settings))
      
      if (settings.theme !== this.savedTheme) {
        this.currentTheme = settings.theme
        this.saveTheme()
      }
      this.hasUnsavedChanges = false
    },
    
  }
})
