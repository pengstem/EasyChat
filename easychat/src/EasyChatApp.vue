<script setup>
import { ref } from 'vue'
import Header from './components/header.vue'
import Sidebar from './components/sidebar.vue'
import ChatWindow from './components/chatwindow.vue'
import TypeZone from './components/typezone.vue'
import Setting from './components/setting.vue'

const showSettings = ref(false)
const currentChat = ref(null)

const toggleSettings = () => {
  showSettings.value = !showSettings.value
}

const selectChat = (chat) => {
  currentChat.value = chat
}
</script>

<template>
  <div class="app-container">
    <Header @toggle-settings="toggleSettings" />
    <div class="main-content">
      <Sidebar @select-chat="selectChat" />
      <div class="chat-container">
        <ChatWindow :current-chat="currentChat" />
        <TypeZone :current-chat="currentChat" />
      </div>
    </div>
    <Setting v-if="showSettings" @close="toggleSettings" />
  </div>
</template>

<style scoped>
.app-container {
  display: grid;
  grid-template-rows: 1fr 20fr;
  height: 100vh;
  background-color: var(--bg-primary);
  color: var(--text-primary);
}

.main-content {
  display: grid;
  grid-template-columns: auto 1fr;
  overflow: hidden;
}

.chat-container {
  display: grid;
  grid-template-rows: 1fr auto;
  overflow: hidden;
  background-color: var(--bg-secondary);
}
</style>
