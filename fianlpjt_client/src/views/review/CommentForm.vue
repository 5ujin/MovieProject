<template>
  <div class="d-flex align-items-center justify-content-center mt-5 font">
    <input @keypress.enter="createComment" class="form-control input" type="text" v-model="content" placeholder="댓글을 작성해주세요.">
    <button @click="createComment" class="btn btn-primary ml-3">댓글등록</button>
  </div>
</template>

<script>
import axios from 'axios'
import moment from 'moment'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CommentForm',
  data: function () {
    return {
      content: '',
    }
  },
  props: {
    reviewId: Number,
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
    createComment: function () {
      const config = this.setToken()
      const comment = {
        content: this.content,
        review: Number(this.reviewId),
      }
      axios.post(`${SERVER_URL}/community/${Number(this.reviewId)}/comments/`, comment, config)
      .then(() => {
        const username = localStorage.getItem('username')
        const now = moment().format('YYYY-MM-DD HH:mm:ss')
        const comment2 = {
          content: this.content,
          review: Number(this.reviewId),
          user: username,
          created_at: now
        }
        this.$emit('createComment', comment2)
        this.content =''
        
      })
      .catch(err => {
        console.log(err)
      })
    }
  }
}
</script>

<style scoped>
.input {
  width: 60%;
  background-color: rgba(209, 208, 208, 0.521);
}
input::placeholder {
  color: lightgray
}
.font {
  font-family: 'Do Hyeon', sans-serif;
}
</style>