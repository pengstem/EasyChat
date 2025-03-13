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
  display: flex;
  flex-direction: column;
  height: 100vh;
  background-color: var(--bg-primary);
  color: var(--text-primary);
}

.main-content {
  display: flex;
  flex: 1;
  overflow: hidden;
}

.chat-container {
  display: flex;
  flex-direction: column;
  flex: 1;
  overflow: hidden;
  background-color: var(--bg-secondary);
}
</style>
