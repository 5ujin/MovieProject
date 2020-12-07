<template>
  <div>
    <div v-if="this.movies.length>0" class="container font">
      <h3 class="ab display-5">"{{ this.$route.params.q }}"로 검색한 결과입니다.</h3>
      <ResultList :movies="movies"/>
    </div>
    <div v-else>
      <h3 class="ab display-5">검색 결과가 없습니다</h3>
    </div>
  </div>
  
</template>

<script>
import ResultList from './ResultList'

export default {
  name: 'SearchResult',
  props: ['q',],
  components: {
    ResultList
  },
  data: function () {
    return {
      movies: []
    }
  },
  methods: {
    movieDetail: function () {
      this.$router.push({ name: 'MovieDetail', params: { movieId: this.movieId }})
    },
    getResult: function () {
      for (var i=0;i<300;i++) {
        if (this.$store.state.movies[0][i]['title'].includes(this.$route.params.q)) {
          this.movies.push(this.$store.state.movies[0][i])
        }
      }
    },
  },
  created: function () {
    this.getResult()
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
.ab {
  color: lightgray;
  margin-bottom: 5rem;
}
.font {
  font-family: 'Do Hyeon', sans-serif;
}
</style>