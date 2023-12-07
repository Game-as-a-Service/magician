<template>
  <div>
    <!-- <WarehouseSecret></WarehouseSecret>
    <WarehouseUnknown></WarehouseUnknown> -->
    <!-- <TableWithPlayer></TableWithPlayer> -->

    <HintBar
      :hint-text="'輪到你了！ 請選擇魔法！'"
      :change-color="'bg-purple text-white'"
    >
    </HintBar>
    <HintBar
      :hint-text="'遊戲開始'"
      :change-color="'bg-skin'"
    ></HintBar>
    <MyState></MyState>
  </div>
</template>

<script setup>
// import HintBar from '@/components/common/HintBar.vue'
// import LadderBoard from '@/components/LadderBoard.vue'
// import WarehouseUnknown from '@/components/WarehouseUnknown.vue'
// import WarehouseSecret from '@/components/WarehouseSecret.vue'
// import TableWithPlayer from '@/components/TableWithPlayer.vue'
// import BoardcastArea from '@/components/BoardcastArea.vue'
import MyState from '@/components/MyState.vue'
</script>

<style>
body{
  background-color: black;
}
</style>