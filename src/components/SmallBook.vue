<script setup>
import {
  computed, inject
} from 'vue'
import MagicCircle from '@/assets/images/book/magic-circle.png'
import Book2 from '@/assets/images/book/book2.png'
const showBook = inject('showOpenedBook')
// const showBook = ref(false)
const magicCircleClass = computed(() => showBook.value ? 'magic-circle' : 'hidden')
// const magicBookClass = computed(() => showBook.value ? 'magic-book' : 'hidden')

</script>

<template>
  <div>
    <div
      class="group flex justify-end [&>img]:cursor-pointer"
      @click="showBook = true"
    >
      <img
        class="w-[100px] mr-2 group-hover:hidden"
        src="/src/assets/images/book/book1.png"
      />
      <img
        :src="Book2"
        class="hidden w-[100px] group-hover:block"
      />
    </div>
    <div 
      :class="magicCircleClass"
    >
      <img
        :src="MagicCircle"
      />
    </div>
  </div>
</template>

<style scoped>

@font-face {
  font-family: 'Custom magic bubble';
  src: url('/src/assets/fonts/jf-openhuninn-2.0.ttf')      format('ttf'),     url('/src/assets/fonts/jf-openhuninn-2.0.woff')      format('woff'),;
}
@font-face {
  font-family: 'Custom magic jh';
  src: url('/src/assets/fonts/JasonHandwriting4.ttf')      format('ttf'),     url('/src/assets/fonts/JasonHandwriting4.woff')      format('woff'),;
}

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

.font {
  font-family: 'Custom magic jh','Custom magic bubble',sans-serif;
  font-size: 16px;
  color: rgb(124, 107, 88);
  cursor: /* url('@/assets/cursor/magicwandmd.cur')5 5,auto; */
  url('@/assets/cursor/magicwand.cur') 15 15,auto;
  /* url('@/assets/cursor/oth269.cur') 5 5, auto ; */
}

.font li:hover {
  color: transparent;
  cursor: url('@/assets/cursor/magicwandmd.cur') 3 3,auto;
  background: linear-gradient(45deg, rgb(34, 43, 165) 0%, rgba(253, 29, 29, 1) 50%, rgb(228, 168, 85) 60%, rgb(22, 147, 28) 75%, rgb(34, 43, 165) 100%);
  -webkit-background-clip: text;
  background-size: 300% 120%;
  transition: all .4s;
  animation: animate-text 4s infinite linear;
}

@keyframes animate-text {
  0% {
    background-position: 0 0;
  }

  100% {
    background-position: -150% 0;
  }
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
    transform: translateX(100%) translateY(150%) rotate(100deg) scale(4);
    /* transform-origin: (50%,50%); */
  }

  55% {
    filter: blur(1px);
    transform: translateX(197%) translateY(330%) rotate(350deg) scale(4);
  }

  65% {
    filter: blur(3px);
    transform: translateX(197%) translateY(330%) rotate(343deg) scale(4);
  }

  75% {
    filter: blur(1px);
    transform: translateX(197%) translateY(330%) rotate(10deg) scale(4);
  }

  100% {
    filter: blur(0px);
    transform: translateX(197%) translateY(330%) rotate(15deg) scale(.6);
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