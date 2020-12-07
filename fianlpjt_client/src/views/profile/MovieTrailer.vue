<template>
  <div v-if="video">
    <b-embed
      type="iframe"
      aspect="16by9"
      :src="videoUrl"
      allowfullscreen
    >
    </b-embed>
  </div>
</template>

<script>
export default {
  name: 'MovieTrailer',
  props: {
    video: {
      type: Object,
    },
  },
  computed: {
    videoUrl: function () {
      return `https://www.youtube.com/embed/${this.video.id.videoId}`
    },
  },
}
</script>

<style>

</style>