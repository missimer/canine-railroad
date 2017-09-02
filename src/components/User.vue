<template>
  <div class="hello">
    <h1>Your User Page</h1> <br> <br>
    Email: <input v-model="email"> <br> <br>
    Address: <input v-model="address"> <br> <br>
    Saturday Availability: <input maxlength="4" size="4" v-model="saturdayAvailability"> Hours <br> <br>
    Sunday Availability: <input maxlength="4" size="4" v-model="sundayAvailability"> Hours
  </div>
</template>

<script>
export default {
  name: 'user',
  data () {
    return {
      email: 'user@gmail.com',
      address: 'Harrisburg, PA',
      sundayAvailability: 2,
      saturdayAvailability: 2
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;

li {
  display: inline-block;
  margin: 0 10px;
}

}
a {
  color: #42b983;
}
</style>
