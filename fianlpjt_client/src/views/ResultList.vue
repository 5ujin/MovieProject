<template>
  <div class="row row-cols-2 row-cols-md-3 row-cols-lg-5">
    <ResultListItem
      v-for="(movie, idx) in movies"
      :key="idx"
      :movie="movie"
    />
  </div>
</template>

<script>
import ResultListItem from '@/views/ResultListItem'

export default {
  name: 'ResultList',
  components: {
    ResultListItem,
  },
  props: {
    movies: Array,
  },

}
</script>

<style>

</style>