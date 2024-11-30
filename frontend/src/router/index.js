import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AskQuestion from '../views/AskQuestion.vue'
import LoginPage from '../views/LoginPage.vue'
import signup from '../views/signup.vue'

import ProfileView from '../views/ProfileView.vue'
import Signup from '../views/signup.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/ask',
      name: 'ask',
      component: AskQuestion,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginPage
    },
    {
      path: '/signup',
      name: 'signup',
      component: signup
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView
    }
  ],
})

export default router
