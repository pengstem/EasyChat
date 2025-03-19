<script setup>
defineEmits(['toggle-settings'])
</script>

<template>
    <header class="app-header">
        <div class="header-content">
            <h1 class="app-title">EasyChat</h1>
            <button class="settings-btn" @click="$emit('toggle-settings')">
                <span class="material-icons">settings</span>
            </button>
        </div>
    </header>
</template>

<style scoped>
.app-header {
    background-color: var(--bg-primary);
    border-bottom: 1px solid var(--border-color);
    padding: 2px 1rem;
}

.header-content {
    display: grid;
    grid-template-columns: 1fr auto;
    align-items: center;
    gap: 1rem;
    margin: 0 auto;
}

.app-title {
    font-size: 1.5rem;
    font-weight: 600;
    width:110px ;
    margin: 0;
    color: var(--text-primary);
}

.settings-btn {
    background: none;
    border: none;
    color: var(--text-secondary);
    cursor: pointer;
    padding: 0.5rem;
    border-radius: 50%;
    transition: background-color 0.2s;
}

.settings-btn:hover {
    background-color: var(--bg-hover);
}
</style>