<template>
  <div class="bg-white shadow">
    <!-- Cover Photo -->
    <div class="relative h-48 md:h-64 h-150">
      <img 
        src="../../assets/Images/IMG_1500.jpg"
        alt="Cover"
        class="w-full h-full object-cover"
      />
    </div>

    <!-- Profile Info -->
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="relative -mt-12 sm:-mt-16 mb-">
        <div class="flex flex-col sm:flex-row items-center sm:items-end sm:space-x-5 m-5 p-3"> <!-- here -->
          <div class="relative">
            <img
              src="/src/assets/Images/WhatsApp Image 2024-11-27 at 7.19.51 PM.png"
              alt="Profile"
              class="h-24 w-24 sm:h-32 sm:w-32 rounded-full border-4 border-white shadow-lg"
            />
            <button class="absolute bottom-0 right-0 bg-white rounded-full p-2 shadow-lg">
              <span class="text-gray-600">Edit</span>
            </button>
          </div>
            <div class="mt-4 sm:mt-0 text-center sm:text-left">
              <!-- edit here -->
                <h1 class="text-2xl font-bold text-gray-900">{{ userStore.user.name }}</h1>
                <p class="text-gray-500">@DSAI_202201124</p>
                <p class="mt-1 text-gray-600">Data Scientist | Football player</p>
         </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'

export default {
    name: 'FeedView',

    setup() {
        const userStore = useUserStore()
        const toastStore = useToastStore()

        return {
            userStore,
            toastStore
        }
    },

    data() {
        return {
            posts: [],
            user: {
                id: ''
            },
            can_send_friendship_request: null,
        }
    },

    mounted() {
        this.getFeed()
    },

    watch: { 
        '$route.params.id': {
            handler: function() {
                this.getFeed()
            },
            deep: true,
            immediate: true
        }
    },

    methods: {
        getFeed() {
            axios
                .get(`/api/posts/profile/${this.$route.params.id}/`)
                .then(response => {
                    console.log('data', response.data)

                    this.posts = response.data.posts
                    this.user = response.data.user
                    this.can_send_friendship_request = response.data.can_send_friendship_request
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
    }
}
</script>