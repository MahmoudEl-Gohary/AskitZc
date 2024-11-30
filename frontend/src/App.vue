<script setup>
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
    <Toast />
    <Footer />
  </div>
</template>

<script>
import Toast from '@/components/Toast.vue';

  export default {
    components: {
      Toast
    }
  }
</script>
