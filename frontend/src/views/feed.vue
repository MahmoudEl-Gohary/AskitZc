<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';
import signedHeader from '../components/signedHeader.vue';

// General feed data (questions and answers)
const feedItems = ref<Array<{
  id: number;
  title: string;
  content: string;
  votes: number;
  answers: number;
  date: string;
  author: string;
  type: 'question' | 'answer';
}>>([]);

// Fetch feed data from an API (mocked for now)
const fetchFeed = async () => {
  try {
    // Mock API response
    feedItems.value = [
      {
        id: 1,
        title: 'How to implement Vue 3 Composition API?',
        content: 'I am trying to understand the best practices...',
        votes: 15,
        answers: 3,
        date: '2024-03-15',
        author: 'John Doe',
        type: 'question',
      },
      {
        id: 2,
        title: 'How to handle authentication in Vue?',
        content: 'You can implement authentication using Vue Router guards...',
        votes: 7,
        answers: 1,
        date: '2024-03-12',
        author: 'Jane Smith',
        type: 'answer',
      },
      {
        id: 3,
        title: 'Vite vs Webpack for Vue applications',
        content: 'What are the main differences between these build tools?',
        votes: 8,
        answers: 5,
        date: '2024-03-10',
        author: 'Alice Johnson',
        type: 'question',
      },
    ];
  } catch (error) {
    console.error('Failed to fetch feed data:', error);
  }
};

// Fetch feed data on component mount
onMounted(() => {
  fetchFeed();
});
</script>

<template>
    <signedHeader />
  <div class="min-h-screen bg-gradient-to-b from-gray-100 to-gray-300 py-10">
    <div class="container mx-auto px-6">
      <h1 class="text-4xl font-extrabold text-center text-gray-900 mb-12">Community Feed</h1>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <!-- Feed Items -->
        <div
          v-for="item in feedItems"
          :key="item.id"
          class="bg-white rounded-xl shadow-lg overflow-hidden hover:shadow-xl transition-shadow duration-300 group"
        >
          <!-- Header -->
          <div
            class="p-4 bg-gradient-to-r from-blue-500 from-[#00b4d1] to-[#00a1b5] text-white text-sm flex justify-between items-center"
          >
            <span>{{ item.author }}</span>
            <span
              class="px-3 py-1 rounded-full bg-white text-xs font-semibold text-gray-800"
              :class="item.type === 'question' ? 'text-blue-600' : 'text-green-600'"
            >
              {{ item.type === 'question' ? 'Question' : 'Answer' }}
            </span>
          </div>

          <!-- Content -->
          <div class="p-6">
            <h2 class="text-lg font-bold text-gray-900 mb-3 group-hover:text-blue-500 transition-colors">
              {{ item.title }}
            </h2>
            <p class="text-gray-600 line-clamp-3">
              {{ item.content }}
            </p>
          </div>

          <!-- Footer -->
          <div class="p-4 bg-gray-50 border-t text-sm text-gray-500 flex justify-between items-center">
            <div>
              <span class="font-semibold">{{ item.votes }} votes</span>
              <span v-if="item.type === 'question'"> • {{ item.answers }} answers</span>
            </div>
            <span>{{ item.date }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Line clamping for content */
.line-clamp-3 {
  display: -webkit-box;
  /* -webkit-line-clamp: 3; */
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* Box shadow hover effect */
.hover\:shadow-xl:hover {
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
}
</style>
