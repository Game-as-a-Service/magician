import { defineStore } from 'pinia'
import {
  ref, computed 
} from 'vue'
export const useGameStore = defineStore('useGameStore', () => {
  const gameStatus = ref({
    game_id: '',
    players: [
      {
        player_id: 'Leave3310',
        name: null,
        joined: false,
        score: 0,
        HP: 6,
        prev_spell: null,
        spells: [],
        secret_spells: [],
      },
      {
        player_id: 'Momo',
        name: null,
        joined: false,
        score: 0,
        HP: 6,
        prev_spell: null,
        spells: [],
        secret_spells: [ 'Magic6 ' ],
      },
      {
        player_id: 'Yock',
        name: null,
        joined: false,
        score: 0,
        HP: 6,
        prev_spell: null,
        spells: [],
        secret_spells: [ 'Magic 3', 'Magic 4' ],
      },
      {
        player_id: 'Tux',
        name: null,
        joined: false,
        score: 0,
        HP: 6,
        prev_spell: null,
        spells: [],
        secret_spells: [ 'Magic 1', 'Magic 4' ],
      },
      {
        player_id: 'Teds',
        name: null,
        joined: false,
        score: 0,
        HP: 6,
        prev_spell: null,
        spells: [],
        secret_spells: [],
      },
    ],
    active: false,
    current_player: undefined,
    round: 0,
    turn: 0,
    secret_warehouse: [ 0, 0, 0, 0 ],
    warehouse: [],
    ladder: [],
  })

  const tmpGameStatus = ref(null)
  const playingId = ref('')
  const playingIndex = computed(() => {
    return gameStatus.value.players.findIndex(
      (player) => player.player_id === playingId.value
    )
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
    return (
      gameStatus.value.players[gameStatus.value.current_player].player_id ===
      playingId.value
    )
  })
  const spellCountDownTimer = ref(30)
  const secretCountDownTimer = ref(20)
  const showSecretTable = ref(false)

  const updateShowSecretTable = (value) => (showSecretTable.value = value)
  const updateTmpGameStatus = (value) => (tmpGameStatus.value = value)
  const restoreGameStatus = () => setGameStatus(tmpGameStatus.value)

  return {
    gameStatus,
    playingId,
    playingIndex,
    setGameStatus,
    tmpGameStatus,
    hoverMagic,
    setHoverMagic,
    myTurn,
    spellCountDownTimer,
    secretCountDownTimer,
    showSecretTable,
    updateShowSecretTable,
    updateTmpGameStatus,
    restoreGameStatus,
  }
})