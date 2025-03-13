<script setup>
import { ref } from 'vue'

const props = defineProps({
  currentChat: {
    type: Object,
    default: null
  }
})

const emit = defineEmits(['send-message'])

const message = ref('')
const isTyping = ref(false)

const sendMessage = () => {
  if (!message.value.trim() || !props.currentChat) return

  emit('send-message', {
    content: message.value,
    timestamp: new Date().toISOString()
  })

  message.value = ''
}

const handleKeydown = (e) => {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault()
    sendMessage()
  }
}
</script>

<template>
  <div class="type-zone">
    <div class="input-container">
      <textarea
        v-model="message"
        placeholder="Type your message..."
        @keydown="handleKeydown"
        @focus="isTyping = true"
        @blur="isTyping = false"
        :disabled="!currentChat"
      ></textarea>
      <button
        class="send-button"
        @click="sendMessage"
        :disabled="!message.trim() || !currentChat"
      >
        <span class="material-icons">send</span>
      </button>
    </div>
  </div>
</template>

<style scoped>
.type-zone {
  padding: 1rem;
  background-color: var(--bg-primary);
  border-top: 1px solid var(--border-color);
}

.input-container {
  display: flex;
  gap: 0.5rem;
  align-items: flex-end;
}

textarea {
  flex: 1;
  min-height: 40px;
  max-height: 200px;
  padding: 0.75rem;
  border: 1px solid var(--border-color);
  border-radius: 8px;
  background-color: var(--bg-secondary);
  color: var(--text-primary);
  resize: none;
  font-family: inherit;
  font-size: 1rem;
  line-height: 1.5;
}

textarea:focus {
  outline: none;
  border-color: var(--primary-color);
}

textarea:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.send-button {
  padding: 0.75rem;
  background-color: var(--primary-color);
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.send-button:hover:not(:disabled) {
  background-color: var(--primary-color-dark);
}

.send-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
</style>
