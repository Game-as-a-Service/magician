<script setup>
import { useGameStore } from '@/stores/game'
import {
  defineEmits, computed
} from 'vue'
import CountDown from './common/CountDown.vue'
defineEmits([ 'close' ])
// function getImageUrl (number) {
//   const url = `/src/assets/images/stone/magic${ number }.png`
//   return new URL(url, import.meta.url)
// }
const gameStore = useGameStore()
const secretNumber = computed(() => {
  if (!gameStore.gameStatus.secret_warehouse) return 0
  return gameStore.gameStatus.secret_warehouse.length
})
</script>

<template>
  <div class="secrect-table w-1/2 flex flex-col items-center p-4 rounded-3xl">
    <div
      class="flex gap-8 p-4"
    >
      <div
        v-for="i in secretNumber"
        :key="i"
        class="border border-grey70 w-[120px] h-[143px] flex justify-center items-center"
      >
        <img
          src="/src/assets/images/stone/stone.png"
        >
      </div>
    </div>
    <CountDown class="z-50"></CountDown>
  </div>
</template>

<style scoped>
.secrect-table {
  background: linear-gradient(7deg, rgba(104, 17, 64, 1) 9%, rgba(244, 202, 152, 1) 100%);
}
</style>