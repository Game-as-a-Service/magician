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
      'player_id': 'Momo', 'name': null, 'joined': false, 'score': 0, 'HP': 6, 'prev_spell': null, 'spells': [], 'secret_spells': [] 
    }, {
      'player_id': 'Yock', 'name': null, 'joined': false, 'score': 0, 'HP': 6, 'prev_spell': null, 'spells': [], 'secret_spells': [] 
    }, {
      'player_id': 'Tux', 'name': null, 'joined': false, 'score': 0, 'HP': 6, 'prev_spell': null, 'spells': [], 'secret_spells': [] 
    }, {
      'player_id': 'Teds', 'name': null, 'joined': false, 'score': 0, 'HP': 6, 'prev_spell': null, 'spells': [], 'secret_spells': [] 
    } ], 'active': false, 'current_player': undefined, 'round': 0, 'turn': 0, 'secret_warehouse': [], 'warehouse': [], 'ladder': [] 
  })
  const playingId = ref('Momo')
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
  return {
    gameStatus,
    playingId,
    playingIndex,
    setGameStatus,
    hoverMagic,
    setHoverMagic
  }
})