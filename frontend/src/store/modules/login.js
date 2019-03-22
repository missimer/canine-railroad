export default {
  state: {
    loggedIn: false,
    admin: false
  },
  mutations: {
    mutateLogIn (state, payload) {
      state.loggedIn = true
      state.admin = payload
    },
    mutateLogOut (state) {
      state.loggedIn = false
    }
  },
  actions: {
    logIn ({ commit }, payload) {
      commit('mutateLogIn', payload)
    },
    logOut ({ commit }) {
      commit('mutateLogOut')
    }
  },
  getters: {
    IsLoggedIn (state) {
      return state.loggedIn
    },
    IsAdmin (state) {
      return state.admin
    }
  }
}
