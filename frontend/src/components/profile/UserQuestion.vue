<script setup lang="ts">
import { ref } from 'vue'

const questions = ref([
  {
    id: 1,
    title: 'How to implement Vue 3 Composition API?',
    content: 'I am trying to understand the best practices...',
    votes: 15,
    answers: 3,
    date: '2024-03-15',
  },
  {
    id: 2,
    title: 'Vite vs Webpack for Vue applications',
    content: 'What are the main differences between...',
    votes: 8,
    answers: 5,
    date: '2024-03-10',
  },
])
</script>

<template>
  <div class="bg-white rounded-lg shadow p-6">
    <h2 class="text-xl font-bold text-gray-900 mb-4">My Questions</h2>
    <div class="space-y-4">
      <div v-for="question in questions" :key="question.id" class="border-b pb-4 last:border-0">
        <h3 class="text-lg font-semibold text-gray-900">{{ question.title }}</h3>
        <p class="text-gray-600 mt-1">{{ question.content }}</p>
        <div class="flex items-center space-x-4 mt-2 text-sm text-gray-500">
          <span>{{ question.votes }} votes</span>
          <span>{{ question.answers }} answers</span>
          <span>{{ question.date }}</span>
        </div>
      </div>
    </div>
  </div>
</template>