<script setup>
import magicStones from '@/models/MagicStones.js'

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

const getMagicStoneUrl = (magicStone) => magicStones[`magic${ magicStone }`]
</script>

<template>
  <div class="flex">
    <div class="border border-grey70 bg-grey50 w-[60px] h-[76px] flex justify-center items-center">
      <img
        class="opacity-50"
        :src="getMagicStoneUrl(magicNumber)"
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