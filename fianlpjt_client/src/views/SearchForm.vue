<template>
  <div class="d-flex align-items-center">
    <b-form-input @keypress.enter="onEnter" size="sm" id="serchbar" class="font mr-sm-2 searchbar" v-model.trim="search" placeholder="영화를 검색하세요."></b-form-input>
    <button @click="onEnter" class="searchb font" id="sB" type="submit">Search</button>
  </div>
</template>

<script>
export default {
  name: 'SearchForm',
  data: function () {
    return {
      search: ''
    }
  },
  methods: {
    onEnter: function () {
      if (this.search) {
        this.$emit('search-input', this.search)
        this.search = '' 
      }
    } 
  }
}
</script>

<style scoped>
.searchbar {
  background-color: rgba(160, 158, 158, 0.315);
}
.searchb {
  background-color: rgb(62, 224, 170);
  font-size: 18px;
  text-align: center;
  border-radius: 5px;
}
#serchbar::placeholder {
  color: lightgray
}
.font {
  font-family: 'Do Hyeon', sans-serif;
}
</style>