import {
  createRouter, createWebHashHistory 
} from 'vue-router'
import Home from '@/views/HomeView.vue'

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/:pathMatch(.*)*', redirect: { name: 'home' } 
    }
  ],
  scrollBehavior () {
    // always scroll to top
    return { top: 0 }
  }
})

export default router