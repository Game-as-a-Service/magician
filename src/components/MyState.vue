<script setup>
import { ref } from 'vue'

function getImageUrl (number) {
  const url = `/src/assets/images/stone/magic${ number }.png`
  return new URL(url, import.meta.url)
}
const secretStones = [ 5, 6, 7, 8 ]
const handStoneCount = ref(5)
</script>

<template>
  <div class="ScoreBoard bg-grey50 w-[450px] h-[322px] pt-[10px] px-[33px]">
    <p class="text-left w-full mt-1 mb-3 text-white font-medium"> 
      我的口袋
    </p>
    <div class="flex ml-4 gap-2">
      <div
        v-for="(stone, index) in secretStones"
        :key="index"
        class="w-[66px] h-[88px]"
      >
        <img
          class="stone-img"
          :src="getImageUrl(stone)"
        >  
      </div>
    </div>
    <p class="text-left w-full mt-8 mb-3 text-white font-medium"> 
      我的手牌
    </p>
    <div class="flex ml-4 gap-2">
      <div
        v-for="item in handStoneCount"
        :key="item"
        class="w-[66px] h-[88px]"
      >
        <img
          class="stone-back"
          :src="`/src/assets/images/stone/stone.png`"
        >  
      </div>
    </div>
  </div>
</template>

<style scoped>
.stone-img {
  border-radius: 5px;
  box-shadow: 4px 4px 5px 0px rgba(0, 0, 0, 0.30) inset, 4px 4px 4px 0px rgba(0, 0, 0, 0.25), -3px -3px 4px 0px rgba(0, 0, 0, 0.25) inset;
}
.stone-back {
  border-radius: 5px;
  box-shadow: 4px 4px 5px 0px rgba(0, 0, 0, 0.60) inset, 4px 4px 4px 0px rgba(0, 0, 0, 0.6), -3px -3px 4px 0px rgba(0, 0, 0, 0.6) inset;
}
</style>