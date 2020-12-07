<template>
  <div class="commentjumbo d-flex justify-content-between align-items-center">
    <div class="d-flex flex-column align-items-start">
      <h5><a class="link" @click="userProfile" href="">{{ comment.user }}</a></h5>
      <p>{{ comment.content }}</p>
      <p>{{ comment.created_at | moment('YYYY-MM-DD HH:mm:ss') }}</p> 
    </div>
    <div>
      <button @click="deleteComment" class="btn btn-danger">삭제</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CommentListItem',
  props: {
    comment: Object
  },
  data: function () {
    return {
      username: '',
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
    userProfile: function () {
      this.username = this.comment.user
      this.$router.push({ name : 'UserProfile', params : {username: this.username}})
    },
    deleteComment: function () {
      const config = this.setToken()
      axios.delete(`${SERVER_URL}/community/comments/${this.comment.id}/`,  config)
      .then(() => {
        this.$emit('deleteComment', this.comment)
      })
      .catch(err => {
        console.log(err)
      })
    }
  }
}
</script>

<style scoped>
.commentjumbo {
  margin-top: 1rem;
  margin-bottom: 1rem;
}
.link {
  color:rgb(62, 224, 170);
}
</style>