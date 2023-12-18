<script setup>
import { defineEmits } from 'vue'
defineEmits([ 'close' ])
</script>

<template>
  <div class="bg-grey50 w-full h-full top-0 left-0 absolute backdrop-blur-sm">
    <div class="bg-cover w-[1000px] h-[700px] bottom-0 left-0  absolute pt-[120px] pb-[140px] px-[80px] flex ">
      <div class=" w-1/2 h-full  z-20 relative">
        <ul class="h-full px-8 list-disc flex flex-col justify-evenly">
          <li class=" mb-1 ">
            <p>Magic1-火爆的龍,共1張</p>
            <p>所有玩家將扣除等同於擲骰點數的生命值,不要怕！如果喊出但手牌中沒有此魔法,將遭到反噬,所以也必須擲骰子,骰出多少點數失去多生命值。</p>
          </li>
          <li class=" mb-1 ">
            <p>Magic2-黑暗幽靈,共2張,</p>
            <p>其他玩家將失去1點生命值,而你卻神秘地回復了1點生命值！</p>
          </li>
          <li class=" mb-1 ">
            <p>Magic3-甜蜜夢境,共3張,</p>
            <p>你將回復擲骰點數所代表的生命值,最高回復上限是6點,享受治癒的魔力吧！</p>
          </li>
          <li class=" mb-1 ">
            <p>Magic4-智慧鳥,共4張,</p>
            <p>你可以暗中查看1個秘密魔法石,蓋在自己面前。在這一輪結束時,每多蓋著1個魔法石,就能額外加1分,智慧鳥賦予你智慧和洞察力。</p>
          </li>
        </ul>
      </div>
      <div class=" w-1/2 h-full  z-20 relative flex-col">
        <ul class="h-full pl-[60px] list-disc flex flex-col justify-evenly">
          <li class=" mb-1 ">
            <p>Magic5-暴風雨,共5張,</p>
            <p>你的左右兩位玩家將不幸失去1點生命值,如同一場閃電狂風的猛烈打擊!</p>
          </li>
          <li class=" mb-1 ">
            <p>Magic6-暴雪,共6張,</p>
            <p>你的左手邊玩家將遭受暴雪的襲擊,失去1點生命值!</p>
          </li>
          <li class=" mb-1 ">
            <p>Magic7-火焰彈,共7張,</p>
            <p>你的右手邊玩家要小心了,他們將被你的火焰彈命中,損失1點生命值,將他們燃燒成灰燼!</p>
          </li>
          <li class=" mb-1 ">
            <p>Magic8-魔藥水,共8張,</p>
            <p>喝下一瓶魔藥水,恢復1點生命值,這瓶神奇的魔法藥水將帶來治癒與重生的力量!</p>
          </li>
        </ul>
      </div>
      <div
        class=" w-[80px] h-[80px] right-[15px] top-[70px] absolute z-40 bg-contain cursor-pointer"
        @click="$emit('close')"
      >
        <img
          class="absolute "
          src="/src/assets/images/book/close.png"
        > 
      </div>
      <img
        class="w-full h-full  top-0 left-0 absolute z-0 "
        src="/src/assets/images/book/magicBookOpen.png"
      > 
    </div>
    
    <!-- <p
      v-for="item of messages"
      :key="item"
      class="text-left w-full text-white font-medium mb-1"
    > 
      {{ item }}
    </p> -->
  </div>
</template>