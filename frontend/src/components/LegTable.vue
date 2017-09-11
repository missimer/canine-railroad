<template>
  <table class="table table-bordered table-hover">
    <thead>
      <tr>
        <th>Start</th>
        <th>End</th>
        <th>Distance</th>
        <th>Duration</th>
      </tr>
    </thead>
    <tbody>
      <router-link
        v-for="(leg, index) in legs"
        tag="tr"
        :to="linkPrefix + index"
        :key="index"
        style="cursor: pointer; text-align:left">
          <td> {{ leg.start_address }} </td>
          <td> {{ leg.end_address }} </td>
          <td> {{ leg.distance.text }} </td>
          <td> {{ leg.duration.text }} </td>
      </router-link>
    </tbody>
  </table>
</template>

<script>
export default {
  name: 'legTable',
  props: ['legs', 'linkPrefix']
}
</script>
