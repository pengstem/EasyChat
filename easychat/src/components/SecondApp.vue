<script setup>
import { ref } from 'vue'

const message = ref('Second Vue App')
const count = ref(0)
</script>

<template>
  <div class="second-app">
    <h1>{{ message }}</h1>
    <div class="card">
      <button type="button" @click="count++">Second app count is {{ count }}</button>
      <p>
        This is a separate Vue application instance with its own state.
      </p>
    </div>
  </div>
</template>

<style scoped>
.second-app {
  padding: 2rem;
  background-color: #f0f8ff;
  border-radius: 8px;
  margin-top: 2rem;
}

h1 {
  color: #42b883;
}

.card {
  padding: 1.5rem;
  background-color: white;
  border-radius: 6px;
}
</style>
