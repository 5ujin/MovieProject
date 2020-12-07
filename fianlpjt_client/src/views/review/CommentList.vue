<template>
  <div class="mt-5">
    <CommentListItem
      v-for="(comment, idx) in comments"
      :key="idx"
      :comment="comment"
      @deleteComment="deleteComment"
    />
  </div>
</template>

<script>
import CommentListItem from './CommentListItem'

export default {
  name: 'CommentList',
  props: {
    comments: Array,
  },
  components: {
    CommentListItem,
  },
  methods: {
    deleteComment: function (comment) {
      this.$emit('deleteComment', comment)
    }
  }
}
</script>

<style>

</style>