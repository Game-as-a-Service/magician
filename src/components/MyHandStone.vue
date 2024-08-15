<script setup>
import {
  computed 
} from 'vue'

import { useGameStore } from '@/stores/game'
const gameStore = useGameStore()
const me = computed(() => gameStore.gameStatus.players.find((player) => player.player_id === gameStore.playingId))
const handStoneCount = computed(() => {
  if (!me.value) return 0
  return me.value.spells.length
})

</script>

<template>
  <div class="flex ml-4 gap-2 justify-end">
    <div
      v-for="item in handStoneCount"
      :key="item"
      class="w-[58px] aspect-[2/3]"
    >
      <img
        class="stone-back"
        src="@/assets/images/stone/stone.png"
      >
    </div>
  </div>
</template>

<style scoped>
.stone-back {
  border-radius: 5px;
  box-shadow: 4px 4px 5px 0px rgba(0, 0, 0, .6) inset, 4px 4px 4px 0px rgba(0, 0, 0, .6), -3px -3px 4px 0px rgba(0, 0, 0, .6) inset;
}
</style>