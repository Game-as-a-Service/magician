import { defineStore } from 'pinia'
import { ref } from 'vue'
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
  const playingId = ref('')
  const setGameStatus = (status) => {
    gameStatus.value = status
  }
  return {
    gameStatus,
    playingId,
    setGameStatus
  }
})