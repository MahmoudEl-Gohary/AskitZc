<script>
import { ref } from 'vue'
import { RouterLink } from 'vue-router';
import axios from 'axios'

import { useToastStore } from '@/stores/toast'

export default {
    setup() {
        const toastStore = useToastStore()

        return {
            toastStore
        }
    },

    data() {
        return {
            form: {
                email: '',
                name: '',
                password1: '',
                password2: ''
            },
            errors: [],
        }
    },

    methods: {
        submitForm() {
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('Your e-mail is missing')
            }

            if (this.form.name === '') {
                this.errors.push('Your name is missing')
            }

            if (this.form.password1 === '') {
                this.errors.push('Your password is missing')
            }

            if (this.form.password1 !== this.form.password2) {
                this.errors.push('The password does not match')
            }

            if (this.errors.length === 0) {
                axios
                    .post('/api/signup/', this.form)
                    .then(response => {
                        if (response.data.message === 'success') {
                            this.toastStore.showToast(5000, 'The user is registered. Please activate your account by clicking your email link.', 'bg-emerald-500')

                            this.form.email = ''
                            this.form.name = ''
                            this.form.password1 = ''
                            this.form.password2 = ''
                        } else {
                            const data = JSON.parse(response.data.message)
                            for (const key in data){
                                this.errors.push(data[key][0].message)
                            }

                            this.toastStore.showToast(5000, 'Something went wrong. Please try again', 'bg-red-300')
                        }
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
    }
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-r from-[#00b5d13a] to-[#00a0b5b0] bg-opacity-10 backdrop-blur-sm">
    <form class="bg-white bg-opacity-85 rounded-lg shadow-xl p-8 w-full max-w-xl" v-on:submit.prevent="submitForm">
      <div class="text-center mb-8">
        <h1 class="text-3xl font-bold text-gray-900 mb-2">Create an Account</h1>
        <p class="text-gray-600">Sign up to start using our service</p>
      </div>

      <div class="mb-6">
        <label for="name" class="block text-gray-800 text-sm font-medium mb-2">Full Name</label>
        <input
          v-model="form.name"
          type="text"
          id="name"
          class="w-full px-4 py-3 border border-gray-300 rounded-md text-gray-900 focus:ring-2 focus:ring-[#00b4d1] focus:outline-none transition duration-200"
          placeholder="Enter your full name"
          required
        />
      </div>
      <!-- Email input -->
      <div class="mb-3">
        <label for="email" class="block text-gray-800 text-sm font-medium mb-2">Email</label>
        <input
          v-model="form.email"
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
          v-model="form.password1"
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
          v-model="form.password2"
          type="password"
          id="verify-password"
          class="w-full px-4 py-3 border border-gray-300 rounded-md text-gray-900 focus:ring-2 focus:ring-[#00b4d1] focus:outline-none transition duration-200"
          placeholder="Re-enter your password"
          required
        />
      </div>

      <!-- Error Messages -->
      <div v-if="errors.length > 0" class="mb-4">
        <div v-for="error in errors" :key="error" class="text-red-500 text-sm font-semibold">
          {{ error }}
        </div>
      </div>

      <!-- Sign Up Button -->
      <div class="mb-4 mt-6">
        <button
          type="submit"
          class="w-full py-3 px-4 bg-gradient-to-r from-[#00b5d198] to-[#00a0b5b0] text-white font-semibold rounded-md focus:outline-none focus:ring-2 focus:ring-[#00b4d1] hover:bg-[#008f9f] transition duration-200"
        >
          Sign Up
        </button>
      </div>

      <p class="text-center text-gray-600 my-3">or</p>

      <!-- Google Sign-In Button -->
      <div>
        <button
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
    </form>
  </div>
</template>

