<script setup>
import TableDesk from '@/components/TableDesk.vue'
function getImageUrl (name) {
  const url = `/src/assets/images/avatar/${ name }.png`
  return new URL(url, import.meta.url)
}

const players = [
  {
    name: 'Leave3310',
    hp: 1,
    imgSrc: getImageUrl('avatar_green'),
    playerClass: 'player-green',
  },
  {
    name: 'Yock',
    hp: 2,
    imgSrc: getImageUrl('avatar_yellow'),
    playerClass: 'player-yellow',
  },
  {
    name: 'Teds',
    hp: 3,
    imgSrc: getImageUrl('avatar_red'),
    playerClass: 'player-red',
  },
  {
    name: 'Cmomo',
    hp: 4,
    imgSrc: getImageUrl('avatar_orange'),
    playerClass: 'player-orange',
  },
  {
    name: 'Tux',
    hp: 5,
    imgSrc: getImageUrl('avatar_blue'),
    playerClass: 'player-blue',
  },
]
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
  top: 190px;
  left: 360px;
}
.player-red {
  top: 30px;
  left: 225px;
}
.player-yellow {
  top: 100px;
  left: 45px;
}
.player-blue {
  top: 345px;
  left: 245px;
}
.hp-player-green {
  top: calc(var(--center-y) + var(--length) * sin(72deg * 1 + var(--deg-angle)));
  left: calc(var(--center-x) + var(--length) * cos(72deg * 1 + var(--deg-angle)));
}
.hp-player-yellow {
  top: calc(var(--center-y) + var(--length) * sin(72deg * 2 + var(--deg-angle)));
  left: calc(var(--center-x) + var(--length) * cos(72deg * 2 + var(--deg-angle)));
}
.hp-player-red {
  top: calc(var(--center-y) + var(--length) * sin(72deg * 3 + var(--deg-angle)));
  left: calc(var(--center-x) + var(--length) * cos(72deg * 3 + var(--deg-angle)));
}
.hp-player-orange {
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