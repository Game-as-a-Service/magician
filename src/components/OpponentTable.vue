<script setup>
import { computed } from 'vue'
import { useGameStore } from '@/stores/game'
const gameStore = useGameStore()
const imgSrcs = [
  '/src/assets/images/avatar/avatar_green.png',
  '/src/assets/images/avatar/avatar_orange.png',
  '/src/assets/images/avatar/avatar_red.png',
  '/src/assets/images/avatar/avatar_yellow.png',
  '/src/assets/images/avatar/avatar_blue.png',
]
const opponents = computed(() => gameStore.gameStatus.players.map((player, i) => ({
  spell: i === gameStore.gameStatus.current_player ? spells[Math.floor(Math.random() * spells.length)] : '',
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
})).filter((player) => player.name !== gameStore.playingId))

// function getAvatarImgUrl (avatar) {
//   const url = `/src/assets/images/avatar/${ avatar }.png`
//   return new URL(url, import.meta.url)
// }

function getMagicStoneUrl (magicStone) {
  const url = `/src/assets/images/stone/${ magicStone }.png`
  return new URL(url, import.meta.url) 
}
const spells = [ '天蒼蒼野茫茫', '9527吃飯了', '天靈靈＃％＠！', 'Give me magic!', '霹靂卡霹靂拉拉', '快龍就是魯魯米', '你還是太年輕6', '讓我想一下', '去去爬爬走' ]

// const opponent = [
//   {
//     spell: spell[0],
//     avatar: 'avatar_blue',
//     stone: [ 'magic1', 'magic2', 'magic3', 'magic4', 'magic5' ],
//     secretStone: 0,
//   },
//   {
//     avatar: 'avatar_green',
//     stone: [ 'magic3', 'magic2', 'magic3', 'magic4', 'magic5' ],
//     secretStone: 0,
//   },
//   {
//     avatar: 'avatar_orange',
//     stone: [ 'magic4', 'magic5', 'magic5' ],
//     secretStone: 0,
//   },
//   {
//     // spell: spell[4],
//     avatar: 'avatar_red',
//     stone: [ 'magic6', 'magic6', 'magic6', 'magic6' ],
//     secretStone: 0,
//   },
// ]
</script>

<template>
  <div class="pt-2">
    <div
      v-for="opponent of opponents"
      :key="opponent.avatar"
      class="flex items-center mb-9"
    >
      <div class="w-[225px] mr-2.5 flex items-center justify-end">
        <span
          v-show="opponent.spell"
          class="rounded-t-full rounded-l-full bg-oldBook p-2.5 h-[60px] text-[28px]"
        >
          {{ opponent.spell }}
        </span>
      </div>

      <div class="w-[60px] mr-2">
        <img :src="opponent.avatar">
      </div>
      <div
        class="text-center pt-4 bg-[url('@/assets/images/sundries/pocket.png')] mr-2 w-[60px] h-[60px] text-gray-700 text-[28px]"
      >
        {{ opponent.secretStone }}
      </div>
      <div class="flex">
        <img
          v-for="(stone, i) of opponent.stone"
          :key="`${stone}-${i}`"
          :src="getMagicStoneUrl(stone)"
          class="px-0.5 w-[65px]"
        >
      </div>
    </div>
  </div>
</template>