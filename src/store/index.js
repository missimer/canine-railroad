import Vue from 'vue'
import Vuex from 'vuex'
import CreatePersistedState from 'vuex-persistedstate'

import Login from './modules/login'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    Login
  },
  plugins: [CreatePersistedState()]
})
