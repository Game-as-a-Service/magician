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

const opponents = computed(() =>
  gameStore.gameStatus.players
    .map((player, i) => ({
      spell:
        i === gameStore.gameStatus.current_player
          ? spells[Math.floor(Math.random() * spells.length)]
          : '',
      avatar: imgSrcs[i],
      stone: player.spells.map((spell) => {
        switch (spell) {
        case 'Magic 1':
          return 'magic1'
        case 'Magic 2':
          return 'magic2'
        case 'Magic 3':
          return 'magic3'
        case 'Magic 4':
          return 'magic4'
        case 'Magic 5':
          return 'magic5'
        case 'Magic 6':
          return 'magic6'
        case 'Magic 7':
          return 'magic7'
        case 'Magic 8':
          return 'magic8'
        default:
          return ''
        }
      }),
      // .sort(a, b => a.localeCompare(b))
      secretStone: player.secret_spells.length,
      name: player.player_id,
      joined: player.joined,
    }))
    .filter((player) => player.name == gameStore.playingId)
)

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