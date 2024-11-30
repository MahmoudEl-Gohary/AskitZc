<script setup lang="ts">
import { ref } from 'vue'
import { RouterLink } from 'vue-router';

const firstName = ref('')
const lastName = ref('')
const email = ref('')
const password = ref('')
const verifyPassword = ref('')

const handleGoogleSignIn = () => {
  console.log('Signing in with Google');
  // TODO: Implement Google Sign-In logic (e.g., redirect to Google Auth)
};

const handleSignUp = () => {
  // Simple password verification logic
  if (password.value !== verifyPassword.value) {
    console.log('Passwords do not match!');
    return;
  }
  
  console.log('Sign-up attempt:', { firstName: firstName.value, lastName: lastName.value, email: email.value, password: password.value });
};
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-r from-[#00b5d13a] to-[#00a0b5b0] bg-opacity-10 backdrop-blur-sm">
    <div class="bg-white bg-opacity-85 rounded-lg shadow-xl p-8 w-full max-w-xl">
      <div class="text-center mb-8">
        <h1 class="text-3xl font-bold text-gray-900 mb-2">Create an Account</h1>
        <p class="text-gray-600">Sign up to start using our service</p>
      </div>

      <!-- First Name and Last Name (in the same row) -->
      <div class="mb-3 flex space-x-4">
        <div class="w-1/2">
          <label for="first-name" class="block text-gray-800 text-sm font-medium mb-2">First Name</label>
          <input
            v-model="firstName"
            type="text"
            id="first-name"
            class="w-full px-4 py-3 border border-gray-300 rounded-md text-gray-900 focus:ring-2 focus:ring-[#00b4d1] focus:outline-none transition duration-200"
            placeholder="First Name"
            required
          />
        </div>

        <div class="w-1/2">
          <label for="last-name" class="block text-gray-800 text-sm font-medium mb-2">Last Name</label>
          <input
            v-model="lastName"
            type="text"
            id="last-name"
            class="w-full px-4 py-3 border border-gray-300 rounded-md text-gray-900 focus:ring-2 focus:ring-[#00b4d1] focus:outline-none transition duration-200"
            placeholder="Last Name"
            required
          />
        </div>
      </div>

      <!-- Email input -->
      <div class="mb-3">
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
      <div class="mb-3">
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

      <!-- Verify Password input -->
      <div class="mb-3">
        <label for="verify-password" class="block text-gray-800 text-sm font-medium mb-2">Verify Password</label>
        <input
          v-model="verifyPassword"
          type="password"
          id="verify-password"
          class="w-full px-4 py-3 border border-gray-300 rounded-md text-gray-900 focus:ring-2 focus:ring-[#00b4d1] focus:outline-none transition duration-200"
          placeholder="Re-enter your password"
          required
        />
      </div>

      <!-- Sign Up Button -->
      <div class="mb-4 mt-6">
        <button
          @click="handleSignUp"
          class="w-full py-3 px-4 bg-gradient-to-r from-[#00b5d198] to-[#00a0b5b0] text-white font-semibold rounded-md focus:outline-none focus:ring-2 focus:ring-[#00b4d1] hover:bg-[#008f9f] transition duration-200"
        >
          Sign Up
        </button>
      </div>

      <p class="text-center text-gray-600 my-3">or</p>

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
          Sign up with Google
        </button>
      </div>

      <!-- "Already have an account?" Section -->
      <p class="text-center text-gray-600 mt-4">
        Already have an account? 
        <RouterLink to="/login" class="text-[#00b4d1] font-semibold hover:underline">Sign In</RouterLink>
      </p>
    </div>
  </div>
</template>
