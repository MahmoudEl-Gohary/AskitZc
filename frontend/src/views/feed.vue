<script setup lang="ts">
import signedHeader from '../components/signedHeader.vue';
import ProfileCard from '../components/feed/profilecard.vue';
import Feed from '../components/feed/feedpost.vue';
</script>


<template>
  <div class="min-h-screen bg-gray-100">
    <signedHeader />
    
    <main class="container mx-auto px-4 py-8 w-full md:w-full">
      <div class="grid grid-cols-1 md:grid-cols-12 gap-6">
        <!-- Left Sidebar -->
        <div class="md:col-span-3">
          <ProfileCard name="Code With Stein" :friends="182" :posts="120" />
        </div>

        <!-- Main Content -->
        <div class="md:col-span-6 w-full">
          <!-- <CreatePost /> -->
          <Feed />
        </div>

        <!-- Right Sidebar -->
        <!-- <div class="md:col-span-3">
          <SuggestedUsers />
          <Trends />
        </div> -->
      </div>
    </main>
  </div>
</template>