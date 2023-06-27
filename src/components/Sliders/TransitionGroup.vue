<script setup>
import { ref } from 'vue'
const currentIndex = ref(0)
const sliderItem = ref(3)
const animateDirective = ref('slider-left')
const navigate = (number) => {
  if (number >= sliderItem.value){
    animateDirective.value = 'slider-left'
  } else if (number < 0){
    animateDirective.value = 'slider-right'
  }
  currentIndex.value = number
  reCalcCurrentIndex()
}
const reCalcCurrentIndex = () => {
  currentIndex.value = (currentIndex.value + sliderItem.value) % sliderItem.value
}
</script>

<template>
  <div class="TransitionGroup">
    <div class="container">
      <button
        class="btn directive-btn"
        @click="navigate(currentIndex-1)"
      >
        left
      </button>
      <TransitionGroup
        :name="animateDirective"
        tag="div"
        class="list"
      >
        <div
          v-for="(item,index) of sliderItem"
          v-show="index===currentIndex"
          :key="item"
          class="item"
          :class="`item-${item%3}`"
        >
          {{ item }}
        </div>
      </TransitionGroup>
      <button
        class="btn directive-btn"
        @click="navigate(currentIndex+1)"
      >
        right
      </button>
    </div>
    <div class="btn-group">
      <button
        v-for="(item,index) of sliderItem"
        :key="item"
        class="btn"
        :class="{ active: index===currentIndex }"
        @click="navigate(index)"
      ></button>
    </div>
  </div>
</template>

<style lang="scss">
.TransitionGroup {
  margin-bottom: 20px;

  .container {
    display: flex;
    align-items: center;
    max-width: 400px;
    margin-right: auto;
    margin-left: auto;
  }

  .directive-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 50px;
    height: 50px;
    color: #fff;
    background-color: #000;
  }

  .list {
    position: relative;
    width: 300px;
    height: 300px;
    overflow: hidden;
  }

  .item {
    position: absolute;
    left: 0;
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

  .slider-left-enter-active,
  .slider-left-leave-active,
  .slider-right-enter-active,
  .slider-right-leave-active {
    transition: all .5s ease;
  }

  .slider-left-enter-from {
    left: 100%;
  }

  .slider-right-enter-from {
    left: -100%;
  }

  .slider-left-enter-to {
    left: 0;
  }

  .slider-right-enter-to {
    left: 0;
  }

  .slider-left-leave-from {
    left: 0;
  }

  .slider-right-leave-from {
    left: 0;
  }

  .slider-left-leave-to {
    left: -100%;
  }

  .slider-right-leave-to {
    left: 100%;
  }
}
// xl | lg | md | sm
// @screen xl {}
</style>