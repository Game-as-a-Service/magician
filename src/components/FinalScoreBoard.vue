<script setup>
import { computed } from 'vue'
import { useGameStore } from '@/stores/game'
import imgSrcs from '@/models/Avatars.js'
const gameStore = useGameStore()

const players = computed(() =>
  gameStore.gameStatus.players.map((player, i) => ({
    name: player.player_id,
    score: player.score,
    imgSrc: imgSrcs[i],
  })).sort((a, b) => b.score - a.score)
)
const winner = computed(() => players.value[0].name)
</script>

<template>
  <div class="m-4">
    <h5 class="text-white font-bold text-center text-[64px] mb-3">
      遊戲結束, {{ winner }}獲勝!
    </h5>
    <div class="bg-black py-3 px-5 text-white bg-opacity-60 rounded-3xl">
      <div
        v-for="player of players"
        :key="player.name"
        class="flex items-center w-[700px] p-2 border-b border-grey70"
      >
        <div class="w-[60px] h-[60px]">
          <img :src="player.imgSrc">
        </div>
        <h6 class="pl-3 flex items-center text-[28px] ">
          <div class="truncate w-[240px]">
            {{ player.name }}
          </div>
          : {{ player.score }}分
        </h6>
      </div>
    </div>
    <div class="flex justify-evenly pt-4">
      <img src="/src/assets/images/sundries/door-leave.svg"> 
    </div>
  </div>
</template>

<style scoped>
.backgroundBlur {
  backdrop-filter: blur(2px);
}
</style>