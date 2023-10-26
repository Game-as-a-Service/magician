<template>
  <div>
    <WarehouseSecret></WarehouseSecret>
    <WarehouseUnknown></WarehouseUnknown>

    <HintBar
      :hint-text="'輪到你了！ 請選擇魔法！'"
      :change-color="'bg-purple text-white'"
    >
    </HintBar>
    <HintBar
      :hint-text="'遊戲開始'"
      :change-color="'bg-skin'"
    ></HintBar>
    <router-view></router-view>
  </div>
</template>

<script setup>
// import HintBar from '@/components/common/HintBar.vue'
// import LadderBoard from '@/components/LadderBoard.vue'
import WarehouseUnknown from '@/components/WarehouseUnknown.vue'
import WarehouseSecret from '@/components/WarehouseSecret.vue'
</script>

<style>
body{
  background-color: black;
}
</style>