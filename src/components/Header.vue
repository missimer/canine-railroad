<template>
  <ul class="nav nav-pills">
    <router-link to="/" tag="li" active-class="active" exact><a>Home</a></router-link>
    <router-link v-if="!$store.getters.IsLoggedIn"  to="/login" tag="li" active-class="active"><a>Login</a></router-link>
    <router-link v-if="$store.getters.IsLoggedIn" to="/user" tag="li" active-class="active"><a>User</a></router-link>
    <router-link v-if="$store.getters.IsLoggedIn" to="/trips" tag="li" active-class="active"><a>Trips</a></router-link>
    <router-link v-if="$store.getters.IsLoggedIn" to="/tripCreate" tag="li" active-class="active"><a>Create Trip</a></router-link>
  </ul>
</template>
