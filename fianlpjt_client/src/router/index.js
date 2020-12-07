import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Review from '@/views/review/Reviews.vue'
import Login from '@/views/accounts/Login.vue'
import MyProfile from '@/views/profile/MyProfile.vue'
import UserProfile from '@/views/profile/UserProfile.vue'
import MovieDetail from '@/views/profile/MovieDetail.vue'
import ReviewForm from '@/views/review/ReviewForm.vue'
import ReviewDetail from '@/views/review/ReviewDetail.vue'
import SearchResult from '@/views/SearchResult.vue'

const originalPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
    return originalPush.call(this, location).catch(() => {
        return window.location.reload()
    })
};

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/review/reviews',
    name: 'Review',
    component: Review
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/profile/mypage',
    name: 'MyProfile',
    component: MyProfile
  },
  {
    path: '/profile/:username',
    name: 'UserProfile',
    component: UserProfile,
    props: true
  },
  {
    path: '/moviedetail/:movieId',
    name: 'MovieDetail',
    component: MovieDetail,
    props: true,
  },
  {  
    path: '/review/reviewForm',
    name: 'ReviewForm',
    component: ReviewForm,
    props: true,
  },
  {  
    path: '/review/:reviewId',
    name: 'ReviewDetail',
    component: ReviewDetail,
    props: true,
  },
  {  
    path: '/serchresult/:q',
    name: 'SearchResult',
    component: SearchResult,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
