<script setup>
import { defineEmits } from 'vue'
import VideoBackground from 'vue-responsive-video-background-player'
defineEmits([ 'close' ])
</script>

<template>
  <div
    class="bg-grey50 z-50 w-full h-full top-0 left-0 absolute backdrop-blur-sm"
  >
    <VideoBackground
      src="/src/assets/video/magician05.mp4"
      style=" top: 50%;
  left: 50%;
  width: 760px;
  height: 540px;
  transform: translate(-50%, -50%);"
      :muted="true"
      :loop="false"
      @ended="showVideo=false"
    >
    </VideoBackground>
  </div>
</template>