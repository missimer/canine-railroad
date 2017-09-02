import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import User from '@/components/User'
import Login from '@/components/Login'
import Trips from '@/components/Trips'
import TripDetails from '@/components/TripDetails'
import TripCreate from '@/components/TripCreate'
import LegDetails from '@/components/LegDetails'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/user',
      name: 'User',
      component: User
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/trips',
      name: 'Trips',
      component: Trips
    },
    {
      path: '/tripCreate',
      name: 'TripCreate',
      component: TripCreate
    },
    {
      path: '/trips/:tripId',
      name: 'TripDetails',
      component: TripDetails,
      props: true
    },
    {
      path: '/trips/:tripId/leg/:legId',
      name: 'LegDetails',
      component: LegDetails,
      props: true
    }
  ]
})
