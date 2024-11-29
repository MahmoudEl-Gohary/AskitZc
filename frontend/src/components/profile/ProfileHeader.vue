<script setup lang="ts">
import { ref } from 'vue'

const user = ref({
  name: 'MADO',
  username: '@DSAI_202201124',
  bio: 'Data Scientist | Football player',
  coverPhoto: 'src/assets/Images/IMG_1500.jpg',
  avatar: '/src/assets/Images/WhatsApp Image 2024-11-27 at 7.19.51 PM.png',
})
</script>

<template>
  <div class="bg-white shadow">
    <!-- Cover Photo -->
    <div class="relative h-48 md:h-64 h-150">
      <img 
        :src="user.coverPhoto"
        alt="Cover"
        class="w-full h-full object-cover"
      />
      <button class="absolute top-4 right-4 bg-white text-gray-700 px-4 py-2 rounded-lg shadow hover:bg-gray-50">
        Edit Cover
      </button>
    </div>

    <!-- Profile Info -->
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="relative -mt-12 sm:-mt-16 mb-">
        <div class="flex flex-col sm:flex-row items-center sm:items-end sm:space-x-5 m-5 p-3"> <!-- here -->
          <div class="relative">
            <img
              :src="user.avatar"
              alt="Profile"
              class="h-24 w-24 sm:h-32 sm:w-32 rounded-full border-4 border-white shadow-lg"
            />
            <button class="absolute bottom-0 right-0 bg-white rounded-full p-2 shadow-lg">
              <span class="text-gray-600">Edit</span>
            </button>
          </div>
            <div class="mt-4 sm:mt-0 text-center sm:text-left">
                <h1 class="text-2xl font-bold text-gray-900">{{ user.name }}</h1>
                <p class="text-gray-500">{{ user.username }}</p>
                <p class="mt-1 text-gray-600">{{ user.bio }}</p>
         </div>
        </div>
      </div>
    </div>
  </div>
</template>