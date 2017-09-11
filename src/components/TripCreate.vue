<template>
  <div>
  <h1>Create a new Trip</h1>
  <div id="map"></div>
  <br> <br>
  <app-location-input text="Start" :showDelete="false" v-model="start" @input="updateMap"> </app-location-input>
  <br>
  <draggable v-model="waypoints" @end="updateMap">
    <div
      v-for="(wp, index) in waypoints"
      :key="index">
      <app-location-input
        :text="'Dropoff ' + (index + 1)"
        v-model="wp.value"
        :showDelete="true"
        @deleteField="deleteWaypoint(index)"
        @input="updateMap">
      </app-location-input>
      <br>
    </div>
  </draggable>
  <app-location-input text="Destination" :showDelete="false" v-model="destination" @input="updateMap"> </app-location-input>
  <br>
  <div v-if="legs.length !== 0">
    <div>
      <div v-if="!newLegBoxDisplayed">
        <button class="btn btn-primary" @click="displayNewLegBox">
          Add New Leg
        </button>
      </div>
      <div class="bordered" v-else>
        <br>
        <p>Enter new leg</p>
        <p>
          After: <select v-model="newLegSelected">
          <option v-for="(leg, index) in legs" :value="leg.start_address">{{leg.start_address}}</option>
          </select>
          Dropoff: <input @keyup.enter="saveNewLeg" v-model="newLegLocation">
        </p>
        <button class="btn btn-primary" @click="saveNewLeg">
          Save
        </button>
        <button class="btn btn-danger" @click="newLegBoxDisplayed = false">
          Cancel
        </button>
        <br> <br>
    </div>

    <hr>
    <div>
      <h3>Legs</h3>
      <app-leg-table :legs="legs" linkPrefix="/tripCreate/leg/"></app-leg-table>
    </div>

    </div>
    <br> <br>
    <button class="btn btn-primary">
      Save Trip
    </button>
    <br> <br>
    </div>
  </div>
</template>

<script>
/* global google */

import LegTable from './LegTable.vue'
import LocationInput from './LocationInput.vue'
import draggable from 'vuedraggable'

export default {
  name: 'tripCreate',

  data () {
    return {
      directionService: null,
      directionsDisplay: null,
      start: '',
      destination: '',
      waypoints: [],
      newLegBoxDisplayed: false,
      newLegSelected: '',
      newLegLocation: '',
      legs: []
    }
  },
  methods: {
    deleteWaypoint (index) {
      this.waypoints.splice(index, 1)
      this.updateMap()
    },
    saveNewLeg () {
      this.waypoints.splice(this.waypoints.map((x) => { return x.value }).indexOf(this.newLegSelected) + 1, 0, {value: this.newLegLocation})
      this.newLegBoxDisplayed = false
      this.newLegLocation = ''
      this.updateMap()
    },
    displayNewLegBox () {
      if (this.start === '') {
        return
      }
      this.newLegBoxDisplayed = true
      this.newLegLocation = ''
      if (this.waypoints.length === 0) {
        this.newLegSelected = this.start
      } else {
        this.newLegSelected = this.waypoints[this.waypoints.length - 1].value
      }
    },
    updateLocations () {
      if (this.start === '' || this.destination === '') {
        return
      }
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

      this.start = this.legs[0].start_address
      this.destination = this.legs[this.legs.length - 1].end_address

      for (var i = 0; i < this.legs.length - 1; i++) {
        this.waypoints[i].value = this.legs[i].end_address
      }
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
        zoom: 4,
        center: {lat: 39.8283, lng: -98.5795}
      })
      this.directionsDisplay.setMap(map)
      this.directionsDisplay.addListener('directions_changed', () => {
        this.updateLocations()
      })
    }
  },

  components: {
    appLegTable: LegTable,
    appLocationInput: LocationInput,
    draggable
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
  height: 400px;
  width: 100%;
  margin: auto;
  background-color: lightgray;
}
.bordered {
  border: 1px solid #dddddd;
  box-sizing: border-box;
}
.sortable-ghost {
  opacity: .5;
}
</style>
