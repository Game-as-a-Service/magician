<script setup>
import {
  ref, onMounted 
} from 'vue'
import PopUp from '@/components/Youtube/PopUpComponent.vue'

const isPop = ref(false)
const closePop = () => {
  isPop.value = false
}
const openPop = () => {
  isPop.value = true
}
const youtubeSlot = ref(null)
const youtubeParams = ref({
  id: 'fGA1ZdJgRW8',
  isPop: false, 
  player: null,
  YTAPI: {
    isReady: false,
    isLoaded: false,
    URL: 'https://www.youtube.com/iframe_api',
    options: {}
  },
})

const init = async (el, options) => {
  await ready()
  setOption(options)
  return new window.YT.Player(el, youtubeParams.value.YTAPI.options)
}
const ready = () => {
  return youtubeParams.value.YTAPI.isReady ? Promise.resolve() : new Promise((resolve, reject) => {
    const scriptTag = document.createElement('script')
    scriptTag.src = youtubeParams.value.YTAPI.URL
    scriptTag.async = true

    scriptTag.onload = () => {
      youtubeParams.value.YTAPI.isLoaded = true
      window.onYouTubeIframeAPIReady = () => {
        youtubeParams.value.YTAPI.isReady = true
        resolve()
      }
    }
    scriptTag.onerror = () => {
      youtubeParams.value.YTAPI.isLoaded = true
      reject(new Error('Youtube script loaded fail'))
    }
    const firstScriptTag = document.body.getElementsByTagName('script')[0]
    firstScriptTag.parentNode.insertBefore(scriptTag, firstScriptTag)
  })
}
const setOption = (options) => {
  youtubeParams.value.YTAPI.options = options
}
const onReady = (e) => {
  e.target.playVideo()
}
const onStateChange = (e) => {
  const { ENDED } = window.YT.PlayerState
  if (e.data === ENDED){
    e.target.playVideo()
  }
}
onMounted(async () => {
  youtubeParams.value.player = await init(youtubeSlot.value, {
    videoId: youtubeParams.value.id,
    height: '720',
    width: '1280',
    playerVars: {
      controls: 0,
      mute: 1,
      rel: 0,
    },
    events: {
      onReady: onReady,
      onStateChange: onStateChange
    }
  })
})

</script>

<template>
  <div class="YoutubeComponent">
    <div class="container">
      <div class="yt-outer">
        <div
          class="fake-click"
          @click="openPop"
        ></div>
        <div
          ref="youtubeSlot"
          class="real-video"
        ></div>
      </div>
    </div>
    <PopUp
      :is-pop="isPop"
      @close-pop="closePop"
    ></PopUp>
  </div>
</template>

<style lang="scss">
.YoutubeComponent {
  .container {
    max-width: 840px;
    margin-right: auto;
    margin-left: auto;
  }

  .yt-outer {
    position: relative;
    padding-bottom: 56.25%;
  }

  .fake-click {
    position: absolute;
    z-index: 1;
    inset: 0;
  }

  .real-video {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
  }
}
// xl | lg | md | sm
// @screen xl {}
</style>