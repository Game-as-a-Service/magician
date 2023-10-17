<template>
  <div
    class="-translate-y-2/4 fixed top-1/2 inset-x-0 text-center py-14 text-7xl leading-normal font-bold "
    :class="changeColor"
  >
    {{ hintText }}
  </div>
</template>

<script setup>

defineProps({
  hintText: {
    default: '',
    type: String,
  },
  changeColor: {
    default: '',
    type: String
  }
})
</script>