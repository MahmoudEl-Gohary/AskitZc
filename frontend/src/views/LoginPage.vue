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
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-r from-[#00b5d13a] to-[#00a0b5b0] bg-opacity-10 backdrop-blur-sm">
    <div class="bg-white bg-opacity-85 rounded-lg shadow-xl p-8 w-full max-w-xl">
      <div class="text-center mb-8">
        <h1 class="text-3xl font-bold text-gray-900 mb-2">Welcome Back</h1>
        <p class="text-gray-600">Sign in to your account</p>
      </div>

      <!-- Email input -->
      <div class="mb-6">
        <label for="email" class="block text-gray-800 text-sm font-medium mb-2">Email</label>
        <input
          v-model="email"
          type="email"
          id="email"
          class="w-full px-4 py-3 border border-gray-300 rounded-md text-gray-900 focus:ring-2 focus:ring-[#00b4d1] focus:outline-none transition duration-200"
          placeholder="Enter your email"
          required
        />
      </div>

      <!-- Password input -->
      <div class="mb-6">
        <label for="password" class="block text-gray-800 text-sm font-medium mb-2">Password</label>
        <input
          v-model="password"
          type="password"
          id="password"
          class="w-full px-4 py-3 border border-gray-300 rounded-md text-gray-900 focus:ring-2 focus:ring-[#00b4d1] focus:outline-none transition duration-200"
          placeholder="Enter your password"
          required
        />
      </div>

      <!-- Login Button -->
      <div class="mb-6">
        <button
          @click="handleLogin"
          class="w-full py-3 px-4 bg-gradient-to-r from-[#00b5d198] to-[#00a0b5b0] text-white font-semibold rounded-md focus:outline-none focus:ring-2 focus:ring-[#00b4d1] hover:bg-[#008f9f] transition duration-200"
        >
          Sign in
        </button>
      </div>

      <p class="text-center text-gray-600 my-4">or</p>

      <!-- Google Sign-In Button -->
      <div>
        <button
          @click="handleGoogleSignIn"
          class="w-full flex items-center justify-center py-3 px-4 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-[#00b4d1] transition duration-200"
        >
          <img
            src="/src/assets/icons/google-logo-png-open-2000.png"
            alt="Google Icon"
            class="w-5 h-5 mr-3"
          />
          Sign in with Google
        </button>
      </div>

      <!-- Don't have an account? Section -->
      <p class="text-center text-gray-600 mt-4">
        Don't have an account? 
        <RouterLink to="/signup" class="text-[#00b4d1] font-semibold hover:underline">Sign Up</RouterLink>
      </p>
    </div>
  </div>
</template>
