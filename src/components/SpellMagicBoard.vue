<script setup>
import { useGameStore } from '@/stores/game'
import {
  defineEmits, ref, computed 
} from 'vue'
defineEmits([ 'close' ])
function getImageUrl (number) {
  const url = `/src/assets/images/stone/magic${ number }.png`
  return new URL(url, import.meta.url)
}

// 上一次出牌
const lastMagic = ref(0)

import CountDown from './common/CountDown.vue'
const gameStore = useGameStore()
// const hoverItem = ref(0)
const focusMagic = computed(() => {
  return magicDesc[gameStore.hoverMagic]
})
const magicDesc = [
  {
    title: '',
    content: '',
  },
  {
    title: 'Magic1-火爆的龍,共1張',
    content:
      '所有玩家將扣除等同於擲骰點數的生命值,不要怕！如果喊出但手牌中沒有此魔法,將遭到反噬,所以也必須擲骰子,骰出多少點數失去多生命值。',
  },
  {
    title: 'Magic2-黑暗幽靈,共2張',
    content: '其他玩家將失去1點生命值,而你卻神秘地回復了1點生命值！',
  },
  {
    title: 'Magic3-甜蜜夢境,共3張',
    content:
      '你將回復擲骰點數所代表的生命值,最高回復上限是6點,享受治癒的魔力吧！',
  },
  {
    title: 'Magic4-智慧鳥,共4張',
    content:
      '你可以暗中查看1個秘密魔法石,蓋在自己面前。在這一輪結束時,每多蓋著1個魔法石,就能額外加1分,智慧鳥賦予你智慧和洞察力。',
  },
  {
    title: 'Magic5-暴風雨,共5張',
    content: '你的左右兩位玩家將不幸失去1點生命值,如同一場閃電狂風的猛烈打擊!',
  },
  {
    title: 'Magic6-暴雪,共6張',
    content: '你的左手邊玩家將遭受暴雪的襲擊,失去1點生命值!',
  },
  {
    title: 'Magic7-火焰彈,共7張,',
    content:
      '你的右手邊玩家要小心了,他們將被你的火焰彈命中,損失1點生命值,將他們燃燒成灰燼!',
  },
  {
    title: 'Magic8-魔藥水,共8張,',
    content:
      '喝下一瓶魔藥水,恢復1點生命值,這瓶神奇的魔法藥水將帶來治癒與重生的力量!',
  },
]
const setHoverMagic = (magicNumber) => {
  gameStore.setHoverMagic(magicNumber)
}
</script>

<template>
  <div class="relative">
    <div
      class="w-[870px] h-[920px] grid grid-cols-3 absolute top-[190px] left-[270px]"
    >
      <div
        v-for="i in 4"
        :key="i"
        class="border border-grey70 w-[120px] h-[143px] flex justify-center items-center"
      >
        <img
          v-if="lastMagic <= i"
          class="cursor-pointer"
          :src="getImageUrl(i)"
          @mouseenter="setHoverMagic(i)"
          @mouseleave="setHoverMagic(0)"
        >
        <img
          v-else
          src="/src/assets/images/stone/stone.png"
        >
      </div>
      <div></div>
      <div
        v-for="i in 4"
        :key="i"
        class="border border-grey70 w-[120px] h-[143px] flex justify-center items-center"
      >
        <img
          v-if="lastMagic <= i + 4"
          class="cursor-pointer"
          :src="getImageUrl(i + 4)"
          @mouseenter="setHoverMagic(i + 4)"
          @mouseleave="setHoverMagic(0)"
        >
        <img
          v-else
          src="/src/assets/images/stone/stone.png"
        >
      </div>
    </div>
    <div class="absolute top-[450px] left-[980px]">
      <div class="parallelogram p-2">
        <p>{{ focusMagic.title }}</p>
        <p>{{ focusMagic.content }}</p>
      </div>
    </div>
    <div class="absolute top-[666px] left-[1233px]">
      <CountDown></CountDown>
    </div>
    <div class="absolute top-[775px] rounded-lg left-[1233px] bg-white text-[#730000] text-3xl px-3 py-2">
      不施法
    </div>
  </div>
</template>

<style scoped>
.parallelogram {
  position: relative;
  width: 380px;
  height: 150px;
  margin: 50px; /* 可根据需要调整位置 */
  font-size: 20px;
  font-weight: 500;
  line-height: 27px;
  color: #fff;
  text-align: left;
  letter-spacing: 0em;
}

.parallelogram::before {
  content: '';
  position: absolute;
  top: 0;
  left: -10px;
  z-index: -1;
  width: 400px;
  height: 150px;
  margin: 0px; /* 可根据需要调整位置 */
  background-color: #730000;
  border-radius: 5px;
  transform: skew(-10deg);
}

</style>