<script setup>
import { useGameStore } from '@/stores/game'
import { useIntervalFn } from '@vueuse/core'
import { computed } from 'vue'
import CountDown from './common/CountDown.vue'
// function getImageUrl (number) {
//   const url = `/src/assets/images/stone/magic${ number }.png`
//   return new URL(url, import.meta.url)
// }
const gameStore = useGameStore()
const secretNumber = computed(() => {
  if (!gameStore.gameStatus.secret_warehouse) return 1
  return gameStore.gameStatus.secret_warehouse.length + 1
})

const clickSecretStone = () => {
  gameStore.updateShowSecretTable(false)
  gameStore.restoreGameStatus()
  pause()
}
const {
  pause, resume 
} = useIntervalFn(() => {
  gameStore.secretCountDownTimer--
  if (gameStore.secretCountDownTimer === 0) {
    clickSecretStone() // 關閉秘密選擇面板
  }
}, 1000)
const resetTimer = () => {
  gameStore.secretCountDownTimer = 20
  resume()
}
resetTimer()
</script>

<template>
  <div class="secret-table w-1/2 flex flex-col items-center p-4 rounded-3xl">
    <div class="flex gap-8 p-4">
      <div
        v-for="i in secretNumber"
        :key="i"
        class="border border-grey70 w-[120px] h-[143px] flex justify-center items-center cursor-pointer"
        @click="clickSecretStone()"
      >
        <img src="/src/assets/images/stone/stone.png">
      </div>
    </div>
    <CountDown class="z-50"></CountDown>
  </div>
</template>

<style scoped>
.secret-table {
  background: linear-gradient(
    7deg, rgba(104, 17, 64, 1) 9%, rgba(244, 202, 152, 1) 100%
  );
}
</style>