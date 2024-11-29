<script setup lang="ts">
import { ref } from 'vue'

const email = ref('')
const password = ref('')
const handleGoogleSignIn = () => {
  console.log('Signing in with Google');
  // TODO: Implement Google Sign-In logic (e.g., redirect to Google Auth)
};

const handleLogin = () => {
  console.log('Login attempt:', { email: email.value, password: password.value })
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-white">
    <div class="bg-gradient-to-r from-[#00b4d1] to-[#00a1b5] bg-opacity-10 backdrop-blur-sm rounded-lg shadow-xl p-8 w-full max-w-md">
      <div class="text-center mb-8">
        <h1 class="text-3xl font-bold text-white mb-2">Welcome Back</h1>
        <p class="text-gray-200">Sign in to your account</p>
      </div>
        <div>
          <button
        @click="handleGoogleSignIn"
        class="w-full flex items-center justify-center py-3 px-4 border border-gray-700 rounded-md shadow-sm text-sm font-medium text-white bg-accent hover:bg-accent-dark focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-accent-light"
      >
        <img
          src="/src/assets/icons/google-logo-png-open-2000.png"
          alt="Google Icon"
          class="w-5 h-5 mr-3"
        />
        Sign in with Google
      </button>
        </div>
    </div>
  </div>
</template>