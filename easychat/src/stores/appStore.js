import { defineStore } from 'pinia'

export const useAppStore = defineStore('app', {
  state: () => ({
    currentApp: 'first' // 'first' or 'second'
  }),
  actions: {
    toggleApp() {
      this.currentApp = this.currentApp === 'first' ? 'second' : 'first'
    }
  },
  getters: {
    isFirstApp: (state) => state.currentApp === 'first',
    isSecondApp: (state) => state.currentApp === 'second'
  }
})
