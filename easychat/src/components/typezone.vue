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
        placeholder="Anything Anywhere Anytime  EasyChat"
        @keydown="handleKeydown"
        @focus="isTyping = true"
        @blur="isTyping = false"
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
  background-color: none;
}

.input-container {
  display: flex;
  gap: 0.5rem;
  align-items: flex-end;
}

textarea {
  flex: 1;
  min-height: 50px;
  max-height: 200px;
  border: 1px solid var(--border-color);
  border-radius: 50q;
  background-color: var(--bg-secondary);
  color: var(--text-primary);
  resize: none;
  font-family: inherit;
  font-size: 1rem;
  padding-top:1rem;
  padding-left: 1.4rem;
  padding-right: 1.3rem;
}


textarea:focus {
  outline: none;
  border-color: var(--primary-color);
}


.send-button {
  padding: 0.75rem;
  background-color: var(--primary-color);
  color: white;
  border: none;
  height: 57.33px;
  width: 57.33px;
  border-radius: 50%;
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
