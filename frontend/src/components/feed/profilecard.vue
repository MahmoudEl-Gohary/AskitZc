<script setup lang="ts">
defineProps<{
  name: string;
  friends: number;
  posts: number;
}>();
</script>

<template>
  <div class="bg-white rounded-xl shadow-lg p-6">
    <div class="flex flex-col items-center">
      <div class="w-24 h-24 rounded-full overflow-hidden mb-4">
        <img src="https://cdn4.iconfinder.com/data/icons/forum-buttons-and-community-signs-1/794/profile-3-512.png" alt="Profile" class="w-full h-full object-cover">
      </div>
      <h2 class="text-xl font-bold mb-4">{{ name }}</h2>
      <div class="flex space-x-8 text-gray-600">
        <div class="text-center">
          <div class="font-bold">{{ friends }}</div>
          <div class="text-sm">friends</div>
        </div>
        <div class="text-center">
          <div class="font-bold">{{ posts }}</div>
          <div class="text-sm">posts</div>
        </div>
      </div>
    </div>
  </div>
</template>