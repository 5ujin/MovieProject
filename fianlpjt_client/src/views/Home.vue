<template>
<div class="font">
  <!-- <h2>{{ poster_paths }}</h2>
  <h2>{{ poster_paths2 }}</h2>
  <h2>{{ poster_paths3 }}</h2> -->
  <h2 class="text-left font" style="color: lightgray; margin-left: 9%;">What's HOT?</h2>
  <div id="carouselExampleControls" class="carousel slide mt-3" data-ride="carousel">
    <div class="carousel-inner">
      <div class="carousel-item active row justify-content-center">
        <img class="i-block marl" :class="{ mar : idx !==4}" v-for="(movie,idx) in movies" :key="idx" 
        style="cursor:pointer; height: auto; width: 14%; border-radius: 10px;" @click="movieDetail(movie['id'])"
        :src="`https://image.tmdb.org/t/p/w500${movie['poster_path']}`" :alt="movie">
      </div>
      <div class="carousel-item row justify-content-center">
        <img class="i-block marl" :class="{ mar : idx !==4}" v-for="(movie,idx) in movies_two" :key="idx" 
        style="cursor:pointer; height: auto; width: 14%; border-radius: 10px;" @click="movieDetail(movie['id'])"
        :src="`https://image.tmdb.org/t/p/w500${movie['poster_path']}`" alt="">
      </div>
      <div class="carousel-item row justify-content-center">
        <img class="i-block marl" :class="{ mar : idx !==4}" v-for="(movie,idx) in movies_three" :key="idx" 
        style="cursor:pointer; height: auto; width: 14%; border-radius: 10px;" @click="movieDetail(movie['id'])"
        :src="`https://image.tmdb.org/t/p/w500${movie['poster_path']}`" alt="">
      </div>
    </div>
    <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="sr-only">Previous</span>
    </a>
    <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="sr-only">Next</span>
    </a>
  </div>
  <h2 class="text-left font" style="color: lightgray; margin-left: 9%; margin-top: 50px; margin-bottom: 24px">{{ username }}님을 위한 추천영화</h2>
  <div v-if="recommended.length>0">
    <div id="carouselExampleControls1" class="carousel slide mt-3" data-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active row justify-content-start">
          <img class="i-block marlr" v-for="(poster,idx) in poster_paths" :key="idx" :src="poster" alt="" 
          style="cursor:pointer; height: auto; width: 10%; border-radius: 10px;" @click="movieDetail(recommended[idx])">
        </div>
        <div v-if="poster_paths2.length>0" class="carousel-item row justify-content-start">
          <img class="i-block marlr" v-for="(poster,idx) in poster_paths2" :key="idx" :src="poster" alt="" 
          style="cursor:pointer; height: auto; width: 10%; border-radius: 10px;" @click="movieDetail(recommended[idx+6])">
        </div>
        <div v-if="poster_paths3.length>0" class="carousel-item row justify-content-start">
          <img class="i-block marl" v-for="(poster,idx) in poster_paths3" :key="idx" :src="poster" alt="" 
          style="cursor:pointer; height: auto; width: 10%; border-radius: 10px;" @click="movieDetail(recommended[idx+12])">
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
  </div>
  <div v-else class="mt-5">
    <h3 style="text-align:center; color:lightgray; margin-top: 7rem;" class="display-4">더 많은 사람을 팔로우 해보세요!</h3>
  </div>
</div>

</template>

<script>
import axios from 'axios'
// import Movie from './Movie'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Home',
  // components: {
  //   Movie,
  // },
  data: function () {
    return {
      movie_all: [],
      username: localStorage.getItem('username'),
      following: [],
      myfavorites: [],
      following_movies: [],
      poster_paths: [],
      recommended: [],
      poster_paths2: [],
      poster_paths3: [],
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
    movieDetail: function (movie) {
      this.$router.push({ name: 'MovieDetail', params: { movieId: movie }})
    },

  },
  created: function () {
    if (!this.$store.state.movies[0]) {
      axios.get(`${SERVER_URL}/movie/`)
        .then(res => {
          this.$store.dispatch('saveMovies', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    }

    axios.get(`${SERVER_URL}/movie/`)
      .then(res => {
        this.movie_all = res.data
        const config = this.setToken()
        const username = localStorage.getItem('username')
        axios.get(`${SERVER_URL}/accounts/${username}`,config)
          .then(res => {
            console.log(res)
            this.following = res.data.followings
            this.myfavorites = res.data.movie_like
            for (const mov of this.following) {
                let x = this.movie_all.filter(function (n) {
                  return n['movie_like_users'].includes(mov)
                  }) 
                for (const a of x) {
                  this.following_movies.push(a['id'])
                }
              }
            this.following_movies = Array.from(new Set(this.following_movies))
            this.recommended = this.following_movies.filter((word) => !this.myfavorites.includes(word))
            for (const movie of this.recommended) {
              this.poster_paths.push(`https://image.tmdb.org/t/p/w500${this.$store.state.movies[0][movie-1]['poster_path']}`)
            }
            if (this.poster_paths.length > 18) {
              this.poster_paths3 = this.poster_paths.splice(12,6)
            } else if (this.poster_paths.length > 12) {
                this.poster_paths3 = this.poster_paths.splice(12, this.poster_paths.length - 12)
            }
            if (this.poster_paths.length > 6) {
              this.poster_paths2 =  this.poster_paths.splice(6, this.poster_paths.length - 6)
            } 

          })
          .catch(err => {
            console.log(err)
          })
      })
      .catch(err => {
        console.log(err)
      })


    const token = localStorage.getItem('jwt')
    if (!token) {
      this.$router.push({ name : 'Login' })
    }
  },
  // mounted: function () {
    // const config = this.setToken()
    // console.log(this.recommended)
    // for (const movie of this.recommended) {
    //   axios.get(`${SERVER_URL}/movies/${movie}`, config)
    //     .then(res => {
    //       console.log(res)
    //       this.poster_paths.push(res.data['poster_path'])
    //     })
    //     .catch(err => {
    //       console.log(err)
    //     })
    //   }
  // },
  computed: {
    movies: function () {
      return this.$store.state.movies[0].slice(0,5)
    },
    movies_two: function () {
      return this.$store.state.movies[0].slice(6,11)
    },
    movies_three: function () {
      return this.$store.state.movies[0].slice(12,17)
    },
    // poster_paths2: function () {

    // }
    // recommended: function () {
    //   return this.following_movies.filter((word) => !this.myfavorites.includes(word))
    // },
  },
}
</script>

<style>
.carousel-item > img:hover {
  opacity: 0.5;
}
.mar {
  margin-right: 20px;
}
.marl {
  margin-left: 20px;
}
.marr {
  margin-right: 30px;
}
.marlr {
  margin-left: 30px;
}
.font {
  font-family: 'Do Hyeon', sans-serif;
}
</style>
