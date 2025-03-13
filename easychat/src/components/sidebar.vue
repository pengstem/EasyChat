<script setup>
import { ref } from 'vue'

const emit = defineEmits(['select-chat'])

const chats = ref([
  { id: 1, title: 'General Chat', lastMessage: 'Hello!' },
  { id: 2, title: 'Code Assistant', lastMessage: 'How can I help you?' },
  { id: 3, title: 'Writing Helper', lastMessage: 'Let\'s improve your writing.' }
])

const selectedChat = ref(null)

const selectChat = (chat) => {
  selectedChat.value = chat
  emit('select-chat', chat)
}

const createNewChat = () => {
  const newChat = {
    id: chats.value.length + 1,
    title: 'New Chat',
    lastMessage: 'Start a new conversation'
  }
  chats.value.push(newChat)
  selectChat(newChat)
}
</script>

<template>
  <aside class="sidebar">
    <button class="new-chat-btn" @click="createNewChat">
      <span class="material-icons">add</span>
      New Chat
    </button>
    <div class="chat-list">
      <div
        v-for="chat in chats"
        :key="chat.id"
        class="chat-item"
        :class="{ active: selectedChat?.id === chat.id }"
        @click="selectChat(chat)"
      >
        <span class="material-icons">chat</span>
        <div class="chat-info">
          <h3>{{ chat.title }}</h3>
          <p>{{ chat.lastMessage }}</p>
        </div>
      </div>
    </div>
  </aside>
</template>

<style scoped>
.sidebar {
  width: 300px;
  background-color: var(--bg-primary);
  border-right: 1px solid var(--border-color);
  display: flex;
  flex-direction: column;
  overflow-y: auto;
}

.new-chat-btn {
  margin: 1rem;
  padding: 0.75rem;
  background-color: var(--primary-color);
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: background-color 0.2s;
}

.new-chat-btn:hover {
  background-color: var(--primary-color-dark);
}

.chat-list {
  flex: 1;
  overflow-y: auto;
}

.chat-item {
  padding: 1rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  cursor: pointer;
  transition: background-color 0.2s;
}

.chat-item:hover {
  background-color: var(--bg-hover);
}

.chat-item.active {
  background-color: var(--bg-active);
}

.chat-info {
  flex: 1;
  overflow: hidden;
}

.chat-info h3 {
  margin: 0;
  font-size: 1rem;
  color: var(--text-primary);
}

.chat-info p {
  margin: 0;
  font-size: 0.875rem;
  color: var(--text-secondary);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
