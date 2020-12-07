<template>
  <div>
    <MoviesReviewsListItem 
      v-for="(review, idx) in moviesReviews"
      :key="idx"
      :review="review"
    />
  </div>
</template>

<script>
import axios from 'axios'
import MoviesReviewsListItem from './MoviesReveiwsListItem'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MoviesReviewsList',
  props: {
    reviews: Array,
    movieId: String,
  },
  components: {
    MoviesReviewsListItem
  },
  data: function () {
    return {
      moviesReviews: [],
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')

      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    getReviews: function () {
      const config = this.setToken()
      axios.get(`${SERVER_URL}/community/`, config)
      .then(res => {
        for (var i=0;i<res.data.length;i++) {
          if (res.data[i]['movie']===Number(this.movieId)) {
            this.moviesReviews.push(res.data[i])
          }
        }
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  created: function () {
    this.getReviews()
  }
}
</script>

<style>

</style>