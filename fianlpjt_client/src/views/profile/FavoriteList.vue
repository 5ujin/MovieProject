<template>
  <div class="row row-cols-2 row-cols-md-3 row-cols-lg-5">
    <p v-for="(movieIdx, idx) in movies" :key="idx">
      <FavoriteListItem 
        :movieIdx="movieIdx"
      />
    </p>
  </div>
</template>

<script>
import FavoriteListItem from '@/views/profile/FavoriteListItem'

export default {
  name: 'FavoriteList',
  props: {
    movies: Array
  },
  components: {
    FavoriteListItem
  },
}
</script>

<style>

</style>