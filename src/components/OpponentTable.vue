<script setup>
import { computed } from 'vue'
import { useGameStore } from '@/stores/game'
import imgSrcs from '@/models/Avatars.js'
import magicStones from '@/models/MagicStones.js'
const gameStore = useGameStore()
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
        case 'Magic Stone':
          return 'MagicStone'
        default:
          return ''
        }
      }),
      // .sort(a, b => a.localeCompare(b))
      secretStone: player.secret_spells.length,
      name: player.player_id,
      joined: player.joined,
    }))
    // .filter((player) => player.name !== gameStore.playingId)
)

// const myHandStone= computed(() =>
// opponents.value.filter((player) => player.name == gameStore.playingId)
// );
// const notMyHandStone= computed(() =>
// opponents.value.filter((player) => player.name !== gameStore.playingId)
// );

function getMagicStoneUrl (magicStone) {
  return magicStones[magicStone]
}
const spells = [
  '天蒼蒼野茫茫',
  '9527吃飯了',
  '天靈靈＃％＠！',
  'Give me magic!',
  '霹靂卡霹靂拉拉',
  '快龍就是魯魯米',
  '你還是太年輕6',
  '讓我想一下',
  '去去爬爬走',
  '左欺敵右欺敵',
  '鄰兵火力掩護我',
  '吃雞大吉大利',
  '地球防衛軍',
]

</script>

<template>
  <div class="pt-2">
    <div
      v-for="opponent of opponents"
      :key="opponent.avatar"
      class="flex items-center mb-4"
    >
      <div class="w-[225px] mr-2.5 flex items-center justify-end">
        <span
          v-show="opponent.spell"
          class="rounded-t-full rounded-l-full bg-oldBook p-2.5 h-[60px] text-[28px]"
        >
          {{ opponent.spell }}
        </span>
        <span
          v-if="!opponent.joined"
          class="rounded-t-full rounded-l-full bg-oldBook p-2.5 h-[60px] text-[28px]"
        >
          等等我～
        </span>
      </div>

      <div class="w-[60px] mr-2">
        <img :src="opponent.avatar">
      </div>
      <div
        :class="
          opponent.secretStone !== 0
            ? `bg-[url('@/assets/images/sundries/pocket-pink.png')]`
            : `bg-[url('@/assets/images/sundries/pocket.png')] `
        "
        class="text-center pt-4 mr-2 w-[60px] h-[60px] text-gray-700 text-[28px]"
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