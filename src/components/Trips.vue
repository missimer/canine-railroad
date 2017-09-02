<template>
  <div>
    <h1>Active and Upcoming Trip</h1>
    <br>
    <ul class="list-group">
    <router-link
      v-for="(trip, index) in trips"
      tag="li"
      :to="/trips/ + index"
      :key="index"
      class="list-group-item"
      style="cursor: pointer">
      {{ trip.name }} - From {{ trip.start }}, To {{ trip.destination }}
    </router-link>
    <router-link
      tag="li"
      to="/tripCreate"
      class="list-group-item"
      style="cursor: pointer">
      Create New Trip
    </router-link>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'trips',
  data () {
    return {
      trips: [
        {
          name: 'Dash',
          start: 'Harrisburg, PA',
          destination: 'Boston, MA'
        },
        {
          name: 'Bitsy',
          start: 'Miami, FL',
          destination: 'New York, NY'
        }
      ]
    }
  }
}
</script>

<style scoped>
  li:hover {
    background-color: #337ab7;
    color: lavender;
  }
</style>
