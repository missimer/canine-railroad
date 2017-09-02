<template>
  <div>
    <h1>
      Leg Details
    </h1>

    <div id="map"></div>
    <br> <br>
    <p>Distance: {{ routeDistance }}</p>
    <p>Duration: {{ routeDuration }}</p>
    <p>Start: Harrisburg, PA</p>
    <p>Destination: Allentown, PA</p>
    <p>Transporter: Eric</p>
    <hr>
    <p>Directions</p>
    <ul class="list-group">
    <li
      v-for="step in directions"
      v-html="step"
      class="list-group-item"> </li>
    </ul>
  </div>
</template>

<script>

/* global google */

export default {
  props: ['tripId', 'legId'],

  data () {
    return {
      directionResponse: null
    }
  },

  computed: {
    routeDistance () {
      if (this.directionResponse == null) {
        return 'N/A'
      } else {
        return this.directionResponse.routes[0].legs[0].distance.text
      }
    },
    routeDuration () {
      if (this.directionResponse == null) {
        return 'N/A'
      } else {
        return this.directionResponse.routes[0].legs[0].duration.text
      }
    },
    directions () {
      var dir = []
      if (this.directionResponse == null) {
        return ['Loading Directions']
      } else {
        for (var i = 0; i < this.directionResponse.routes[0].legs[0].steps.length; i++) {
          dir.push(this.directionResponse.routes[0].legs[0].steps[i].instructions)
        }
        return dir
      }
    }
  },

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
      this.directionsService.route({
        origin: 'Harrisburg, PA',
        destination: 'Allentown, PA',
        travelMode: 'DRIVING'
      }, (response, status) => {
        if (status === 'OK') {
          this.directionResponse = response
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

<style>
#map {
  height: 300px;
  width: 100%;
  margin: auto;
  background-color: lightgray;
}
</style>
