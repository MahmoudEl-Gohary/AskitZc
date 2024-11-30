<script>
  import { RouterView } from 'vue-router'
  import Header from './components/Header.vue'
  import Footer from './components/Footer.vue'
  import axios from 'axios'
  import Toast from '@/components/Toast.vue'
  import { useUserStore } from '@/stores/user'

  export default {
    
      setup() {
          const userStore = useUserStore()

          return {
              userStore
          }
      },

      components: {
          Toast,
          Header,
          Footer
      },

      beforeCreate() {
          this.userStore.initStore()

          const token = this.userStore.user.access

          if (token) {
              axios.defaults.headers.common["Authorization"] = "Bearer " + token;
          } else {
              axios.defaults.headers.common["Authorization"] = "";
          }
      }
  }
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

