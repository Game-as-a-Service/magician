<script setup>
function getImageUrl (number) {
  const url = `/src/assets/images/stone/magic${ number }.png`
  return new URL(url, import.meta.url)
}
defineProps({
  magicNumber: {
    default: 1,
    type: Number,
  },
  used: {
    default: 0,
    type: Number,
  },
})
</script>

<template>
  <div class="flex">
    <div class="border border-grey70 bg-grey50 w-[60px] h-[76px] flex justify-center items-center">
      <img
        class="opacity-50"
        :src="getImageUrl(magicNumber)"
      >
    </div>
    <div
      v-for="number in magicNumber"
      :key="number"
      class="border border-grey70 bg-grey50 w-[60px] h-[76px]"
    >
      <img
        v-if="used >= number"
        :src="getImageUrl(magicNumber)"
      >
    </div>
    <div></div>
  </div>
</template>