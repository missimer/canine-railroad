<template>
  <div class="input-group">
    <span class="input-group-addon"> {{ text }}</span>
    <input type="text" class="form-control waypoint-input" @blur="update" @keyup.enter="update" ref="inputField" :value="value" :placeholder="text">
    <img v-if="showDelete" style="cursor: pointer" @click="deleteField" src="../assets/delete.svg">
  </div>
</template>

<script>
export default {
  name: 'locationInput',

  props: ['text', 'linkPrefix', 'value', 'showDelete'],
  methods: {
    update () {
      this.$emit('input', this.$refs.inputField.value)
    },
    deleteField () {
      this.$emit('deleteField')
    }
  }
}
</script>

<style scoped>
.waypoint-input {
  width: calc(100% - 30px)
}
</style>
