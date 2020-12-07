<template>
  <div class="container font">
    <div class="jumbotron bigjumbo">
      <div class="d-flex justify-content-around"> 
        <img :src="movieUrl" alt="" style="width: 22rem; height: 25rem;">
        <div class="d-flex flex-column justify-content-around align-items-center" style="width: 100%">
          <div>
            <h4 @click="movieDetail" class="font display-4 h4">"{{ movieTitle }}"</h4>
            <h5>작성자 <a style="color: lightgray" href="" @click="userProfile" >{{ user }}</a></h5>
          </div>
          <div class="jumbotron contentjumbo mb-0 d-flex flex-column justify-content-around">
            <h5>{{ reviewTitle }}</h5>
            <hr style="border: 1px solid lightgray">
            <p>{{ reviewContent }}</p>
          </div>
          작성시각 | {{ createdAt | moment('YYYY-MM-DD HH:mm:ss') }}<br>
          수정시각 | {{ updatedAt | moment('YYYY-MM-DD HH:mm:ss') }}
        </div>
      </div>
      
      
      <b-form-rating 
        readonly 
        variant="warning" 
        style="background-color: transparent" 
        v-model="this.rank" 
        no-border 
        size="lg"
        class="mt-5"
      >
      </b-form-rating>
      <div v-if="verify" class="my-3">
        <button class="btn btn-secondary mx-3" data-toggle="modal" data-target="#reviewUpdateForm">수정하기</button>
        <button @click="deleteReview" class="btn btn-danger mx-3">삭제하기</button>
      </div>
      <CommentForm :reviewId="this.reviewId" @createComment="createComment"/>
      <CommentList :comments="this.comments" @deleteComment="deleteComment" />
    </div>
    <div class="modal fade" id="reviewUpdateForm" tabindex="-1">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content formodal">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">리뷰 수정</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <div class="contianer">
              <input type="text" class="form-control input" v-model="reviewTitle">
              <textarea type="text" class="form-control input fortextarea" v-model="reviewContent"></textarea>
              <b-form-rating class="form-control input" variant="warning" v-model="rank"></b-form-rating>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">취소</button>
            <button type="button" class="btn btn-primary" @click="updateReview" data-dismiss="modal">수정하기</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import CommentForm from './CommentForm'
import CommentList from './CommentList'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ReviewDetail',
  components: {
    CommentForm,
    CommentList
  },
  props: ['reviewId'],
  data: function () {
    return {
      movieId: '',
      createdAt: '',
      genre: '',
      likeUsers: '',
      movieTitle: '',
      posterPath: '',
      rank: '',
      reviewContent: '',
      reviewTitle: '',
      updatedAt: '',
      user: '',
      comments: [],
      verify: false,
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
    getDetail: function () {
      const config = this.setToken()
      axios.get(`${SERVER_URL}/community/${this.reviewId}/`, config)
      .then(res => {
        this.movieId = res.data.movie
        this.createdAt = res.data.created_at
        this.genre = this.$store.state.genre_info[res.data.genre]
        this.likeUsers = res.data.like_users.length
        this.movieTitle = res.data.movie_title
        this.posterPath = res.data.poster_path
        this.rank = res.data.rank
        this.reviewContent = res.data.review_content
        this.reviewTitle = res.data.review_title
        this.updatedAt = res.data.updated_at
        this.user = res.data.user
        this.comments = res.data.comments
        const currentUser = localStorage.getItem('username')
        if (currentUser == this.user) {
          this.verify = true
        }
      })
      .catch(err => {
        console.log(err)
      })    
    },
    deleteReview: function () {
      const config = this.setToken()
      const reviewId = Number(this.reviewId)
      axios.delete(`${SERVER_URL}/community/${reviewId}/`, config)
      .then(() => {
      this.$router.push({ name: "Review"})
      })
      .catch(err => {
        console.log(err)
      })
    },
    updateReview: function () {
      const config = this.setToken()
      const review = {
        movie: this.movieId,
        review_title: this.reviewTitle,
        review_content: this.reviewContent,
        rank: this.rank
      }
      axios.put(`${SERVER_URL}/community/${this.reviewId}/`,review, config)
      .then(() => {
        console.log('수정')
      })
      .catch(err => {
        console.log(err)
      })
    },
    userProfile: function () {
      this.$router.push({ name: 'UserProfile', params: {username: this.user} })
    },
    deleteComment: function (comment) {
      const deleteId = this.comments.indexOf(comment)
      this.comments.splice(deleteId, 1)
    },
    createComment: function (comment2) {
      this.comments.push(comment2)
    },
    movieDetail: function () {
      this.$router.push({ name : 'MovieDetail', params: { movieId: this.movieId}})
    }
  },
  created: function () {
    this.getDetail()

  },
  computed: {
    movieUrl: function() {
      return `https://image.tmdb.org/t/p/w200${this.posterPath}`
    },
  },

}
</script>

<style scoped>
.bigjumbo {
  background-color: rgba(78, 78, 78, 0.438);
}
.smjumbo {
  background-color: rgba(136, 136, 136, 0.158);
  width: 18rem;
}
div {
  color: lightgray;
}
.contentjumbo {
  background-color: rgba(136, 136, 136, 0.158);
  width: 80%;
  height: 16rem;
}
.formodal {
  background-color: rgba(56, 56, 56, 0.61);
}
.input {
  background-color: rgba(214, 211, 211, 0.692);
  margin-top: 2rem;
  margin-bottom: 2rem;
}
.fortextarea {
  height: 15rem;
}
.font {
  font-family: 'Do Hyeon', sans-serif;
}
.h4 {
  cursor: pointer;
}
</style>