<script setup>
import { ref } from 'vue'

const emit = defineEmits(['select-chat'])

const chats = ref([
  { id: 3, title: 'General Chat'},
  { id: 2, title: 'Code Assistant'},
  { id: 1, title: 'Writing Helper'}
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
  }
  chats.value.unshift(newChat)
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
        <div class="chat-info">
          <h3>{{ chat.title }}</h3>
        </div>
      </div>
    </div>
  </aside>
</template>
<style scoped>
.sidebar {
    width: 240px;
    background-color: var(--bg-primary);
    border-right: 1px solid var(--border-color);
    display: grid;
    grid-template-rows: auto 1fr;
    overflow-y: auto;
}

.new-chat-btn {
    margin: 0.5rem;
    padding: 0.5rem;
    background-color: var(--primary-color);
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    display: grid;
    grid-template-columns: auto 1fr;
    height: 45px;
    gap: 0.5rem;
    align-items: center;
    transition: background-color 0.2s;
    font-size: x-large;
    font-family: monospace;
}

.new-chat-btn:hover {
    background-color: var(--primary-color-dark);
}

.chat-list {
    overflow-y: auto;
    display: grid;
    grid-template-rows: repeat(auto-fill, minmax(50px, 50px));
    gap: 1px;
}

.chat-item {
    display: grid;
    height: 50px;
    align-items: center;
    cursor: pointer;
    transition: background-color 0.2s;
    border-radius: 8px;
    margin:2px 8px;
    padding: 0 1rem;

}

.chat-item:hover {
    background-color: var(--bg-hover);
}

.chat-item.active {
    background-color: var(--bg-active);
}

.chat-info {
    overflow: hidden;
    display: grid;
    grid-template-rows: auto auto;
}

.chat-info h3 {
    margin: 10px 0px;
    font-size: 1rem;
    color: var(--text-primary);
}

</style>
