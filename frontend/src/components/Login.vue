<template>
  <div>
    <template v-if="!isLoggedIn">
      <h1>Log In</h1>
      email: <input v-model="email" type="text"><br><br>
      password: <input type="password"><br><br>
      <button class="btn btn-primary" @click="login()">login</button>
      <br> <br>
    </template>
    <template v-else>
    <p>{{ loginType }}</p>
    </template>
  </div>
</template>

<script>
export default {
  name: 'login',
  data () {
    return {
      email: ''
    }
  },
  computed: {
    isLoggedIn () {
      return this.$store.getters.IsLoggedIn
    },
    loginType () {
      if (!this.$store.getters.IsLoggedIn) {
        return 'Not logged in'
      } else {
        if (this.$store.getters.IsAdmin) {
          return 'logged in as admin'
        } else {
          return 'logged in as user'
        }
      }
    }
  },
  methods: {
    login () {
      if (this.email === 'user@gmail.com') {
        this.$store.dispatch('logIn', false)
        this.$router.push('/')
      } else if (this.email === 'admin@gmail.com') {
        this.$store.dispatch('logIn', true)
        this.$router.push('/')
      } else {
        alert('invalid username and password')
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  font-weight: normal;
}
</style>
