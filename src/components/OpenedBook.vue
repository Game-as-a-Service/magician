<script setup>
import {
  computed, ref 
} from 'vue'

import CloseIcon from '@/assets/images/book/CloseIcon.vue'
import MagicCircle from '@/assets/images/book/magic-circle.png'
import Book2 from '@/assets/images/book/book2.png'

const showBook = ref(false)
const magicCircleClass = computed(() => showBook.value ? 'magic-circle' : 'hidden')
const magicBookClass = computed(() => showBook.value ? 'magic-book' : 'hidden')
</script>

<template>
  <div
    class="absolute top-[750px] left-[830px] "
  >
    <div
      class="group cursor-pointer"
      @click="showBook = true"
    >
      <img
        class="w-[100px] mr-2 group-hover:hidden"
        src="/src/assets/images/book/book1.png"
      >
      <img
        :src="Book2"
        class="hidden w-[100px] group-hover:block"
      >
    </div>
    <div 
      :class="magicCircleClass"
    >
      <img
        :src="MagicCircle"
      >
    </div>
  </div>
  <div
    class="bg-grey50 z-50 w-full h-full top-0 left-0 absolute backdrop-blur-sm magic-book"
    :class="magicBookClass"
  >
    <div
      class="bg-cover w-[1000px] h-[700px] bottom-0 left-0 absolute pt-[120px] pb-[140px] px-[80px] flex"
    >
      <div class="w-1/2 h-full z-20 relative">
        <ul class="h-full px-8 list-disc flex flex-col justify-evenly">
          <li class="mb-1">
            <p>Magic1-火爆的龍,共1張</p>
            <p>
              所有玩家將扣除等同於擲骰點數的生命值,不要怕！如果喊出但手牌中沒有此魔法,將遭到反噬,所以也必須擲骰子,骰出多少點數失去多生命值。
            </p>
          </li>
          <li class="mb-1">
            <p>Magic2-黑暗幽靈,共2張,</p>
            <p>其他玩家將失去1點生命值,而你卻神秘地回復了1點生命值！</p>
          </li>
          <li class="mb-1">
            <p>Magic3-甜蜜夢境,共3張,</p>
            <p>
              你將回復擲骰點數所代表的生命值,最高回復上限是6點,享受治癒的魔力吧！
            </p>
          </li>
          <li class="mb-1">
            <p>Magic4-智慧鳥,共4張,</p>
            <p>
              你可以暗中查看1個秘密魔法石,蓋在自己面前。在這一輪結束時,每多蓋著1個魔法石,就能額外加1分,智慧鳥賦予你智慧和洞察力。
            </p>
          </li>
        </ul>
      </div>
      <div class="w-1/2 h-full z-20 relative flex-col">
        <ul class="h-full pl-[60px] list-disc flex flex-col justify-evenly">
          <li class="mb-1">
            <p>Magic5-暴風雨,共5張,</p>
            <p>
              你的左右兩位玩家將不幸失去1點生命值,如同一場閃電狂風的猛烈打擊!
            </p>
          </li>
          <li class="mb-1">
            <p>Magic6-暴雪,共6張,</p>
            <p>你的左手邊玩家將遭受暴雪的襲擊,失去1點生命值!</p>
          </li>
          <li class="mb-1">
            <p>Magic7-火焰彈,共7張,</p>
            <p>
              你的右手邊玩家要小心了,他們將被你的火焰彈命中,損失1點生命值,將他們燃燒成灰燼!
            </p>
          </li>
          <li class="mb-1">
            <p>Magic8-魔藥水,共8張,</p>
            <p>
              喝下一瓶魔藥水,恢復1點生命值,這瓶神奇的魔法藥水將帶來治癒與重生的力量!
            </p>
          </li>
        </ul>
      </div>
      <div
        class="group right-[-46px] top-[86px] absolute z-40 cursor-pointer flex items-center"
        @click="showBook=false"
      >
        <div
          class="absolute left-[-10px] z-[-1] bg-transparent py-2 px-[10px] rounded-[20px] w-1/2 group-hover:w-[calc(100%+20px)] h-[100px] group-hover:bg-white transition-all"
        ></div>
        <CloseIcon
          class="w-[80px] fill-[#F7F7F7] group-hover:fill-[#730000] transition-all group-hover:rotate-180 mr-[14px]"
        ></CloseIcon>
        <div
          class="text-[28px] font-medium text-transparent group-hover:text-[#730000] shrink-0 transition-colors"
        >
          收起
        </div>
      </div>
      <img
        class="w-full h-full top-0 left-0 absolute z-0"
        src="/src/assets/images/book/magicBookOpen.png"
      >
    </div>
  </div>
</template>

<style scoped>
.magic-circle {
  position: absolute;
  top: 0px;
  z-index: 100;
  width: 95px;
  height: 95px;
  animation: animate-magic-circle 3s forwards;
}

.magic-book {
  opacity: 0;
  animation: animate-magic-book 1s 2.2s forwards;
}

@keyframes animate-magic-circle {
  0% {
    position: absolute;
    filter: blur(2px);
    opacity: 0;
    transform: translateX(0%) translateY(10%) rotate(0deg) scale(0);
    transform-origin: (50%,50%);
  }

  30% {
    filter: blur(2px);
    opacity: 1;
    transform: translateX(2%) translateY(0%) rotate(0deg) scale(1);
    /* transform-origin: (50%,50%); */
  }

  45% {
    filter: blur(0px);
    transform: translateX(-280%) translateY(-240%) rotate(343deg) scale(4);
    /* transform-origin: (50%,50%); */
  }

  55% {
    filter: blur(1px);
    transform: translateX(-280%) translateY(-240%) rotate(350deg) scale(4);
  }

  65% {
    filter: blur(3px);
    transform: translateX(-280%) translateY(-240%) rotate(343deg) scale(4);
  }

  75% {
    filter: blur(1px);
    transform: translateX(-280%) translateY(-240%) rotate(10deg) scale(4);
  }

  100% {
    filter: blur(0px);
    transform: translateX(36%) translateY(60%) rotate(15deg) scale(.6);
  }
}

@keyframes animate-magic-book {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}
</style>