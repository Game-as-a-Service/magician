<template>
  <div>
    <!-- <HintBar
      :hint-text="'輪到你了！ 請選擇魔法！'"
      :change-color="'bg-purple text-white'"
    >
    </HintBar>
    <HintBar
      :hint-text="'遊戲開始'"
      :change-color="'bg-skin'"
    ></HintBar> -->
    <MainLayout></MainLayout>
  </div>
</template>

<script setup>
import MainLayout from '@/components/MainLayout.vue'
</script>

<style>
body{
  background-color: black;
}
</style>