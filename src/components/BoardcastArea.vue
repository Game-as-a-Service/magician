<script setup>
import { computed } from 'vue'
import { useGameStore } from '@/stores/game'
const gameStore = useGameStore()
// 抓最後14個訊息
const messages = computed(() => gameStore.messages.slice(-17))
// const messages = [ '遊戲開始', 'Leave3310的回合', 'Leave3310選擇施放7號魔法火焰彈', '施放成功', 'Teds扣1HP' ]
</script>

<template>
  <div class=" bg-grey50 w-[450px] h-[490px] px-[25px] pt-[10px] relative">
    <p
      v-for="(item, index) in messages"
      :key="`${item}-${index}`"
      class="text-left w-full text-white font-medium mb-1 last:bg-orange px-2"
    > 
      {{ item }}
    </p>
    <!-- <div class="absolute bottom-4 left-0 h-4 bg-pink w-full"></div> -->
  </div>
</template>