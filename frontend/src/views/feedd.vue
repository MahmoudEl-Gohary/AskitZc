<script>
import axios from 'axios'
import signedHeader from '../components/signedHeader.vue'
// import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
// import Trends from '../components/Trends.vue'
// import FeedItem from '../components/FeedItem.vue'
// import FeedForm from '../components/FeedForm.vue'

export default {
    name: 'FeedView',

    components: {
        signedHeader,
    //     PeopleYouMayKnow,
    //     Trends,
    //     FeedItem,
    //     FeedForm
    },

    data() {
        return {
            posts: [],
            body: '',
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

        deletePost(id) {
            this.posts = this.posts.filter(post => post.id !== id)
        },
    }
}
</script>

<template>
    <signedHeader />
  <div class="min-h-screen bg-gradient-to-b from-gray-100 to-gray-300 py-10">
    <div class="container mx-auto px-6">
      <h1 class="text-4xl font-extrabold text-center text-gray-900 mb-12">Community Feed</h1>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <!-- Feed Items -->
        <div
          v-for="item in posts"
          v-bind:key="item.id"
          class="bg-white rounded-xl shadow-lg overflow-hidden hover:shadow-xl transition-shadow duration-300 group"
        >
          <!-- Header -->
          <div
            class="p-4 bg-gradient-to-r from-blue-500 from-[#00b4d1] to-[#00a1b5] text-white text-sm flex justify-between items-center"
          >
            <span>{{ item.created_by.name }}</span>
            <span
              class="px-3 py-1 rounded-full bg-white text-xs font-semibold text-gray-800"
              :class='text-blue-600'
            >
              {{ item.created_at_formated}} ago
            </span>
          </div>

          <!-- Content -->
          <div class="p-6">
            <h2 class="text-lg font-bold text-gray-900 mb-3 group-hover:text-blue-500 transition-colors">
              {{ item.title }}
            </h2>
            <p class="text-gray-600 line-clamp-3">
              {{ item.body }}
            </p>
          </div>

          <!-- Footer -->
          <div class="p-4 bg-gray-50 border-t text-sm text-gray-500 flex justify-between items-center">
            <div>
              <!-- <span class="font-semibold">{{ item.votes }} votes</span>
              <span > • {{ item.answers }} answers</span> -->
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
