<script setup>
import { defineEmits } from 'vue'
import VideoBackground from 'vue-responsive-video-background-player'
defineEmits([ 'close' ])
</script>

<template>
    <div
        class="bg-grey50 z-50 w-full h-full top-0 left-0 absolute backdrop-blur-sm"
    >
        <video-background
            src="/src/assets/video/magician05.mp4"
            style="height: 540px; width: 760px; top:50%; left:50%; transform: translate(-50%, -50%);"
            :muted="true"
            :loop="false"
            @ended="showVideo=false"
            >
        </video-background>
    </div>
</template>