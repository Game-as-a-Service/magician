<script setup>
import {
  defineEmits, computed 
} from 'vue'
import VideoBackground from 'vue-responsive-video-background-player'
import { useGameStore } from '@/stores/game'
import MagicVideo from '@/models/MagicVideo.js'

const gameStore = useGameStore()
defineEmits([ 'close' ])

const videoSrc = () => MagicVideo[`magic0${ gameStore.videoNumber }`]

const ended = () => {
  gameStore.showVideo = false
  if (gameStore.videoNumber === 4)
    gameStore.updateShowSecretTable(true)
  if (gameStore.videoNumber == 1 || gameStore.videoNumber == 3){
    gameStore.setShowDice(true)
  }
}
const afterAction = computed(() => {
  return !gameStore.afterAction
})
</script>

<template>
  <div
    class="bg-grey50 z-50 w-full h-full top-0 left-0 absolute backdrop-blur-sm"
  >
    <VideoBackground
      :src="videoSrc()"
      class="video"
      :muted="afterAction"
      :loop="false"
      @ended="ended"
    >
    </VideoBackground>
  </div>
</template>

<style scoped>
  div > .video {
    top: 50%;
    left: 50%;
    width: 760px;
    height: 540px;
    border-radius: 20px;
    transform: translate(-50%, -50%);
  }
</style>