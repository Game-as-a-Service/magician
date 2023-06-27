<script setup>

defineProps({
  isPop: {
    default: false,
    type: Boolean
  }
})
defineEmits([ 'close-pop' ])
</script>

<template>
  <div
    v-if="isPop"
    class="PopUpComponent"
    @click.self="$emit('close-pop')"
  >
    <div class="container">
      <div class="yt-full">
        <iframe
          class="yt-iframe" 
          src="https://www.youtube.com/embed/fGA1ZdJgRW8?autoplay=1"
          title="YouTube video player"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
        ></iframe>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.PopUpComponent {
  position: fixed;
  z-index: 10;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgba(#000, .6);
  inset: 0;

  .container {
    min-width: 300px;
    max-width: 80vw;
    max-height: 80vh;
  }

  .yt-full {
    position: relative;
    width: 70vw;
    margin-right: auto;
    margin-left: auto;
    padding-bottom: 56.25%;
  }

  .yt-iframe {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
  }
}
// xl | lg | md | sm
// @screen xl {}
</style>