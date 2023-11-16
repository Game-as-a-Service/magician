<script setup>
function getAvatarImgUrl (avatar) {
  const url = `/src/assets/images/avatar/${ avatar }.png`
  return new URL(url, import.meta.url)
}

function getMagicStoneUrl (magicStone) {
  const url = `/src/assets/images/stone/${ magicStone }.png`
  return new URL(url, import.meta.url)
}
const spell = [ '天蒼蒼野茫茫', '9527吃飯了', '天靈靈＃％＠！', 'Give me magic!' ]

const opponent = [
  {
    spell: spell[0],
    avatar: 'avatar_blue',
    stone: [ 'magic1', 'magic2', 'magic3', 'magic4', 'magic5' ],
    secretStone: 0,
  },
  {
    avatar: 'avatar_green',
    stone: [ 'magic3', 'magic2', 'magic3', 'magic4', 'magic5' ],
    secretStone: 0,
  },
  {
    avatar: 'avatar_orange',
    stone: [ 'magic4', 'magic5', 'magic5' ],
    secretStone: 0,
  },
  {
    avatar: 'avatar_red',
    stone: [ 'magic6', 'magic6', 'magic6', 'magic6' ],
    secretStone: 0,
  },
]
</script>

<template>
  <div>
    <div
      v-for="item of opponent"
      :key="item.avatar"
      class="flex items-center"
    >
      <div class="w-[225px] mr-2.5 flex items-center justify-end">
        <span
          v-show="item.spell"
          class="rounded-t-full rounded-l-full bg-oldBook p-2.5 h-[60px] text-[28px] font-medium"
        >
          {{ item.spell }}
        </span>
      </div>

      <div class="w-[60px] mr-2">
        <img :src="getAvatarImgUrl(item.avatar)">
      </div>
      <div
        class="text-center pt-4 bg-[url('@/assets/images/sundries/pocket.png')] mr-2 w-[60px] h-[60px] text-grey text-[28px]"
      >
        {{ item.secretStone }}
      </div>
      <div class="flex">
        <img
          v-for="stone of item.stone"
          :key="stone"
          :src="getMagicStoneUrl(stone)"
          class="px-0.5 w-[65px]"
        >
      </div>
    </div>
  </div>
</template>