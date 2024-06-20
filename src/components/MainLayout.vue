<script setup>
import PlayVideo from '@/components/PlayVideo.vue'
import LadderBoard from '@/components/LadderBoard.vue'
import ScoreBoard from '@/components/ScoreBoard.vue'
import FinalScoreBoard from '@/components/FinalScoreBoard.vue'
import WarehouseUnknown from '@/components/WarehouseUnknown.vue'
import WarehouseSecret from '@/components/WarehouseSecret.vue'
import TableWithPlayer from '@/components/TableWithPlayer.vue'
import BoardcastArea from '@/components/BoardcastArea.vue'
import OpponentTable from '@/components/OpponentTable.vue'
import MyState from '@/components/MyState.vue'
import LeaveBtn from './LeaveBtn.vue'
import OpenedBook from './OpenedBook.vue'
import SpellMagicBoard from './SpellMagicBoard.vue'
import SecretSelectTable from './SecretSelectTable.vue'
import HintBar from '@/components/common/HintBar.vue'
// import io from 'socket.io-client'
import { useGameStore } from '@/stores/game'
import {
  ref, computed, watch, onMounted 
} from 'vue'
import axios from 'axios'
import {
  useRouter, useRoute 
} from 'vue-router'
const api = axios.create({
  baseURL: 'https://gaas-magician-backend.azurewebsites.net/',
  headers: {
    'Content-Type': 'application/json',
  },
})
const route = useRoute()
const router = useRouter()
const gameStore = useGameStore()
const socket = ref(null)
const playingId = computed(() => gameStore.playingId)
const myTurn = computed(() => gameStore.myTurn)
const playerId = ref('Leave3310')
const playerIds = [ 'Leave3310', 'Momo', 'Yock', 'Tux', 'Teds' ]
const showHint1 = ref(false)
const showHintStart = ref(false)
const gameOver = computed(() => gameStore.gameOver)
const handleConnect = () => {
  socket.value = io(import.meta.env.VITE_SOCKET_IO_URL, {
    transports: [ 'websocket', 'polling' ],
  })
  socket.value.on('connect', () => {
    console.log('socket connected')
    joinGame()
    // handleJoinGame()
    // 因為panel已經加入過玩家 這裡再加一次會失敗
    // 須考慮之後從大平台加入時要如何加入game
    getGameStatus()
    // socket.value.emit({ player_id: 'Leave3310' })
  })
  socket.value.on('game_update', (data) => {
    const gameStatus = JSON.parse(data)
    console.log(gameStatus, 'game_update')
    if (
      gameStatus.game_id !== route.query.gameRoomID ||
      playerId.value !== route.query.playerId
    ) {
      router.push({
        path: route.path,
        query: {
          gameRoomID: gameStatus.game_id,
          playerId: playerId.value,
        },
      })
    }
    gameStore.updateTmpGameStatus(JSON.parse(data))
    if (!(gameStore.showVideo && gameStore.videoNumber === 4)) {
      gameStore.setGameStatus(JSON.parse(data))
    }
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
const getGameStatus = async () => {
  const gameRoomID = route.query.gameRoomID
  const player_id = route.query.playerId || playerId.value
  const params = {
    gameRoomID,
    player_id,
  }
  const res = await api.get('/player/status', {
    params,
  })
  gameStore.setGameStatus(res.data)
}
// const handleJoinGame = async () => {
//   const gameRoomID = route.query.gameRoomID
//   const playerId = route.query.playerId || playerId.value
//   await api.put(`/player/${ playerId }/join`, {
//     gameRoomID,
//   })
// }
watch(
  () => gameStore.gameStatus.current_player,
  (newVal, oldVal) => {
    if (newVal !== oldVal) {
      if (newVal === undefined) return
      if (playerIds[newVal] === playingId.value) {
        showHint1.value = true
        setTimeout(() => {
          showHint1.value = false
        }, 1000)
      }
    }
  }
)
watch(
  () => gameStore.gameStatus.current_player,
  (newCp, oldCp) => {
    if (oldCp === undefined) {
      showHintStart.value = true
      setTimeout(() => {
        showHintStart.value = false
      }, 1000)
    }
  }
)
onMounted(() => {
  if (route.query.gameRoomID && route.query.playerId) {
    playerId.value = route.query.playerId
    handleConnect()
  }
  console.log('mounted')
  console.log(import.meta.env.VITE_SOCKET_IO_URL)
})
const bgNumber = ref(Math.floor(Math.random() * 10))
const handleUserConnect = () => {
  handleConnect()
  if (route.query.gameRoomID) {
    router.push({
      path: route.path,
      query: {
        gameRoomID: route.query.gameRoomID,
        playerId: playerId.value,
      },
    })
  }
  router.push({
    path: route.path,
    query: {
      // gameRoomID: gameId.value,
      // gameId暫時沒用
      playerId: playerId.value,
    },
  })
}
</script>

<template>
  <div>
    <div
      :class="`bg-[url('@/assets/images/background/bg0` + bgNumber + `.webp')]`"
      class="bg-no-repeat bg-center bg-cover w-[1440px] h-[1024px] p-8 relative"
    >
      <div class="flex gap-11 top-8 left-8 absolute">
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
      <div class="absolute z-40 top-[330px] left-[370px]">
        <TableWithPlayer></TableWithPlayer>
      </div>
      
      <div class="absolute bottom-8 left-[730px]">
        <LeaveBtn></LeaveBtn>
      </div>
      <OpenedBook></OpenedBook>
      
      <div v-if="gameStore.showVideo">
        <PlayVideo>
        </PlayVideo>
      </div>      
      <div
        v-if="gameStore.showSecretTable"
        class="flex justify-center items-center bg-grey50 top-0 z-50 left-0 w-full h-full backgroundBlur absolute"
      >
        <SecretSelectTable></SecretSelectTable>
      </div>

      <HintBar
        v-if="showHint1"
        :hint-text="'輪到你了！ 請選擇魔法！'"
        :change-color="'bg-purple text-white'"
        class="z-50"
      >
      </HintBar>
      <HintBar
        v-if="showHintStart"
        :hint-text="'遊戲開始！'"
        :change-color="'bg-purple text-white'"
        class="z-50"
      >
      </HintBar>
      <div
        v-if="myTurn"
        class="bg-grey50 top-0 left-0 w-full h-full backgroundBlur absolute"
      >
        <SpellMagicBoard></SpellMagicBoard>
      </div>
      <div
        v-if="gameOver"
        class="bg-grey50 z-50 top-1/4 left-0 w-full backgroundBlur absolute flex justify-center items-center"
      >
        <FinalScoreBoard></FinalScoreBoard>
      </div>
    </div>
    <div>
      <div
        v-if="playingId"
        class="text-white p-2"
      >
        您好，魔法師：{{ playingId }}
      </div>
      <div class="user-switch-panel">
        <label
          for="countries"
          class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        >切換角色？</label>
        <div class="flex pl-5 pb-5 gap-3">
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
            @click="handleUserConnect"
          >
            連線
          </button>
          <button
            v-if="playerId !== playerIds[gameStore.gameStatus.current_player]"
            type="button"
            class="focus:outline-none text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
            @click="
              () => {
                playerId = playerIds[gameStore.gameStatus.current_player];

                handleUserConnect();
              }
            "
          >
            切換至當前玩家 (a.k.a.
            {{ playerIds[gameStore.gameStatus.current_player] }})
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

.backgroundBlur {
  backdrop-filter: blur(2px);
}

.backgroundBlur10 {
  backdrop-filter: blur(10px);
}
</style>