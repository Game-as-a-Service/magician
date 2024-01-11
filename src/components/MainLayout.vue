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
import MagicBoard from './MagicBoard.vue'
import HintBar from '@/components/common/HintBar.vue'
import io from 'socket.io-client'
import { useGameStore } from '@/stores/game'
import {
  ref, computed, watch 
} from 'vue'
const gameStore = useGameStore()
const socket = ref(null)
const playingId = computed(() => gameStore.playingId)
const playerId = ref('Leave3310')
const playerIds = [ 'Leave3310', 'Momo', 'Yock', 'Tux', 'Teds' ]
const showBook = ref(false)
const showHint = ref(false)
const handleConnect = () => {
  socket.value = io('https://gaas-magician-socketio.azurewebsites.net/', {
    transports: [ 'websocket', 'polling' ],
  })
  socket.value.on('connect', () => {
    console.log('socket connected')
    joinGame()
    // socket.value.emit({ player_id: 'Leave3310' })
  })
  socket.value.on('game_update', (data) => {
    console.log(data, 'game_update')
    gameStore.setGameStatus(JSON.parse(data))
  })
  socket.value.on('player_joined', (data) => {
    console.log(data, 'player_joined')
  })
}
const joinGame = () => {
  socket.value.emit('player_joined', { player_id: playerId.value }, () => {
    console.log(playerId.value, ' join')
    gameStore.playingId = playerId.value
  })
}
const showWarehouse = computed(() => {
  return gameStore.hoverMagic === 4
})
watch(
  () => gameStore.gameStatus.current_player,
  (newVal, oldVal) => {
    if (newVal !== oldVal) {
      if (newVal === undefined) return
      if (playerIds[newVal] === playingId.value) {
        showHint.value = true
        setTimeout(() => {
          showHint.value = false
        }, 1000)
      }
    }
  }
)
</script>

<template>
  <div>
    <div class="bg-gray-700 w-[1440px] h-[1024px] p-8 relative">
      <div class="flex gap-11">
        <ScoreBoard></ScoreBoard>
        <WarehouseUnknown></WarehouseUnknown>
        <WarehouseSecret
          :class="{ 'show-warehouse': showWarehouse }"
        ></WarehouseSecret>
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
      <div class="absolute z-50 top-[330px] left-[370px]">
        <TableWithPlayer></TableWithPlayer>
      </div>
      <div
        class="absolute top-[750px] left-[830px] cursor-pointer"
        @click="showBook = true"
      >
        <div class="w-[100px] mr-2">
          <img src="/src/assets/images/book/book1.png">
        </div>
      </div>
      <div class="absolute bottom-8 left-[730px]">
        <LeaveBtn></LeaveBtn>
      </div>
      <div v-if="showBook">
        <OpenedBook @close="showBook = false"></OpenedBook>
      </div>
      <div
        class="bg-grey50 top-0 left-0 w-full h-full backdrop-blur-sm absolute"
      >
        <MagicBoard></MagicBoard>
      </div>
      <HintBar
        v-if="showHint"
        :hint-text="'輪到你了！ 請選擇魔法！'"
        :change-color="'bg-purple text-white'"
      >
      </HintBar>
    </div>
    <div>
      <div
        v-if="playingId"
        class="text-white p-2"
      >
        您好，魔法師：{{ playingId }}
      </div>
      <div v-else>
        <label
          for="countries"
          class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        >你是誰？</label>
        <div class="flex gap-2">
          <select
            id="countries"
            v-model="playerId"
            class="w-40 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          >
            <option
              v-for="id in playerIds"
              :key="id"
              :value="id"
            >
              {{ id }}
            </option>
          </select>
          <button
            type="button"
            class="focus:outline-none text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800"
            @click="handleConnect"
          >
            連線
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scope>
.show-warehouse {
  z-index: 50;
  border: 5px solid #fff;
  border-style: outset;
  box-shadow: 5px 5px 5px rgba(0, 0, 0, .3) 0;
}
</style>