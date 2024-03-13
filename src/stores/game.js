import { defineStore } from 'pinia'
import {
  ref, computed 
} from 'vue'
export const useGameStore = defineStore('useGameStore', () => {
  const gameStatus = ref({
    game_id: '',
    players: [ {
      'player_id': 'Leave3310', 'name': null, 'joined': false, 'score': 0, 'HP': 6, 'prev_spell': null, 'spells': [], 'secret_spells': [] 
    }, {
      'player_id': 'Momo', 'name': null, 'joined': false, 'score': 0, 'HP': 6, 'prev_spell': null, 'spells': [], 'secret_spells': [ 'Magic6 ' ] 
    }, {
      'player_id': 'Yock', 'name': null, 'joined': false, 'score': 0, 'HP': 6, 'prev_spell': null, 'spells': [], 'secret_spells': [ 'Magic 3', 'Magic 4' ] 
    }, {
      'player_id': 'Tux', 'name': null, 'joined': false, 'score': 0, 'HP': 6, 'prev_spell': null, 'spells': [], 'secret_spells': [ 'Magic 1', 'Magic 4' ] 
    }, {
      'player_id': 'Teds', 'name': null, 'joined': false, 'score': 0, 'HP': 6, 'prev_spell': null, 'spells': [], 'secret_spells': [] 
    } ], 'active': false, 'current_player': undefined, 'round': 0, 'turn': 0, 'secret_warehouse': [ 0, 0, 0, 0 ], 'warehouse': [], 'ladder': [] 
  })
  const playingId = ref('')
  const playingIndex = computed(() => {
    return gameStatus.value.players.findIndex(player => player.player_id === playingId.value)
  })
  const setGameStatus = (status) => {
    gameStatus.value = status
  }
  const hoverMagic = ref(0)
  const setHoverMagic = (magicNumber) => {
    hoverMagic.value = magicNumber
  }
  const myTurn = computed(() => {
    if (gameStatus.value.current_player === undefined) {
      return false
    }
    return gameStatus.value.players[gameStatus.value.current_player].player_id === playingId.value
  })
  const countDownTimer = ref(5)
  return {
    gameStatus,
    playingId,
    playingIndex,
    setGameStatus,
    hoverMagic,
    setHoverMagic,
    myTurn,
    countDownTimer,
  }
})