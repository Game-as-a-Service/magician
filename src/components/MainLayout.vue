<script setup>
import LadderBoard from '@/components/LadderBoard.vue'
import ScoreBoard from '@/components/ScoreBoard.vue'
import WarehouseUnknown from '@/components/WarehouseUnknown.vue'
import WarehouseSecret from '@/components/WarehouseSecret.vue'
import TableWithPlayer from '@/components/TableWithPlayer.vue'
import BoardcastArea from '@/components/BoardcastArea.vue'
import OpponentTable from '@/components/OpponentTable.vue'
import MyState from '@/components/MyState.vue'
import LeaveBtn from './LeaveBtn.vue'
import OpenedBook from './OpenedBook.vue'
</script>

<template>
  <div class=" bg-gray-700 w-[1440px] h-[1024px] p-8 relative">
    <div class="flex gap-11">
      <ScoreBoard></ScoreBoard>
      <WarehouseUnknown></WarehouseUnknown>
      <WarehouseSecret></WarehouseSecret>
    </div>
    <div class="absolute top-8 right-8">
      <OpponentTable></OpponentTable>
    </div>
    <div class="absolute bottom-8 left-8">
      <LadderBoard></LadderBoard>
    </div>
    <div class="absolute bottom-8 right-8">
      <BoardcastArea></BoardcastArea>
      <MyState class="mt-6"></MyState>
    </div>
    <div class="absolute top-[330px] left-[370px]">
      <TableWithPlayer></TableWithPlayer>
    </div>
    <div class="absolute top-[750px] left-[830px]">
      <div class="w-[100px] mr-2">
        <img src="/src/assets/images/book/book1.png">
      </div>
    </div>
    <div class="absolute bottom-8  left-[730px]">
      <LeaveBtn></LeaveBtn>
    </div>
    <div>
      <OpenedBook></OpenedBook>
    </div>
  </div>
</template>