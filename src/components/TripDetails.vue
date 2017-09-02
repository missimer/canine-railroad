<template>
  <div>
    <h1>Trip Details for Dash</h1>
    <div id="map"></div>
    <br> <br>
    <ul class="list-group">
    <router-link
      v-for="index in (locations.length - 1)"
      tag="li"
      :to="/trips/ + tripId + /leg/ + (index - 1)"
      :key="index"
      class="list-group-item"
      style="cursor: pointer">
      {{ locations[index - 1] }} to {{ locations[index] }}
    </router-link>
    </ul>
  </div>
</template>

<script>
/* global google */
export default {
  name: 'tripDetails',

  data () {
    return {
      directionService: null,
      directionsDisplay: null,
      locations: [
        'Harrisburg, PA',
        'Allentown, PA',
        'Oakland, NY',
        'Danbury, CT',
        'Springfield, MA',
        'Boston, MA'
      ]
    }
  },

  props: ['tripId'],

  methods: {
    initMap () {
      this.directionsService = new google.maps.DirectionsService()
      this.directionsDisplay = new google.maps.DirectionsRenderer()
      var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 6,
        center: {lat: 41.85, lng: -87.65}
      })
      this.directionsDisplay.setMap(map)
      this.calculateAndDisplayRoute()
    },

    calculateAndDisplayRoute () {
      var waypts = []
      for (var i = 1; i < this.locations.length - 1; i++) {
        waypts.push({location: this.locations[i], stopover: true})
      }
      this.directionsService.route({
        origin: this.locations[0],
        destination: this.locations[this.locations.length - 1],
        waypoints: waypts,
        optimizeWaypoints: true,
        travelMode: 'DRIVING'
      }, (response, status) => {
        if (status === 'OK') {
          this.directionsDisplay.setDirections(response)
        } else {
          window.alert('Directions request failed due to ' + status)
        }
      })
    }
  },

  mounted () {
    this.initMap()
  }
}
</script>

<style scoped>
/* Always set the map height explicitly to define the size of the div
 * element that contains the map. */
#map {
  height: 300px;
  width: 100%;
  margin: auto;
  background-color: lightgray;
}
li:hover {
  background-color: #337ab7;
  color: lavender;
}
</style>
