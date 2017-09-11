<template>
  <div class="hello">
    <h1>Your User Page</h1> <br> <br>
    <app-user-input v-model="email" field="Email"></app-user-input>
    <app-user-input v-model="address" field="Address"></app-user-input>
    <app-user-input v-model="saturdayAvailability" field="Saturday Availability (Hours)"></app-user-input>
    <app-user-input v-model="sundayAvailability" field="Sunday Availability (Hours)"></app-user-input>
  </div>
</template>

<script>
import UserInput from './UserInput.vue'

export default {
  name: 'user',
  data () {
    return {
      email: 'user@gmail.com',
      address: 'Harrisburg, PA',
      sundayAvailability: 2,
      saturdayAvailability: 2
    }
  },

  components: {
    appUserInput: UserInput
  }
}
</script>
