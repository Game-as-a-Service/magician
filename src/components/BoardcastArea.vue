<template>
  <div class="ScoreBoard bg-grey50 w-[450px] h-[150px] px-[33px] pt-[10px] ">
    <p
      v-for="item of messages"
      :key="item"
      class="text-left w-full text-white font-medium"
    > 
      {{ item }}
    </p>
  </div>
</template>

<script setup>
const messages = [ '天蒼蒼野茫茫', '9527吃飯了', '天靈靈＃％＠！', 'Give me magic!', 'Give me a hand!' ]

</script>