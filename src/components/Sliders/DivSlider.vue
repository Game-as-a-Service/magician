<script setup>
import {
  ref, computed, onMounted
} from 'vue'
import { useWindowSize } from '@vueuse/core'

const fakeList = computed(() => {
  return state.value.sliderItem * 3
})
const navigate = (number) => {
  state.value.currentIndex = number
  state.value.isTranslating = true
  state.value.buttonIndex = number
  reCalcButtonIndex()
}
const transitionendHandler = () => {
  state.value.isTranslating = false
  reCalcCurrentIndex()
}
const reCalcCurrentIndex = () => {
  state.value.currentIndex = (state.value.currentIndex + state.value.sliderItem) % state.value.sliderItem
}
const reCalcButtonIndex = () => {
  state.value.buttonIndex = (state.value.buttonIndex + state.value.sliderItem) % state.value.sliderItem
}
const state = ref({
  currentIndex: 0,
  buttonIndex: 0,
  sliderItem: 5,
  translateX: 0,
  itemWidth: 300,
  transitionDuration: '500',
  isTranslating: false,
  isDragging: false,
  startPosition: 0,
  draggingPosition: 0,
  timerId: 0,
  autoTime: 3000,
})
const {
  width
} = useWindowSize()
const calcPositionX = computed(() => {
  const windowWidth = Math.min(document.body.clientWidth, width.value)
  return (state.value.currentIndex + 0.5 + state.value.sliderItem) * state.value.itemWidth - windowWidth / 2
})
const animateStyle = computed(() => {
  return {
    transform: `translateX(-${ calcPositionX.value + state.value.draggingPosition }px)`,
    'transition-duration': state.value.isTranslating ? '500ms' : '0ms'
  }
})
const startDrag = (e) => {
  if (state.value.isDragging || state.value.isTranslating){
    return
  }
  stopAutoMove()
  state.value.isDragging = true
  state.value.startPosition = e.pageX
}
const dragging = (e) => {
  if (!state.value.isDragging){
    return
  }
  state.value.draggingPosition = state.value.startPosition - e.pageX 
}
const stopDrag = () => {
  const moveIndex = Math.round(state.value.draggingPosition / state.value.itemWidth) 
  if (moveIndex !== 0){
    navigate(state.value.currentIndex + moveIndex)
  }
  state.value.isDragging = false
  state.value.draggingPosition = 0
  startAutoMove()
}
const startAutoMove = () => {
  if (!state.value.timerId){
    state.value.timerId = setInterval(() => {
      navigate(state.value.currentIndex + 1)
    }, state.value.autoTime)
  }
}

const stopAutoMove = () => {
  // clearInterval不會把id刪除 所以要clear完後需重設定成0才有辦法再自動播放
  clearInterval(state.value.timerId)
  state.value.timerId = 0
}

onMounted(() => {
  startAutoMove()
})
</script>

<template>
  <div class="DivSlider">
    <div class="container">
      <div class="sliders">
        <div
          class="list"
          :style="animateStyle"
          @mouseover="stopAutoMove"
          @mousedown="startDrag"
          @touchstart="startDrag"
          @mousemove="dragging"
          @mouseleave="startAutoMove"
          @touchmove="dragging"
          @mouseup="stopDrag"
          @touchend="stopDrag"
          @transitionend="transitionendHandler"
        >
          <div
            v-for="(item) of fakeList"
            :key="item"
            class="item"
            :class="`item-${item%state.sliderItem}`"
          >
            {{ item }}
          </div>
        </div>
      </div>
      <div class="directive-group">
        <button
          class="btn directive-btn"
          @click="navigate(state.currentIndex-1)"
        >
          left
        </button>
        <button
          class="btn directive-btn"
          @click="navigate(state.currentIndex+1)"
        >
          right
        </button>
      </div>
      <div class="btn-group">
        <button
          v-for="(item,index) of state.sliderItem"
          :key="item"
          class="btn"
          :class="{ active: index===state.buttonIndex }"
          @click="navigate(index)"
        ></button>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
.DivSlider {
  .container {
    position: relative;
    margin-right: auto;
    margin-left: auto;
    overflow: hidden;
  }

  .directive-group {
    position: absolute;
    top: 50%;
    left: 50%;
    display: flex;
    justify-content: space-between;
    width: 100%;
    max-width: 400px;
    pointer-events: none;
    transform: translateY(-50%) translateX(-50%);
  }

  .directive-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 50px;
    height: 50px;
    color: #fff;
    pointer-events: all;
    background-color: #000;
  }

  .list {
    display: flex;
    width: 100%;
    height: 300px;
  }

  .item {
    display: flex;
    flex-shrink: 0;
    align-items: center;
    justify-content: center;
    width: 300px;
    height: 300px;
    font-size: 25px;
    font-weight: bold;
  }

  .btn-group {
    display: flex;
    justify-content: center;
    margin-top: 20px;

    & > button {
      width: 30px;
      height: 10px;
      margin-right: 10px;
      background-color: rgb(128, 128, 128);

      &.active {
        background-color: rgb(255, 0, 0);
      }
    }
  }

  .item-0 {
    background-color: rgb(183, 255, 0);
  }

  .item-1 {
    background-color: rgb(255, 145, 0);
  }

  .item-2 {
    background-color: rgb(0, 255, 229);
  }

  .item-3 {
    background-color: rgb(38, 65, 184);
  }

  .item-4 {
    background-color: rgb(194, 34, 128);
  }

  .item-5 {
    background-color: rgb(32, 170, 101);
  }
}
// xl | lg | md | sm
// @screen xl {}
</style>