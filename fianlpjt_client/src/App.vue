<template>
  <div id="app" class="font">
    <b-navbar v-if="login" class="navbar mb-5" toggleable="lg" type="dark">
      <b-navbar-brand href="#">
        <img @click="goToHome" class="logo" src="@/assets/logo.png" alt="">
        <router-link :to="{ name: 'Home' }"></router-link>
      </b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav class="mt-4">
        <b-navbar-nav >
          <b-nav-item href="#">
            <router-link :to="{ name: 'Home' }" class="navbartext"><h4>Home</h4></router-link>
          </b-nav-item>
          <b-nav-item href="#">
            <router-link :to="{ name: 'Review' }" class="navbartext"><h4>Review</h4></router-link>
          </b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <div class="mb-4 mr-2 d-flex justify-content-center">
            <SearchForm @search-input="onSearchInput"/>
          </div>

          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template #button-content>
              <em><h4>{{ username }}</h4></em>
            </template>
            <b-dropdown-item href="#" class="navbar">
              <router-link :to="{ name: 'MyProfile' }" class="navbartext">My Page</router-link>
              </b-dropdown-item>
            <b-dropdown-item href="#" class="navbar">
              <router-link @click.native='logout' to="#" class="navbartext">Sign Out</router-link>
              </b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <router-view @login="loginF"/>
  </div>
</template>

<script>
import SearchForm from '@/views/SearchForm'

export default {
  name: 'App',
  data: function () {
    return {
      login: false,
      username: '',
      search: ''
    }
  },
  components: {
    SearchForm
  },
  methods: {
    logout: function () {
      localStorage.removeItem('jwt')
      localStorage.removeItem('username')
      this.login = false
      this.$router.push({ name: 'Login' })
    },
    loginF: function (usern) {
      this.login = true
      this.username = usern
    },
    goToHome: function () {
      this.$router.push({ name : 'Home' })
    },
    onSearchInput: function (search) {
      this.$router.push({ name : 'SearchResult', params: { q: search }})
    }
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.login = true
    }
  },
  mounted: function () {
    this.username = localStorage.getItem('username')
  }
}
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.navbartext {
  color: rgb(165, 165, 167);
}
.navbar {
  background-color:rgba(47, 49, 49, 0);
}
.logo {
  height: 5rem;
  width: 5rem;
}
.searchbar {
  background-color: rgba(160, 158, 158, 0.315);
}
.searchb {
  background-color: rgb(62, 224, 170);
  font-size: 18px;
  text-align: center;
  border-radius: 5px;
}
#serchbar::placeholder {
  color: lightgray
}
.font {
  font-family: 'Do Hyeon', sans-serif;
}
</style>
