<script setup>
import {
  computed 
} from 'vue'
import LadderStep from '@/components/LadderStep.vue'
import { useGameStore } from '@/stores/game'
const gameStore = useGameStore()
const usedMagic = computed(() => {
  return [ 1, 2, 3, 4, 5, 6, 7, 8 ].map(number => {
    if (!gameStore.gameStatus.ladder) return 0
    return gameStore.gameStatus.ladder.filter(stock => stock === `Magic ${ number }`).length
  })
})
// const usedMagic = ref([ 0, 0, 2, 0, 1, 2, 3, 7 ])
</script>

<template>
  <div>
    <LadderStep
      v-for="number in 8"
      :key="number"
      :magic-number="number"
      :used="usedMagic[number - 1]"
    ></LadderStep>
  </div>
</template>