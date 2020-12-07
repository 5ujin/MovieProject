<template>
  <div id="mpage" class="container font" style="background-color: #1e1e1e;">
    <div class="jumbotron jumbo">
      <h4 class="display-4 font">{{ username }}님의 장르는</h4>
      <h4 class="display-4 font">"{{ mygenre }}"</h4>
      <div class="d-flex justify-content-around mt-4">
        <h4 class="font">팔로워 {{ follower }}</h4>
        <h4 class="font">팔로잉 {{ following }}</h4>
      </div>
    </div>
    <h3 class="d-flex jusify-content-left mb-3">{{ username }}님이 좋아하는 영화</h3>
    <FavoriteList 
      :movies="myfavorites"
    />
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'

import FavoriteList from '@/views/profile/FavoriteList'


const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MyProfile',
  components: {
    FavoriteList
  },
  data: function () {
    return {
      username: '',
      follower: '',
      following: '',
      myfavorites: [],
      mygenres: [],
      mygenre: '',
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
    getUserInfo: function () {
      const config = this.setToken()
      const username = localStorage.getItem('username')
      axios.get(`${SERVER_URL}/accounts/${username}`,config)
      .then(res => {
        this.username = username
        this.follower = res.data.followers.length
        this.following = res.data.followings.length
        this.myfavorites = res.data.movie_like
        for (var i=0;i<this.myfavorites.length;i++) {
          this.mygenres.push(this.$store.state.movies[0][this.myfavorites[i]-1]['genres'][0])
        }
        var array = this.mygenres
        var result = _.head(_(array).countBy().entries().maxBy(_.last))
        this.mygenre = this.$store.state.genre_info[result]
          
      })
      .catch(err => {
        console.log(err)
      })
      
    },
  },
  created: function () {
    this.getUserInfo()
  }
}
</script>

<style scoped>
div {
  color: lightgrey;
}
.jumbo {
  background-color: rgba(108, 74, 131, 0.349);
}
.font {
  font-family: 'Do Hyeon', sans-serif;
}
</style>