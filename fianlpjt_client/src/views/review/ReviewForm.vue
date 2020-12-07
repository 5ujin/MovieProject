<template>
  <div class="container">
    <div class="jumbotron bigjumbo">
      <h4 class="display-4">리뷰작성</h4> 
      <div class="d-flex flex-column justify-content-around">
        <input id="review_title" class="form-control input" placeholder="제목을 입력해주세요." type="text" v-model.trim="review_title">
        <textarea class="form-control input" placeholder="내용을 입력해주세요." style="height: 10rem;" type="text" v-model.trim="review_content"></textarea>
        <b-form-rating class="form-control input" variant="warning" v-model="rank"></b-form-rating>
      </div> 
      <button class="btn btn-danger mt-5 btn-lg" @click="createReview">작성하기</button>
    </div>
  </div>
</template>

<script>
import axios from'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ReviewForm',
  data: function () {
    return {
      movie: '',
      review_title: '',
      review_content: '',
      rank: '',
    }
  },
  props: ['movieId'],
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
    createReview: function () {
      const config = this.setToken()

      const review = {
        movie: this.movieId,
        review_title: this.review_title,
        review_content: this.review_content,
        rank: this.rank
      }
      console.log(this.movieId)
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
  }
</script>

<style scoped>
  .bigjumbo {
    background-color: rgba(78, 78, 78, 0.438);
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
</style>