<template>
  <div class="d-flex justify-content-between align-items-center my-4">
    <div class="d-flex flex-column align-items-start">
      <h5 class="pointer" @click="reviewDetail">{{ review.review_title }}</h5>
      <h6 class="pointer" @click="userProfile">{{ review.user }}</h6>
    </div>
    <b-form-rating readonly class="formbg" style="background-color: transparent; width: 10rem;" variant="warning" v-model="this.review.rank" no-border size="sm"></b-form-rating>
  </div>
</template>

<script>
export default {
  name: 'MoviesReviewsListItem',
  props: {
    review: Object
  },
  methods: {
    reviewDetail: function () {
      this.$router.push({ name : 'ReviewDetail', params : { reviewId: this.review.id}})
    },
    userProfile: function () {
      this.$router.push({ name: 'UserProfile', params: {username: this.review.user} })
    },
  }
}
</script>

<style scoped>
.pointer {
  cursor: pointer;
}
</style>