<template>
  <div class="col mb-4">
    <img @click="movieDetail" class="mb-3 cardimg" :src="movieUrl" alt="movieTitle">
    <br>
    <a @click="movieDetail" class="cardTitle cardimg">{{ movieTitle }}</a>
  </div>
</template>

<script>

export default {
  name: 'FavoriteListItem',
  props: {
    movieIdx: Number,
  },
  
  data: function () {
    return {
      movieTitle: '',
      posterSrc: '',
      movieid: '',
    }
  },
  methods: {
    getFavorites: function () {
      this.movieTitle = this.$store.state.movies[0][this.movieIdx-1]['title']
      this.posterSrc = this.$store.state.movies[0][this.movieIdx-1]['poster_path']
      this.movieid = this.movieIdx
    },
    movieDetail: function () {
      this.$router.push({ name: 'MovieDetail', params: { movieId: this.movieid }})
    }
  },
  computed: {
    movieUrl: function() {
      return `https://image.tmdb.org/t/p/w200${this.posterSrc}`
    },
  },
  created: function () {
    this.getFavorites()
  }
  
}
</script>

<style scoped>
.cardTitle {
  text-align: center;
  color: lightgrey;
  margin-top: 2rem;
}
.cardimg {
  cursor: pointer;
  border-radius: 8%;
}
.formodal {
  background-color: rgba(54, 58, 58, 0.747);
}
</style>