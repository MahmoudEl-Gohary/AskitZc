<script setup lang="ts">
import { RouterView } from 'vue-router'
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
</script>

<template>
  <div class="min-h-screen bg-gray-50">
    <Header />
    <main class="w-full"> <!-- Ensure full width here -->
      <RouterView />
    </main>
    <Footer />
  </div>
</template>
