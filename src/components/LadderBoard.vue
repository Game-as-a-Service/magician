<script setup>
import { ref } from 'vue'
import LadderStep from '@/components/LadderStep.vue'
const usedMagic = ref([ 0, 0, 2, 0, 1, 2, 3, 7 ])
</script>

<template>
  <div class="p-[12px]">
    <LadderStep
      v-for="number in 8"
      :key="number"
      :magic-number="number"
      :used="usedMagic[number - 1]"
    ></LadderStep>
  </div>
</template>