<template>
  <div>
    <HintBar
      :hint-text="'輪到你了！ 請選擇魔法！'"
      :change-color="'bg-purple text-white'"
    ></HintBar>
    <HintBar
      :hint-text="'遊戲開始'"
      :change-color="'bg-skin'"
    ></HintBar>
    <router-view></router-view>
  </div>
</template>

<script setup>
import HintBar from '@/components/common/HintBar.vue'
</script>

<style>
body{
  background-color: black;
}
</style>