<template>
  <div @click="reviewDetail" class="card ml-4 my-2 cardbg font" style="height: 22rem; width: 15rem; border-radius:20px; overflow: hidden;">
    <img class="card-img-top cardimg" :src="actionUrl" alt="Card image cap">
    <div class="card-body pt-1" style="height: 30px;'">
      <h5 class="card-title"><span class="title font-weight-bold">"{{ movie_title | truncate(10, '...')}}"</span></h5>
      <h6 class="card-title lg font-weight-bold">{{ review_title | truncate(11, '...') }}</h6>
      <b-form-rating readonly class="formbg" variant="warning" v-model="this.rank" no-border size="sm"></b-form-rating>
      <p class="card-text"></p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Action_Review',
  props: {
    actionMovie: Object,
  },
  computed: {
    actionUrl: function() {
      return `https://image.tmdb.org/t/p/w200${this.actionMovie['poster_path']}`
    },
    review_title: function() {
      return this.actionMovie['review_title']
    },
    movie_title: function() {
      return this.actionMovie['movie_title']
    },
    rank: function() {
      return this.actionMovie['rank']
    },
  },
  methods: {
    reviewDetail: function () {
      this.$router.push({ name : 'ReviewDetail', params: {reviewId: this.actionMovie.id}})
    }
  }
}
</script>

<style scoped>
  .cardbg {
    background-color: rgba(112, 112, 112, 0.425);
  }
  .font_size {
    font-size: 1.5rem;
  }
  .bg_color {
    background-color: rgba(209, 200, 200, 0.486);
  }
  .text_color {
    color: lightgray;
  }
  .card:hover > img {
    opacity:0.5;
  }
  .formbg {
    background-color: transparent;
  }
  .title {
    color: lightgray;
  }
  .lg {
    color: whitesmoke;
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