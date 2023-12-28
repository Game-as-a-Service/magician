<script setup>
import { defineEmits } from 'vue'
defineEmits([ 'close' ])
function getImageUrl (number) {
  const url = `/src/assets/images/stone/magic${ number }.png`
  return new URL(url, import.meta.url)
}
</script>

<template>
  <div class="relative">
    <div class="w-[870px] h-[920px] grid grid-cols-3 absolute top-[190px] left-[270px]">
      <div
        v-for="i in 4"
        :key="i"
        class="border border-grey70 w-[120px] h-[143px] flex justify-center items-center"
      >
        <img
          class=""
          :src="getImageUrl(i)"
        >
      </div>
      <div></div>
      <div
        v-for="i in 4"
        :key="i"
        class="border border-grey70 w-[120px] h-[143px] flex justify-center items-center"
      >
        <img
          class=""
          :src="getImageUrl(i+4)"
        >
      </div>
    </div>
    <div class="absolute top-[450px] left-[980px]">
      <div class="parallelogram p-2">
        <p>Magic1-火爆的龍,共1張</p>
        <p>所有玩家將扣除等同於擲骰點數的生命值,不要怕！如果喊出但手牌中沒有此魔法,將遭到反噬,所以也必須擲骰子,骰出多少點數失去多生命值。</p>
      </div>
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