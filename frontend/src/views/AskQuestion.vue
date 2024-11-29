<script setup lang="ts">
import { ref } from 'vue'

// State variables
const title = ref('')
const content = ref('')
const isAnonymous = ref(false)
const tags = ref<string[]>([])
const selectedTags = ref<string[]>([])

// Available tags for selection
tags.value = ['Academics', 'Social Life', 'Campus Events', 'Technology', 'Other']

// Toggle anonymous mode
const toggleAnonymous = () => {
  isAnonymous.value = !isAnonymous.value
}

// Submit question function
const submitQuestion = () => {
  console.log('Submitting question:', {
    title: title.value,
    content: content.value,
    anonymous: isAnonymous.value,
    tags: selectedTags.value,
  })
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-primary text-white">
    <div class="bg-gradient-to-r from-[#00b4d1] to-[#00a1b5] rounded-lg shadow-lg p-8 w-full max-w-3xl">

    <!-- <div class="bg-[#00b4d1] bg-opacity-50 rounded-lg shadow-lg p-8 w-full max-w-3xl"> -->
        <!-- Header -->
      <div class="flex items-center justify-between mb-6">
        <!-- User Profile Picture -->
        <div class="flex items-center space-x-4">
          <img
            :src="isAnonymous ? '/src/assets/icons/anon.png' : '/src/assets/icons/user.png'"
            alt="User Profile"
            class="h-10 w-10 rounded-full border border-gray-400"
          />
          <span class="text-lg font-semibold">
            {{ isAnonymous ? 'Anonymous' : 'Username' }}
          </span>
        </div>

        <!-- Anonymous Toggle -->
        <div class="flex items-center space-x-2">
          <label for="anonymous" class="text-sm">Post Anonymously</label>
          <input
            id="anonymous"
            type="checkbox"
            v-model="isAnonymous"
            @change="toggleAnonymous"
            class="h-5 w-5 cursor-pointer"
          />
        </div>
      </div>

      <!-- Form -->
      <h1 class="text-3xl font-semibold text-center mb-6">Ask a Question</h1>
      <form @submit.prevent="submitQuestion" class="space-y-6">
        <!-- Title Input -->
        <div>
          <label for="title" class="block text-sm font-medium mb-2">Title</label>
          <input
            id="title"
            v-model="title"
            type="text"
            class="w-full px-4 py-3 rounded-md border border-gray-300 text-black focus:ring-2 focus:border-[#00a1b5] focus:outline-none"
            placeholder="What's your question?"
            required
          />
        </div>

        <!-- Details Input -->
        <div>
          <label for="content" class="block text-sm font-medium mb-2">Details</label>
          <textarea
            id="content"
            v-model="content"
            rows="6"
            class="w-full px-4 py-3 rounded-md border border-gray-300 text-black focus:ring-2 focus:ring-blue-500 focus:outline-none"
            placeholder="Provide more details about your question..."
            required
          ></textarea>
        </div>

        <!-- Tags Selection -->
        <div>
          <label class="block text-sm font-medium mb-2">Select Tags</label>
          <div class="flex flex-wrap gap-2 ">
            <button
              v-for="tag in tags"
              :key="tag"
              @click.prevent="() => selectedTags.includes(tag) ? selectedTags.splice(selectedTags.indexOf(tag), 1) : selectedTags.push(tag)"
              :class="selectedTags.includes(tag) ? 'bg-[#00b4d1] text-white' : 'bg-white text-black'"
              class="px-3 py-2 rounded-md transition-all"
            >
              {{ tag }}
            </button>
          </div>
        </div>

        <!-- Submit Button -->
        <button class="bg-[#00b4d1] text-white hover:bg-[#0099b3] w-full rounded-lg px-6 py-2 font-medium transition-all duration-300 transform hover:scale-105 shadow-lg">
        Post a question
        </button>
      </form>
    </div>
  </div>
</template>

<style scoped>
.bg-primary {
  background-color: white;
}
</style>
