<template>
  <div>
    <div class="input-group">
      <span class="input-group-addon"> {{ field }} </span>
      <input type="text" class="form-control" ref="inputField" :placeholder="field" :value="value" @input="update">
    </div>
    <br>
  </div>
</template>

<script>
export default {
  name: 'userInput',
  props: ['field', 'value'],

  methods: {
    update: function () {
      this.$emit('input', this.$refs.inputField.value)
    }
  }
}
</script>
