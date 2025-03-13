<script setup>
import { ref } from 'vue'

const emit = defineEmits(['close'])

const settings = ref({
  theme: 'dark',
  fontSize: 'medium',
  language: 'en',
  notifications: true
})

const themes = [
  { value: 'light', label: 'Light' },
  { value: 'dark', label: 'Dark' },
  { value: 'system', label: 'System' }
]

const languages = [
  { value: 'en', label: 'English' },
  { value: 'cn', label: '简体中文' },
]

const saveSettings = () => {
  // Here you would typically save settings to localStorage or backend
  localStorage.setItem('easychat-settings', JSON.stringify(settings.value))
  emit('close')
}
</script>

<template>
  <div class="settings-overlay">
    <div class="settings-modal">
      <div class="settings-header">
        <h2>Settings</h2>
        <button class="close-button" @click="emit('close')">
          <span class="material-icons">close</span>
        </button>
      </div>
      
      <div class="settings-content">
        <div class="setting-group">
          <h3>Theme</h3>
          <select v-model="settings.theme">
            <option v-for="theme in themes" :key="theme.value" :value="theme.value">
              {{ theme.label }}
            </option>
          </select>
        </div>

        <div class="setting-group">
          <h3>Language</h3>
          <select v-model="settings.language">
            <option v-for="lang in languages" :key="lang.value" :value="lang.value">
              {{ lang.label }}
            </option>
          </select>
        </div>

        <div class="setting-group">
          <h3>Notifications</h3>
          <label class="toggle-switch">
            <input type="checkbox" v-model="settings.notifications">
            <span class="toggle-slider"></span>
          </label>
        </div>
      </div>

      <div class="settings-footer">
        <button class="cancel-button" @click="emit('close')">Cancel</button>
        <button class="save-button" @click="saveSettings">Save Changes</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.settings-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.settings-modal {
  background-color: var(--bg-primary);
  border-radius: 12px;
  width: 90%;
  max-width: 500px;
  max-height: 90vh;
  display: flex;
  flex-direction: column;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.settings-header {
  padding: 1rem;
  border-bottom: 1px solid var(--border-color);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.settings-header h2 {
  margin: 0;
  font-size: 1.5rem;
}

.close-button {
  background: none;
  border: none;
  color: var(--text-secondary);
  cursor: pointer;
  padding: 0.5rem;
  border-radius: 50%;
  transition: background-color 0.2s;
}

.close-button:hover {
  background-color: var(--bg-hover);
}

.settings-content {
  padding: 1rem;
  overflow-y: auto;
}

.setting-group {
  margin-bottom: 1.5rem;
}

.setting-group h3 {
  margin: 0 0 0.5rem 0;
  font-size: 1rem;
}

select {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid var(--border-color);
  border-radius: 6px;
  background-color: var(--bg-secondary);
  color: var(--text-primary);
}

.toggle-switch {
  position: relative;
  display: inline-block;
  width: 50px;
  height: 24px;
}

.toggle-switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.toggle-slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: var(--bg-secondary);
  transition: .4s;
  border-radius: 24px;
}

.toggle-slider:before {
  position: absolute;
  content: "";
  height: 16px;
  width: 16px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  transition: .4s;
  border-radius: 50%;
}

input:checked + .toggle-slider {
  background-color: var(--primary-color);
}

input:checked + .toggle-slider:before {
  transform: translateX(26px);
}

.settings-footer {
  padding: 1rem;
  border-top: 1px solid var(--border-color);
  display: flex;
  justify-content: flex-end;
  gap: 0.5rem;
}

.cancel-button, .save-button {
  padding: 0.5rem 1rem;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.cancel-button {
  background-color: var(--bg-secondary);
  border: 1px solid var(--border-color);
  color: var(--text-primary);
}

.save-button {
  background-color: var(--primary-color);
  border: none;
  color: white;
}

.save-button:hover {
  background-color: var(--primary-color-dark);
}
</style>
