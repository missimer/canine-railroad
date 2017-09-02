export default {
  state: {
    loggedIn: false,
    admin: false
  },
  mutations: {
    mutateLogIn (state, payload) {
      state.loggedIn = true
      state.admin = payload
    }
  },
  actions: {
    logIn ({ commit }, payload) {
      commit('mutateLogIn', payload)
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
