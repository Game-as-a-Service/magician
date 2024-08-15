<script setup>
import {
  computed 
} from 'vue'

import { useGameStore } from '@/stores/game'
import magicStones from '@/models/MagicStones'

const gameStore = useGameStore()
const me = computed(() => gameStore.gameStatus.players.find((player) => player.player_id === gameStore.playingId))

const getMagicStoneUrl = (magicStone) => magicStones[`magic${ magicStone }`]
const secretStones = computed(() => {
  if (!me.value) return []

  return me.value.secret_spells.map((spell) => {
    switch (spell) {
    case 'Magic 1':
      return 1 
    case 'Magic 2':
      return 2
    case 'Magic 3':
      return 3
    case 'Magic 4':
      return 4
    case 'Magic 5':
      return 5
    case 'Magic 6':
      return 6
    case 'Magic 7':
      return 7
    case 'Magic 8':
      return 8
    default:
      return 0
    }
  }).sort((a, b) => a - b)
})

// 如果要 debug 直接註解拿掉
// const secretStones = [ 5, 6, 7, 8 ]
// const handStoneCount = computed(() => {
//   if (!me.value) return 0
//   return me.value.spells.length
// })
// </script>

<template>
  <div class=" bg-grey50 w-[250px] h-[120px] pt-[5px] px-[10px]">
    <p class="text-left w-full mt-1 mb-3 text-white font-medium"> 
      我的口袋
    </p>
    <div class="flex ml-4 gap-2">
      <div
        v-for="(stone, index) in secretStones"
        :key="index"
        class="w-[44px] aspect-[2/3]"
      >
        <img
          class="stone-img"
          :src="getMagicStoneUrl(stone)"
        >  
      </div>
    </div>
    
    <!-- //我的手牌 -->
    <!-- <div class="flex ml-4 gap-2">
      <div
        v-for="item in handStoneCount"
        :key="item"
        class="w-[66px] h-[88px]"
      >
        <img
          class="stone-back"
          src="@/assets/images/stone/stone.png"
        >
      </div>
    </div> -->
  </div>
</template>

<style scoped>
.stone-img {
  border-radius: 5px;
  box-shadow: 4px 4px 5px 0px rgba(0, 0, 0, .3) inset, 4px 4px 4px 0px rgba(0, 0, 0, .25), -3px -3px 4px 0px rgba(0, 0, 0, .25) inset;
}

.stone-back {
  border-radius: 5px;
  box-shadow: 4px 4px 5px 0px rgba(0, 0, 0, .6) inset, 4px 4px 4px 0px rgba(0, 0, 0, .6), -3px -3px 4px 0px rgba(0, 0, 0, .6) inset;
}
</style>