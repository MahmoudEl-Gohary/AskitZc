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

<template>
  <div class="bg-white rounded-xl shadow-lg p-6">
    <div class="flex flex-col items-center">
      <div class="w-24 h-24 rounded-full overflow-hidden mb-4">
        <img src="https://cdn4.iconfinder.com/data/icons/forum-buttons-and-community-signs-1/794/profile-3-512.png" alt="Profile" class="w-full h-full object-cover">
      </div>
      <h2 class="text-xl font-bold mb-4">{{ userStore.user.name }}</h2>
      <div class="flex space-x-8 text-gray-600">
        <div class="text-center">
          <div class="font-bold">120</div>
          <div class="text-sm">friends</div>
        </div>
        <div class="text-center">
          <div class="font-bold">12</div>
          <div class="text-sm">posts</div>
        </div>
      </div>
    </div>
  </div>
</template>