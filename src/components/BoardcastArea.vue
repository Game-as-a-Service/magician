<template>
  <div class="ScoreBoard bg-grey50 w-[450px] h-[160px] px-[25px] pt-[10px] relative">
    <p
      v-for="item of messages"
      :key="item"
      class="text-left w-full text-white font-medium mb-1 last:bg-orange px-2"
    > 
      {{ item }}
    </p>
    <!-- <div class="absolute bottom-4 left-0 h-4 bg-pink w-full"></div> -->
  </div>
</template>

<script setup>
const messages = [ '遊戲開始', 'Leave3310的回合', 'Leave3310選擇施放7號魔法火球', '施放成功', 'Tux扣1HP' ]

</script>