<script setup>
import { computed } from 'vue'
import { useGameStore } from '@/stores/game'
const gameStore = useGameStore()
const secretNumber = computed(() => {
  if (!gameStore.gameStatus.secret_warehouse) return 0
  return gameStore.gameStatus.secret_warehouse.length
})
const unKnownNumber = computed(() => {
  if (!gameStore.gameStatus.warehouse) return 0
  return gameStore.gameStatus.warehouse.length
})
</script>

<template>
  <div class="flex bg-grey50 h-[120px] min-w-[150px] pt-[5px] px-[10px] flex-col items-start justify-evenly ">
    <h4 class="w-full text-white ">
      秘密魔法石 : {{ secretNumber }}
    </h4>
    <h4 class="w-full text-white ">
      未知的魔法石:  {{ unKnownNumber }}
    </h4>
  </div>
</template>