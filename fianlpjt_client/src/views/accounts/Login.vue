<template>
  
  <div class="container font" style="margin-top: 6rem;">

    <h4 class="display-1 a">Triflix</h4>

    <div class="d-flex justify-content-center" style="margin-top: 8rem;">
      <div class="d-flex flex-column align-items-center">
        <div>
          <input 
          type="text" id="username" 
          v-model="credentials.username"
          class="form-control input"
          placeholder="ID를 입력하세요."
          >
        </div>
        <div>
          <input 
            type="password" 
            id="password" 
            v-model="credentials.password"
            @keypress.enter="login"
            class="form-control input"
            placeholder="비밀번호를 입력하세요."
          >
        </div>
      </div>
      <button @click="login" class="loginButton btn">로그인</button>
    </div>
    
    <div>
      <span style="color: lightgrey">계정이 없으신가요? <a href="" data-toggle="modal" data-target="#signupModal">가입하기</a>

      <div class="modal fade formodal" id="signupModal" tabindex="-1">
        <div class="modal-dialog modal-dialog-centered">

          <div class="modal-content formodal d-flex flex-column align-items-center">

            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel">회원가입</h5>
            </div>

            <div class="modal-body">
              <div>
                <input type="text" class="form-control input" v-model="credentialsForSignup.username" placeholder="ID를 입력하세요.">
              </div>
              <div>
                <input type="password" class="form-control input" v-model="credentialsForSignup.password" placeholder="비밀번호를 입력하세요.">
              </div>
              <div>
                <input 
                  type="password"  
                  v-model="credentialsForSignup.passwordConfirm"
                  @keypress.enter="signUp"
                  class="form-control input"
                  placeholder="비밀번호를 한 번 더 입력하세요."
                >
              </div>
            </div>

            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">닫기</button>
              <button type="button" class="btn btn-primary" @click="signUp" data-dismiss="modal">회원가입</button>
            </div>
            
          </div>
        </div>
      </div>
      </span>
      
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
      },
      credentialsForSignup: {
        username: '',
        password: '',
        passwordConfirm: '',
      },
    }
  },
  methods: {
    login: function () {
      axios.post(`${SERVER_URL}/accounts/api-token-auth/`, this.credentials)
        .then((res) => {
          localStorage.setItem('jwt', res.data.token)
          console.log(res)
          const usern = JSON.parse(res.config.data).username
          localStorage.setItem('username', usern)
          this.$emit('login', usern)
          this.$router.push({ name: 'Home' })
        })
        .catch((err) => {
          console.log(err)
        })
    },
    signUp: function () {
      console.log(this.credentials)
      axios.post(`${SERVER_URL}/accounts/signup/`, this.credentialsForSignup)
        .then((res) => {
          console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>

<style scoped>
  .logo {
    width: 15rem;
    height: 15rem;
    margin-bottom: 3rem;
  }
  .input {
    margin-bottom: 2rem;
    width: 20rem;
    background-color: rgba(156, 160, 160, 0.658);
  }
  .loginButton {
    margin-bottom: 2rem;
    margin-left: .5rem;
    background-color: rgb(62, 224, 170);
  }
  .formodal {
    background-color: rgba(73, 75, 75, 0.329);
  }
  .a {
    margin-top: 10rem;
  }
  input::placeholder {
    color: lightgrey;
  }
  .font {
    font-family: 'Do Hyeon', sans-serif;
  }
</style>