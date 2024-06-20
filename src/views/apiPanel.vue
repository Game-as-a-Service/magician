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
const stones = [
  {
    name: 'Magic 1',
    label: '火爆的龍(1)',
  },
  {
    name: 'Magic 2',
    label: '黑暗幽靈(2)',
  },
  {
    name: 'Magic 3',
    label: '甜蜜夢境(3)',
  },
  {
    name: 'Magic 4',
    label: '智慧鳥(4)',
  },
  {
    name: 'Magic 5',
    label: '暴風雨(5)',
  },
  {
    name: 'Magic 6',
    label: '暴雪(6)',
  },
  {
    name: 'Magic 7',
    label: '火焰彈(7)',
  },
  {
    name: 'Magic 8',
    label: '魔藥水(8)',
  },
]
const gameId = ref('')
const messages = ref([])
const reversedMessages = computed(() => messages.value.slice().reverse())
const selectedPlayer = ref('Leave3310')
const selectedStone = ref('Magic 1')
const autoJoinCompletedText = ref('')
const autoJoinBaseTimer = ref(-1)
const autoJoinTimer = ref(0)
const resetAutoJoinTimer = () => {
  autoJoinTimer.value = autoJoinBaseTimer.value
  autoJoinCompletedText.value = ''
}
const cancelAutoJoin = () => {
  autoJoinTimer.value = 0
  autoJoinCompletedText.value = '取消自動加入房間'
}
const countDownAutoJoin = async () => {
  if (autoJoinBaseTimer.value < 0) return

  resetAutoJoinTimer()
  while (autoJoinTimer.value > 0) {
    await new Promise((resolve) => setTimeout(resolve, 1000))
    autoJoinTimer.value -= 1
  }

  autoJoinGameRoom()
}
const autoJoinGameRoom = async () => {
  autoJoinCompletedText.value = '自動加入房間中...'
  for (let playerId of playerIds) {
    const res = await api.put(`/player/${ playerId }/join`, {
      gameRoomID: gameId.value,
    })
    messages.value.push(`${ getTimeString() }: ${ res.data.message }`)
    await new Promise((resolve) => setTimeout(resolve, 100))
  }
  autoJoinCompletedText.value = '加入完成'
}
const handleCreateGame = async () => {
  const res = await api.post('/gameCreate', {
    playerIDs: playerIds,
  })
  gameId.value = res.data.gameRoomID
  messages.value.push(`${ getTimeString() }: ${ res.data.message }`)
  countDownAutoJoin()
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
    spellName: selectedStone.value,
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
    <div class="flex gap-4 p-4">
      <button
        v-if="gameId && autoJoinTimer > 0"
        class="bg-green-900 text-white py-2 px-4 rounded cursor-not-allowed"
      >
        創建房間
      </button>
      <button
        v-else
        class="bg-green-500 hover:bg-green-600 text-black py-2 px-4 border-b-4 border-green-700 hover:border-green-800 rounded"
        @click="handleCreateGame"
      >
        創建房間
      </button>
      <button
        v-if="gameId && autoJoinTimer > 0"
        class="bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 border-b-4 border-blue-700 hover:border-blue-800 rounded animate-pulse"
        @click="cancelAutoJoin"
      >
        {{ autoJoinTimer }} 秒後自動加入房間
      </button>
      <button
        v-if="autoJoinCompletedText"
        class="bg-blue-900 text-white py-2 px-4 rounded cursor-not-allowed"
      >
        {{ autoJoinCompletedText }}
      </button>

      <template v-if="true">
        <div class="flex gap-3 items-center">
          <label>
            <input
              id="disable-auto-join"
              v-model="autoJoinBaseTimer"
              type="radio"
              :value="-1"
            >
            取消自動加入房間
          </label>
          <label>
            <input
              id="enable-auto-join"
              v-model="autoJoinBaseTimer"
              type="radio"
              :value="1"
            >
            {{ 1 }} 秒後自動加入房間
          </label>
          <label>
            <input
              id="enable-auto-join"
              v-model="autoJoinBaseTimer"
              type="radio"
              :value="10"
            >
            {{ 10 }} 秒後自動加入房間
          </label>
        </div>
      </template>
    </div>
    <div class="flex gap-4">
      <div>當前房號</div>
      <div>{{ gameId }}</div>
      <div>
        <a
          :href="`#/?gameRoomID=${gameId}&playerId=${selectedPlayer}`"
          target="_blank"
          class="text-blue-500 hover:underline"
        >
          ↗️ 另開新分頁前往遊戲房間，(扮演玩家 {{ selectedPlayer }})
        </a>
      </div>
    </div>
    <div>
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
        <div class="flex flex-wrap">
          <template v-for="(stone, i) in stones">
            <button
              v-if="stone.name === selectedStone"
              :key="stone.name"
              type="button"
              class="mb-2 me-2 rounded-lg bg-blue-700 px-5 py-2.5 text-sm font-medium text-white hover:bg-blue-800"
            >
              {{ stone.label }}
            </button>
            <button
              v-else
              :key="i"
              type="button"
              class="mb-2 me-2 rounded-lg border border-gray-200 bg-white px-5 py-2.5 text-sm font-medium text-gray-900"
              @click="selectedStone = stone.name"
            >
              {{ stone.label }}
            </button>
          </template>
        </div>
      </div>
      <div class="p-4">
        <div>動作</div>
        <button
          class="bg-black border border-1 border-green-500 hover:bg-green-600 text-white py-2 px-4 border-b-4 hover:border-green-800 hover:text-black rounded-lg mb-2 me-2"
          @click="handleJoinGame"
        >
          玩家加入遊戲
        </button>
        <button
          class="bg-black border border-1 border-green-500 hover:bg-green-600 text-white py-2 px-4 border-b-4 hover:border-green-800 hover:text-black rounded-lg mb-2 me-2"
          @click="playStone"
        >
          施法
        </button>
        <button
          class="bg-black border border-1 border-green-500 hover:bg-green-600 text-white py-2 px-4 border-b-4 hover:border-green-800 hover:text-black rounded-lg mb-2 me-2"
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