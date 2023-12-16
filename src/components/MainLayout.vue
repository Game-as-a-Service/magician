<script setup>
import LadderBoard from '@/components/LadderBoard.vue'
import ScoreBoard from '@/components/ScoreBoard.vue'
import WarehouseUnknown from '@/components/WarehouseUnknown.vue'
import WarehouseSecret from '@/components/WarehouseSecret.vue'
import TableWithPlayer from '@/components/TableWithPlayer.vue'
import BoardcastArea from '@/components/BoardcastArea.vue'
import OpponentTable from '@/components/OpponentTable.vue'
import MyState from '@/components/MyState.vue'
// import LeaveBtn from './LeaveBtn.vue'
import io from 'socket.io-client'
import { useGameStore } from '@/stores/game'
import {
  onMounted, ref, computed
} from 'vue'
const gameStore = useGameStore()
const socket = ref(null)
const playingId = computed(() => gameStore.playingId)
const playerId = ref('Leave3310')
const playerIds = [ 'Leave3310', 'Momo', 'Yock', 'Tux', 'Teds' ]

onMounted(() => {

})
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
</script>

<template>
  <div>
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
        >妳是誰？</label>
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
            class="focus:outline-none  text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800"
            @click="handleConnect"
          >
            連線
          </button>
        </div>
      </div>
    </div>
  </div>
</template>