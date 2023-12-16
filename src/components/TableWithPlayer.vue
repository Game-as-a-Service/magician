<script setup>
import { computed } from 'vue'
import TableDesk from '@/components/TableDesk.vue'
import { useGameStore } from '@/stores/game'
const gameStore = useGameStore()
const imgSrcs = [
  '/src/assets/images/avatar/avatar_green.png',
  '/src/assets/images/avatar/avatar_orange.png',
  '/src/assets/images/avatar/avatar_red.png',
  '/src/assets/images/avatar/avatar_yellow.png',
  '/src/assets/images/avatar/avatar_blue.png',
]
const playerClasses = [
  'player-green',
  'player-orange',
  'player-red',
  'player-yellow',
  'player-blue',
]
const players = computed(() => gameStore.gameStatus.players.map((player, i) => ({
  name: player.player_id,
  hp: player.HP,
  score: player.score,
  imgSrc: imgSrcs[i],
  playerClass: playerClasses[i],
})))
// function getImageUrl (name) {
//   const url = `/src/assets/images/avatar/${ name }.png`
//   return new URL(url, import.meta.url)
// }

// const players = [
//   {
//     name: 'Leave3310',
//     hp: 6,
//     imgSrc: getImageUrl('avatar_green'),
//     playerClass: 'player-green',
//   },
//   {
//     name: 'Yock',
//     hp: 6,
//     imgSrc: getImageUrl('avatar_yellow'),
//     playerClass: 'player-yellow',
//   },
//   {
//     name: 'Teds',
//     hp: 6,
//     imgSrc: getImageUrl('avatar_red'),
//     playerClass: 'player-red',
//   },
//   {
//     name: 'Cmomo',
//     hp: 6,
//     imgSrc: getImageUrl('avatar_orange'),
//     playerClass: 'player-orange',
//   },
//   {
//     name: 'Tux',
//     hp: 5,
//     imgSrc: getImageUrl('avatar_blue'),
//     playerClass: 'player-blue',
//   },
// ]
</script>

<template>
  <div class="w-[480px] h-[480px] relative flex justify-center items-center ">
    <div
      v-for="item of players"
      :key="item.name"
      class="w-[100px] h-[100px] absolute"
      :class="item.playerClass"
    >
      <img :src="item.imgSrc">
    </div>
    <div
      v-for="item of players"
      :key="item.name"
      class="absolute"
      :class="`hp-${item.playerClass}`"
    >
      <div class="text-5xl font-bold">
        {{ item.hp }}
      </div>
    </div>
    <TableDesk></TableDesk>
  </div>
</template>

<style>
.player-green {
  top: 295px;
  left: 60px;
}

.player-orange {
  top: 100px;
  left: 45px;
}

.player-red {
  top: 30px;
  left: 225px;
}

.player-yellow {

  top: 190px;
  left: 360px;
}

.player-blue {
  top: 345px;
  left: 245px;
}

.hp-player-green {
  top: calc(var(--center-y) + var(--length) * sin(72deg * 1 + var(--deg-angle)));
  left: calc(var(--center-x) + var(--length) * cos(72deg * 1 + var(--deg-angle)));
}

.hp-player-orange {
  top: calc(var(--center-y) + var(--length) * sin(72deg * 2 + var(--deg-angle)));
  left: calc(var(--center-x) + var(--length) * cos(72deg * 2 + var(--deg-angle)));
}

.hp-player-red {
  top: calc(var(--center-y) + var(--length) * sin(72deg * 3 + var(--deg-angle)));
  left: calc(var(--center-x) + var(--length) * cos(72deg * 3 + var(--deg-angle)));
}

.hp-player-yellow {
  top: calc(var(--center-y) + var(--length) * sin(72deg * 4 + var(--deg-angle)));
  left: calc(var(--center-x) + var(--length) * cos(72deg * 4 + var(--deg-angle)));
}

.hp-player-blue {
  top: calc(var(--center-y) + var(--length) * sin(72deg * 0 + var(--deg-angle)));
  left: calc(var(--center-x) + var(--length) * cos(72deg * 0 + var(--deg-angle)));
}

:root {
  --deg-angle: 69deg;
  --length: 90px;
  --center-x: 227px;
  --center-y: 215px;
}

</style>