<script setup lang="ts">
import ProfileHeader from '../components/profile/ProfileHeader.vue'
import UserQuestions from '../components/profile/UserQuestion.vue'
// import UserAnswers from '../components/profile/UserAnswer.vue'
import signedHeader from '../components/signedHeader.vue';
</script>

<template>
  <signedHeader />
  <div class="min-h-screen bg-gray-50">
    <ProfileHeader />
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="space-y-6">
        <UserQuestions />
        <!-- <UserAnswers /> -->
      </div>
    </div>
  </div>
</template>

