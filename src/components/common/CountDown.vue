<script setup>
import { useGameStore } from '@/stores/game'
const gameStore = useGameStore()
</script>

<template>
  <div class=" w-[160px] h-[76px] flex items-center place-content-center gap-4 ">
    <div class=" w-[60px] h-[60px] -rotate-6 bg-contain flex items-center mix-blend-soft-light shrink-0">
      <img src="/src/assets/images/sundries/timer.svg"> 
    </div>
    <p class="text-center text-white font-bold text-3xl"> 
      00:{{ gameStore.countDownTimer.toString().padStart(2, '0') }}
    </p>
  </div>
</template>