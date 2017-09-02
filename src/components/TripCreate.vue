<template>
  <div>
  <h1>Create a new Trip</h1>
  <div id="map"></div>
  <br> <br>
  Start: <input @blur="updateMap" v-model="start"> <br> <br>
  Destination: <input @blur="updateMap" v-model="destination"> <br> <br>
  <hr>
  <p>Switch Locations:</p>
  <div
    v-for="(wp,index) in waypoints"
    :key="index"
    style="cursor: pointer">
    <input @blur="updateMap" v-model="wp.value">
    <br> <br>
  </div>
  <button @click="addWaypointField">
    Add New Switch Location
  </button>
  <br> <br>
  <button>
    Save Trip
  </button>
  </div>
</template>

<script>
/* global google */
export default {
  name: 'tripCreate',

  data () {
    return {
      directionService: null,
      directionsDisplay: null,
      start: '',
      destination: '',
      waypoints: []
    }
  },

  methods: {
    updateLocations () {
      var legs = this.directionsDisplay.getDirections().routes[0].legs
      console.log(legs)
      console.log('before')
      console.log(this.waypoints)
      this.start = legs[0].start_address
      this.destination = legs[legs.length - 1].end_address

      for (var i = 0; i < legs.length - 1; i++) {
        console.log(legs[i].end_address)
        this.waypoints[i].value = legs[i].end_address
      }
      console.log('after')
      console.log(this.waypoints)
    },
    addWaypointField () {
      this.waypoints.push({value: ''})
    },
    updateMap () {
      var waypts = []
      for (var wp of this.waypoints) {
        if (wp !== '') {
          waypts.push({location: wp.value, stopover: true})
        }
      }
      this.directionsService.route({
        origin: this.start,
        destination: this.destination,
        waypoints: waypts,
        travelMode: 'DRIVING'
      }, (response, status) => {
        if (status === 'OK') {
          this.directionsDisplay.setDirections(response)
        }
      })
    },
    initMap () {
      this.directionsService = new google.maps.DirectionsService()
      this.directionsDisplay = new google.maps.DirectionsRenderer({
        draggable: true
      })
      var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 6,
        center: {lat: 41.85, lng: -87.65}
      })
      this.directionsDisplay.setMap(map)
      this.directionsDisplay.addListener('directions_changed', () => {
        this.updateLocations()
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
</style>
