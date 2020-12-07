<template>
  <div @click="reviewDetail" class="card ml-4 my-2 cardbg font" style="height: 22rem; width: 15rem; border-radius:20px; overflow: hidden;">
    <img class="card-img-top cardimg" :src="dramaUrl" alt="Card image cap">
    <div class="card-body pt-1" style="height: 30px;'">
      <h5 class="card-title"><span class="title font-weight-bold">"{{ movie_title | truncate(10, '...') }}"</span></h5>
      <h6 class="card-title lg font-weight-bold">{{ review_title | truncate(11, '...') }}</h6>
      <b-form-rating readonly class="formbg" variant="warning" v-model="this.rank" no-border size="sm"></b-form-rating>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Drama_Review',
  props: {
    dramaMovie: Object,
  },
  computed: {
    dramaUrl: function() {
      return `https://image.tmdb.org/t/p/w200${this.dramaMovie['poster_path']}`
    },
    review_title: function() {
      return this.dramaMovie['review_title']
    },
    movie_title: function() {
      return this.dramaMovie['movie_title']
    },
    rank: function() {
      return this.dramaMovie['rank']
    },

  },
  methods: {
    reviewDetail: function () {
      this.$router.push({ name : 'ReviewDetail', params: {reviewId: this.dramaMovie.id} })
    }
  }
}
</script>

<style scoped>
.cardbg {
  background-color: rgba(112, 112, 112, 0.425);
}
.card:hover > img {
  opacity:0.5;
}
.formbg {
  background-color: transparent;
}
.title {
  color: whitesmoke;
}
.lg {
  color: lightgray
}
.cardimg {
  height: 15rem;
  padding: .5rem;
  border-radius: 10%;
}
.font {
  font-family: 'Do Hyeon', sans-serif;
}
</style>