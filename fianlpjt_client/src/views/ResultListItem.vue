<template>
  <div class="col mb-4">
    <img @click="movieDetail" class="mb-3 cardimg" :src="movieUrl" alt="movieTitle">
    <br>
    <a @click="movieDetail" class="cardTitle cardimg">{{ movie.title }}</a>
  </div>
</template>

<script>
export default {
  name: 'ResultListItem',
  props: {
    movie: Object,
  },
  methods: {
    movieDetail: function () {
      this.$router.push({ name: 'MovieDetail', params: { movieId: this.movie.id }})
    }
  },
  computed: {
    movieUrl: function() {
      return `https://image.tmdb.org/t/p/w200${this.movie.poster_path}`
   },
  },
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
</style>