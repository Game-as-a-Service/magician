<script setup>
import axios from 'axios'
import {
  computed, ref
} from 'vue'
const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
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
const autoJoinBaseTimer = ref(1)
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
    await new Promise((resolve) => setTimeout(resolve, 50))
  }
  autoJoinCompletedText.value = '加入完成'
}

const createGameBtnAvailable = ref(true)
const handleCreateGame = async () => {
  messages.value.push(`${ getTimeString() }: 創建房間中...`)
  createGameBtnAvailable.value = false

  try {
    const res = await api.post('/gameCreate', {
      playerIDs: playerIds,
    })
    gameId.value = res.data.gameRoomID
    messages.value.push(`${ getTimeString() }: ${ res.data.message }`)
    countDownAutoJoin()
  } catch (error) {
    messages.value.push(`${ getTimeString() }: 創建房間失敗，請閱讀錯誤訊息`)
  } finally {
    createGameBtnAvailable.value = true
  }
}

const handleJoinGame = async () => {
  const playerId = selectedPlayer.value
  const res = await api.put(`/player/${ playerId }/join`, {
    gameRoomID: gameId.value,
  })
  messages.value.push(`${ getTimeString() }: ${ res.data.message }`)
}

const playStoneBtnAvailable = ref(true)
const playStone = async () => {
  messages.value.push(`${ getTimeString() }: ${ selectedPlayer.value } 施放 ${ stones.find(stone => stone.name === selectedStone.value).label }...`)
  playStoneBtnAvailable.value = false
  try {
    const res = await api.patch('/stone', {
      gameRoomID: gameId.value,
      playerID: selectedPlayer.value,
      spellName: selectedStone.value,
    })
    const { message } = res.data
    switch (message) {
    case 'Spell cast failed':
      messages.value.push(`${ getTimeString() }: ${ selectedPlayer.value } 施法失敗`)
      break
    case 'Spell cast successfully':
      messages.value.push(`${ getTimeString() }: ${ selectedPlayer.value } 施法成功`)
      break

    default:
      messages.value.push(`${ getTimeString() }: ${ res.data.message }`)
      break
    }
  } catch (error) {
    if (error.response.status === 400) {
      switch (error.response.data.message) {
      case 'gameRoomID is required':
        messages.value.push(`${ getTimeString() }: 請先設定房間號碼`)
        break

        // TODO: Only `Spell cast failed` can not distinguish the error type
        // case 'Spell cast failed':
        //   messages.value.push(`${ getTimeString() }: ${ selectedPlayer.value } 並非當前玩家`)
        //   messages.value.push(`${ getTimeString() }: ${ selectedPlayer.value } 選擇了非法的數字`)
        //   break

      default:
        messages.value.push(`${ getTimeString() }: ${ error.response.data.message }`)
        break
      }
    } else {
      messages.value.push(`${ getTimeString() }: 施法失敗，請閱讀錯誤訊息`)
    }
  } finally {
    playStoneBtnAvailable.value = true
  }
}

const spellStopBtnAvailable = ref(true)
const spellStop = async () => {
  messages.value.push(`${ getTimeString() }: ${ selectedPlayer.value } 不再施法...`)
  spellStopBtnAvailable.value = false
  try {
    const playerId = selectedPlayer.value
    const res = await api.patch(`/player/${ playerId }/spellstop`, {
      gameRoomID: gameId.value,
    })
    messages.value.push(`${ getTimeString() }: ${ res.data.message }`)
  } catch (error) {
    messages.value.push(`${ getTimeString() }: 不再施法失敗，請閱讀錯誤訊息`)
  } finally {
    spellStopBtnAvailable.value = true
  }
}

const setGameId = () => {
  const id = prompt('請輸入房間號碼')
  if (id) {
    gameId.value = id
    messages.value.push(`${ getTimeString() }: 已設定房間號碼 ${ id }`)
  }
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
        class="py-2 px-4 border-b-4 border-green-900 rounded active:translate-y-1 transform transition"
        :class="createGameBtnAvailable
          ? 'bg-green-500 hover:bg-green-600 text-black'
          : 'bg-green-900 text-white cursor-not-allowed'"
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
          <label
            v-for="value of [-1,1,10]"
            :key="value"
            class="px-3 py-1.5 border cursor-pointer"
            :class="autoJoinBaseTimer === value ? ' border-gray-200 rounded-lg ' : 'border-transparent'"
          >
            <input
              v-model="autoJoinBaseTimer"
              type="radio"
              :value="value"
            >
            {{ value < 0 ? '取消自動加入房間' : `${ value } 秒後自動加入房間` }}
          </label>
        </div>
      </template>
    </div>
    <div
      v-if="!gameId"
      class="flex gap-4 p-4"
    >
      <button
        type="button"
        class="py-2 px-4 border-b-4 bg-green-500 text-black border-green-900 rounded active:translate-y-1 transform transition"
        @click="setGameId"
      >
        加入指定房間
      </button>
    </div>
    <div class="flex gap-4">
      <div>當前房號</div>
      <div>{{ gameId }}</div>
      <div>
        <a
          v-if="gameId"
          :href="`#/?gameRoomID=${gameId}&playerId=${selectedPlayer}`"
          target="_blank"
          class="text-blue-500 hover:underline"
        >
          ↗️ 另開新分頁前往遊戲房間，(扮演玩家 {{ selectedPlayer }})
        </a>
        <p
          v-else
          class="text-blue-500"
        >
          {{ createGameBtnAvailable ? '請先創建房間' : '創建房間中...' }}
        </p>
      </div>
    </div>
    <div>
      <div class="p-4">
        <div>選擇玩家</div>
        <div class="flex">
          <button
            v-for="playerId of playerIds"
            :key="playerId"
            type="button"
            class="mb-2 me-2 rounded-lg px-5 py-2.5 text-sm font-medium text-gray-900 hover:opacity-80 active:translate-y-1 transform transition"
            :class="playerId === selectedPlayer ? 'bg-blue-700 text-white' : 'bg-white text-gray-900'"
            @click="selectedPlayer = playerId"
          >
            {{ playerId }}
          </button>
        </div>
      </div>
      <div class="p-4">
        <div>選擇魔法</div>
        <div class="flex flex-wrap">
          <button
            v-for="{ name, label } of stones"
            :key="name"
            type="button"
            class="mb-2 me-2 rounded-lg px-5 py-2.5 text-sm font-medium text-gray-900 hover:opacity-80 active:translate-y-1 transform transition"
            :class="name === selectedStone ? 'bg-blue-700 text-white' : 'bg-white text-gray-900'"
            @click="selectedStone = name"
          >
            {{ label }}
          </button>
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
          class="bg-black border border-1 border-green-500 hover:bg-green-600 text-white min-w-[8rem] py-2 px-4 border-b-4 hover:border-green-800 hover:text-black rounded-lg mb-2 me-2 active:translate-y-1"
          :class="playStoneBtnAvailable ? '' : 'cursor-not-allowed'"
          @click="playStone"
        >
          {{ playStoneBtnAvailable ? '施法' : '施法中...' }}
        </button>
        <button
          class="bg-black border border-1 border-green-500 hover:bg-green-600 text-white min-w-[8rem] py-2 px-4 border-b-4 hover:border-green-800 hover:text-black rounded-lg mb-2 me-2 active:translate-y-1"
          :class="spellStopBtnAvailable ? '' : 'cursor-not-allowed'"
          @click="spellStop"
        >
          {{ spellStopBtnAvailable ? '不再施法' : '不再施法中...' }}
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