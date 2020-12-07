<template>
  <div>
    <h4 class="font-weight-bold text-color text-left pl-4 mb-4 mt-2" style="margin-left: 10%">Drama</h4>
    <div id="carouselExampleControls1" class="carousel slide mt-3" data-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active d-flex row justify-content-start" style="margin-left: 150px;">
          <Drama_Review
            v-for="(dramaMovie,idx) in dramaMovies" :key="idx"
            :dramaMovie='dramaMovie'
            :idx="idx"
          />
        </div>
      </div>
      <a class="carousel-control-prev" href="#carouselExampleControls1" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a class="carousel-control-next" href="#carouselExampleControls1" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
    </div>

    <h4 class="font-weight-bold text-color text-left pl-4 mb-4 mt-5" style="margin-left: 10%;">Action</h4>
    <div id="carouselExampleControls3" class="carousel slide mt-3" data-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active d-flex row justify-content-start" style="margin-left: 150px;">
          <Action_Review
            v-for="(actionMovie,idx) in actionMovies" :key="idx"
            :actionMovie='actionMovie'
          />  
        </div>
      </div>
      <a class="carousel-control-prev" href="#carouselExampleControls3" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a class="carousel-control-next" href="#carouselExampleControls3" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
    </div>

    <h4 class="font-weight-bold text-color text-left pl-4 mb-4 mt-5" style="margin-left: 10%;">Comedy</h4>  
    <div id="carouselExampleControls4" class="carousel slide mt-3" data-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active d-flex row justify-content-start" style="margin-left: 150px;">
          <Comedy_Review
            v-for="(comedyMovie,idx) in comedyMovies" :key="idx"
            :comedyMovie='comedyMovie'
          />    
        </div>
      </div>
      <a class="carousel-control-prev" href="#carouselExampleControls4" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a class="carousel-control-next" href="#carouselExampleControls4" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Drama_Review from '@/views/review/Drama_Review'
import Action_Review from '@/views/review/Action_Review'
import Comedy_Review from '@/views/review/Comedy_Review'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ReviewList',
  components: {
    Drama_Review,
    Action_Review,
    Comedy_Review,
  },
  data: function () {
    return {
      reviews: [],
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
  },   
  computed: {
    dramaMovies: function () {
      let x = this.reviews.filter(function (n) {
        return n['genre'] == 18
      })
      const y = x.splice(x.length-5,5)
      return y  
    },
    actionMovies: function () {
      let x = this.reviews.filter(function (n) {
        return n['genre'] == 28
      })
      const y = x.splice(x.length-5,5)
      return y
    },
    comedyMovies: function () {
      let x = this.reviews.filter(function (n) {
        return n['genre'] == 35
      })
      const y = x.splice(x.length-5,5)
      return y
    }
  },
  created: function () {
    const config = this.setToken()
    axios.get(`${SERVER_URL}/community`,config)
      .then(res => {
        this.reviews = res.data
      })
      .catch(err => {
        console.log(err)
      })

  }
}
</script>

<style>
.text-color {
  color: rgb(214, 109, 109);
}
</style>