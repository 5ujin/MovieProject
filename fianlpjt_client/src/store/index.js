import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: [],
    genre_info: {
      1: '액션',
      2: '어드벤처',
      3: '애니메이션',
      4: '코미디',
      5: '범죄',
      6: '다큐멘터리',
      7: '드라마',
      8: '가족',
      9: '판타지', 
      10: '역사',
      11: '호러',
      12: '음악',
      13: '미스테리',
      14: '로맨스',
      15: 'SF',
      16: 'TV영화',
      17: '스릴러',
      18: '전쟁',
      19: '서부',  
    }
  },
  mutations: {
    SAVE_MOVIES: function (state, movies) {
      state.movies.push(movies)
    },
  },
  actions: {
    saveMovies: function ({ commit }, movies) {
      commit('SAVE_MOVIES', movies)
  },
  },
  plugins: [
    createPersistedState(),
  ]
})
