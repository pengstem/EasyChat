<script setup>
import { ref, onMounted, nextTick } from 'vue'

const props = defineProps({
  currentChat: {
    type: Object,
    default: null
  }
})

const messages = ref([])
const chatContainer = ref(null)

const scrollToBottom = async () => {
  await nextTick()
  if (chatContainer.value) {
    chatContainer.value.scrollTop = chatContainer.value.scrollHeight
  }
}

onMounted(() => {
  scrollToBottom()
})

// Mock messages for demonstration
const mockMessages = [
  {
    id: 1,
    content: 'Hello! How can I help you today?',
    type: 'ai',
    timestamp: new Date().toISOString()
  },
  {
    id: 2,
    content: 'I need help with my code.',
    type: 'user',
    timestamp: new Date().toISOString()
  }
]

// Initialize with mock messages
messages.value = mockMessages
</script>

<template>
  <div class="chat-window" ref="chatContainer">
    <div v-if="currentChat" class="chat-messages">
      <div
        v-for="message in messages"
        :key="message.id"
        class="message"
        :class="message.type"
      >
        <div class="message-content">
          <div class="message-text">{{ message.content }}</div>
          <div class="message-time">
            {{ new Date(message.timestamp).toLocaleTimeString() }}
          </div>
        </div>
      </div>
    </div>
    <div v-else class="no-chat-selected">
      <p>Select a chat or start a new conversation</p>
    </div>
  </div>
</template>
<style scoped>
.chat-window {
  flex: 1;
  overflow-y: auto;
  padding: 1rem;
}

.chat-messages {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.message {
  display: flex;
  margin-bottom: 1rem;
  max-width: 80%;
}

.message.user {
  margin-left: auto;
}

.message-content {
  padding: 0.75rem 1rem;
  border-radius: 1rem;
}

.message.user .message-content {
  background-color: var(--text-background);
  color: white;
  border-radius: 1.5rem;
}

.message-text {
  margin-bottom: 0.25rem;
  line-height: 1.4;
  color: var(--text-primary);
}

.message-time {
  font-size: 0.75rem;
  opacity: 0.7;
  color: var(--text-secondary);
}

.no-chat-selected {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  color: var(--text-secondary);
  gap: 1rem;
}

.no-chat-selected .material-icons {
  font-size: 3rem;
}
</style>
