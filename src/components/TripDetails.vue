<template>
  <div>
    <h1>Trip Details for Dash</h1>
    <div id="map"></div>
    <br> <br>
    <app-leg-table :legs="legs" :linkPrefix="'/trips/' + tripId + '/leg/'"></app-leg-table>
  </div>
</template>

<script>
/* global google */

import LegTable from './LegTable.vue'

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
      ],
      legs: []
    }
  },

  props: ['tripId'],

  methods: {
    initMap () {
      this.directionsService = new google.maps.DirectionsService()
      this.directionsDisplay = new google.maps.DirectionsRenderer()
      var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 4,
        center: {lat: 39.8283, lng: -98.5795}
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
          this.legs = []

          for (var index in this.directionsDisplay.getDirections().routes[0].legs) {
            var leg = this.directionsDisplay.getDirections().routes[0].legs[index]
            this.legs.push({
              start_address: leg.start_address,
              end_address: leg.end_address,
              duration: leg.duration,
              distance: leg.distance
            })
          }
        } else {
          window.alert('Directions request failed due to ' + status)
        }
      })
    }
  },

  components: {
    appLegTable: LegTable
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
