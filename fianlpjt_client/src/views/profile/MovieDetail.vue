<template>
  <div class="container jumbotron bigjumbo font">
    <div class="d-flex justify-content-around mb-5">
      <div class="d-flex flex-column align-items-start">
        <p>이 영화를 {{movieLikeUsers }}명이 좋아합니다.</p>
        <img :src="movieUrl" alt="" style="width: 18rem; height: 25rem;">
      </div>
      
      <div class="d-flex flex-column justify-content-center align-items-center">
        <h4 class="display-4 mb-3 font">"{{ movieTitle }}"</h4>
        <h5>{{ genre }}</h5>
        <br>
        <h5>{{ releaseDate }} 개봉</h5>
        <br>
        <button data-toggle="modal" data-target="#reviewForm" class="btn btn-danger mt-5 bt">리뷰 쓰기</button>
        <button @click="likeMovie" class="btn btn-secondary mt-2 bt">내 영화리스트에 추가하기</button>
      </div>
    </div>
    <div class="smjumbo jumbotron">
      {{ overview }}
    </div>
    <MovieTrailer :video="video" />
    <div v-if="reviews.length>0">
      <h3 class="mt-5">리뷰목록</h3>
      <MoviesReviewsList :reviews="reviews" :movieId="this.movieId"/>
    </div>
    <div v-else>
      <h3 class="mt-5">아직 리뷰가 없어요</h3>
    </div>
    <div class="modal fade" id="reviewForm" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content formodal">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">리뷰 작성</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <div class="d-flex flex-column justify-content-around">
              <input id="review_title" v-model.trim="reviewTitle" class="form-control input" placeholder="제목을 입력해주세요." type="text">
              <textarea class="form-control input" v-model.trim="reviewContent" placeholder="내용을 입력해주세요." style="height: 10rem;" type="text"></textarea>
              <b-form-rating class="form-control input" variant="warning" v-model="rank"></b-form-rating>
            </div> 
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">닫기</button>
            <button @click="createReview" type="button" class="btn btn-primary" data-dismiss="modal">작성하기</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieTrailer from './MovieTrailer'
import MoviesReviewsList from './MoviesReviewsList'


const SERVER_URL = process.env.VUE_APP_SERVER_URL
const YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search'
const YOUTUBE_API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY

export default {
  name: 'movieDetail',
  props: ['movieId'],
  components: {
    MovieTrailer,
    MoviesReviewsList,
  },
  data: function () {
    return {
      movieTitle: '',
      posterPath: '',
      overview: '영화 개요 정보 없음',
      genre: '',
      releaseDate: '',
      movieLikeUsers: '',
      reviews: [],
      reviewTitle: '',
      reviewContent: '',
      rank: '',
      video: {},

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
    getMovieInfo: function () {
      this.movieTitle = this.$store.state.movies[0][this.movieId-1]['title']
      this.posterPath = this.$store.state.movies[0][this.movieId-1]['poster_path']
      if (this.$store.state.movies[0][this.movieId-1]['overview']!=0) {
        this.overview = this.$store.state.movies[0][this.movieId-1]['overview']
      }
      const genreId = this.$store.state.movies[0][this.movieId-1]['genres'][0]
      this.genre = this.$store.state.genre_info[genreId]
      this.releaseDate = this.$store.state.movies[0][this.movieId-1]['release_date']
      this.movieLikeUsers = this.$store.state.movies[0][this.movieId-1]['movie_like_users'].length
      this.reviews = this.$store.state.movies[0][this.movieId-1]['movies_reviews']
      axios.get(YOUTUBE_API_URL, {
        params: {
          key: YOUTUBE_API_KEY,
          part: 'snippet',
          type: 'video',
          q: `${this.movieTitle} trailer`,
        }
        })
      .then(res => {
        this.video = res.data.items[0]
      })
      .catch(err => console.log(err))      
    }, 
    likeMovie: function () {
      const config = this.setToken()
      axios.post(`${SERVER_URL}/movie/${this.movieId}/`, {}, config)
      .then(() => {
        this.$router.push({ name : 'MyProfile' })
      })
      .catch(err => {
        console.log(err)
      })
    },
    createReview: function () {
      const config = this.setToken()

      const review = {
        movie: this.movieId,
        review_title: this.reviewTitle,
        review_content: this.reviewContent,
        rank: this.rank
      }
      axios.post(`${SERVER_URL}/community/`, review, config)
      .then((res) => {
        console.log(res)
        this.$router.push({ name: 'Review' })
      })
      .catch((err) => {
        console.log(err)
      })
      }
  },
  computed: {
    movieUrl: function() {
      return `https://image.tmdb.org/t/p/w200${this.posterPath}`
    },
  },
  created: function () {
    this.getMovieInfo()
  },
  
}
</script>

<style scoped>
.bigjumbo {
  background-color: rgba(78, 78, 78, 0.438);
}
.smjumbo {
  background-color: rgba(136, 136, 136, 0.158);
  width: 100%;

}
div {
  color: lightgray;
}
.bt {
  width: 18rem;
}
.input {
  background-color: rgba(112, 112, 112, 0.534);
  color: lightgray;
  margin-bottom: 1rem;
  margin-top: 1rem;
}
input::placeholder {
  color: lightgray
}
textarea::placeholder {
  color: lightgray
}
.formodal {
  background-color: rgba(56, 56, 56, 0.61);
}
.font {
  font-family: 'Do Hyeon', sans-serif;
}
</style>