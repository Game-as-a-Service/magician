<script setup>
import axios from 'axios'
import {
  computed, ref 
} from 'vue'
const api = axios.create({
  baseURL: 'https://gaas-magician-backend.azurewebsites.net/',
  headers: {
    'Content-Type': 'application/json',
  },
})
const playerIds = [ 'Leave3310', 'Momo', 'Yock', 'Tux', 'Teds' ]
const stoneNames = [ 'Magic 1', 'Magic 2', 'Magic 3', 'Magic 4', 'Magic 5', 'Magic 6', 'Magic 7', 'Magic 8' ]
const gameId = ref('')
const messages = ref([])
const reversedMessages = computed(() => messages.value.slice().reverse())
const selectedPlayer = ref('Leave3310')
const selectedStone = ref('Magic 1')
const handleCreateGame = async () => {
  const res = await api.post('/gameCreate', {
    playerIDs: playerIds,
  })
  gameId.value = res.data.gameRoomID
  messages.value.push(`${ getTimeString() }: ${ res.data.message }`)
}
const handleJoinGame = async () => {
  const playerId = selectedPlayer.value
  const res = await api.put(`/player/${ playerId }/join`, {
    gameRoomID: gameId.value,
  })
  messages.value.push(`${ getTimeString() }: ${ res.data.message }`)
}
const playStone = async () => {
  const res = await api.patch('/stone', {
    gameRoomID: gameId.value,
    playerID: selectedPlayer.value,
    spellName: selectedStone.value
  })
  messages.value.push(`${ getTimeString() }: ${ res.data.message }`)
}
const spellStop = async () => {
  const playerId = selectedPlayer.value
  const res = await api.patch(`/player/${ playerId }/spellstop`, {
    gameRoomID: gameId.value,
  })
  messages.value.push(`${ getTimeString() }: ${ res.data.message }`)
}
const getTimeString = () => {
  const date = new Date()
  const hours = date.getHours()
  const minutes = date.getMinutes()
  const seconds = date.getSeconds()
  return `${ hours }:${ minutes }:${ seconds }`
}
</script>

<template>
  <div class="text-green-400">
    <h1 class="text-green-400">
      API Test Panel
    </h1>
    <div class="p-4">
      <button
        class="bg-green-500 hover:bg-green-600 text-black py-2 px-4 border-b-4 border-green-700 hover:border-green-800 rounded"
        @click="handleCreateGame"
      >
        創建房間
      </button>
    </div>
    <div class="flex gap-4">
      <div>當前房號</div>
      <div>{{ gameId }}</div>
    </div>    <div>
      <div class="p-4">
        <div>選擇玩家</div>
        <div class="flex">
          <template v-for="(playerId, i) in playerIds">
            <button
              v-if="playerId === selectedPlayer"
              :key="playerId"
              type="button"
              class="mb-2 me-2 rounded-lg bg-blue-700 px-5 py-2.5 text-sm font-medium text-white hover:bg-blue-800"
            >
              {{ playerId }}
            </button>
            <button
              v-else
              :key="i"
              type="button"
              class="mb-2 me-2 rounded-lg border border-gray-200 bg-white px-5 py-2.5 text-sm font-medium text-gray-900"
              @click="selectedPlayer = playerId"
            >
              {{ playerId }}
            </button>
          </template>
        </div>
      </div>
      <div class="p-4">
        <div>選擇魔法</div>
        <div class="flex">
          <template v-for="(stone, i) in stoneNames">
            <button
              v-if="stone === selectedStone"
              :key="stone"
              type="button"
              class="mb-2 me-2 rounded-lg bg-blue-700 px-5 py-2.5 text-sm font-medium text-white hover:bg-blue-800"
            >
              {{ stone }}
            </button>
            <button
              v-else
              :key="i"
              type="button"
              class="mb-2 me-2 rounded-lg border border-gray-200 bg-white px-5 py-2.5 text-sm font-medium text-gray-900"
              @click="selectedStone = stone"
            >
              {{ stone }}
            </button>
          </template>
        </div>
      </div>
      <div class="p-4">
        <div>動作</div>
        <button
          class="bg-black border border-1 border-green-500 hover:bg-green-600 text-white py-2 px-4 border-b-4  hover:border-green-800 hover:text-black rounded-lg mb-2 me-2"
          @click="handleJoinGame"
        >
          玩家加入遊戲
        </button>
        <button
          class="bg-black border border-1 border-green-500 hover:bg-green-600 text-white py-2 px-4 border-b-4  hover:border-green-800 hover:text-black rounded-lg mb-2 me-2"
          @click="playStone"
        >
          施法
        </button>
        <button
          
          class="bg-black border border-1 border-green-500 hover:bg-green-600 text-white py-2 px-4 border-b-4  hover:border-green-800 hover:text-black rounded-lg mb-2 me-2"
          @click="spellStop"
        >
          不再施法
        </button>
      </div>
    </div>
    <div class="flex gap-4">
      <div>API 訊息</div>
      <div>
        <div
          v-for="(message, i) in reversedMessages"
          :key="i"
        >
          {{ message }}
        </div>  
      </div>
    </div>
  </div>
</template>