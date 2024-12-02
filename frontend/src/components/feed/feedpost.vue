<script>
import axios from 'axios'
import signedHeader from '../../components/signedHeader.vue'
export default {
    name: 'FeedView',

    components: {
        signedHeader,
    },
    data() {
        return {
            posts: [],
            body: '',
            title: '',
        }
    },

    mounted() {
        this.getFeed()
    },

    methods: {
        getFeed() {
            axios
                .get('/api/posts/')
                .then(response => {
                    console.log('data', response.data)

                    this.posts = response.data
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
        submitForm() {
            console.log("submitting form", this.body)
            console.log("submitting form", this.title)

            axios
                .post('api/posts/create/',{
                        'title': this.title,
                        'body': this.body
                    })
                .then(response => {
                  console.log('POST response data:', response.data);
                  this.posts.unshift(response.data);
                  this.title = '';
                  this.body = '';
                })
                .catch(error => {
                    console.log('error', error)
                })
        }
    }
}
</script>

<template>
  <form method="post" v-on:submit.prevent="submitForm" class="bg-white rounded-xl shadow-lg p-6 mb-6 w-full md:w-full">
    <div class="space-y-4">
      <div class="flex items-center space-x-4">
        <div class="w-10 h-10 rounded-full overflow-hidden">
          <img src="https://cdn4.iconfinder.com/data/icons/forum-buttons-and-community-signs-1/794/profile-3-512.png" alt="Profile" class="w-full h-full object-cover">
        </div>
        <input
          type="text"
          v-model="title"
          placeholder="Title"
          class="w-full bg-gray-100 rounded-full px-6 py-3 focus:outline-none focus:ring-2 focus:ring-purple-500"
        >
      </div>

      <textarea
        v-model="body"
        placeholder="What are you thinking about?"
        class="w-full bg-gray-100 rounded-full px-6 py-3 focus:outline-none focus:ring-2 focus:ring-purple-500"
      ></textarea>
    </div>
    
    <div class="flex justify-between mt-4">
      <div class="flex items-center space-x-2">
        <label for="anonymous" class="text-sm text-gray-700">Post Anonymously</label>
        <input
          id="anonymous"
          type="checkbox"
          v-model="anonymous"
          class="h-4 w-4 cursor-pointer rounded border-gray-300 text-blue-600 focus:ring-blue-500"
        />
      </div>
      <button
        class="px-6 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700 transition-colors"
      >
        Post
      </button>
    </div>
  </form>

  <div
    v-for="post in posts"
    v-bind:key="post.id"
    class="bg-white rounded-xl shadow-lg overflow-hidden mb-4">
    <!-- Post Header -->
    <div class="p-4 flex justify-between items-center">
      <div class="flex items-center space-x-3">
        <div class="w-10 h-10 rounded-full overflow-hidden">
          <img src="https://cdn4.iconfinder.com/data/icons/forum-buttons-and-community-signs-1/794/profile-3-512.png" :alt="author" class="w-full h-full object-cover">
        </div>
        <div>
          <h3 class="font-semibold">{{ post.created_by.name  }}</h3>
          <span class="text-sm text-gray-500">{{ post.created_at_formated }} ago</span>
        </div>
      </div>
      <button 
        @click="isMenuOpen = !isMenuOpen"
        class="text-gray-500 hover:text-gray-700"
      >
        ⋮
      </button>
    </div>

  <!-- Post Content -->
<!-- Post Content -->
<div class="px-4 py-3 space-y-3">
  <h4 class="text-2xl font-semibold text-gray-900 leading-tight">{{ post.title }}</h4> <!-- Post Title -->
  <p class="text-gray-800 text-base leading-relaxed">{{ post.body }}</p> <!-- Post Body -->
</div>


    <!-- Post Actions -->
    <div class="px-4 py-3 flex items-center space-x-6 text-gray-500">
      <button class="flex items-center space-x-2 hover:text-gray-700">
        <span>♡</span>
        <span>{{ likes }} likes</span>
      </button>
      <button class="flex items-center space-x-2 hover:text-gray-700">
        <span>💬</span>
        <span>{{ comments }} comments</span>
      </button>
    </div>
  </div>
</template>