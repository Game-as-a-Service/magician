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
  const gameOver = computed(() => {
    return gameStatus.value.players.some((player) => player.score >= 8)
  })
  const setGameStatus = (status) => {
    // 把訊息放到廣播區
    gameStatus.value = status
    messages.value.push(status.action_message)
    // if (status.action_message.includes('成功')){
    //   const number = status.action_message.split(' ')[3]
    //   if (gameStatus.value.players[gameStatus.value.current_player].player_id !== playingId.value){
    //     playMagicVideo(Number(number))
    //   }
    // }
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
  const showVideo = ref(false)
  const showFailAnimation = ref(false)
  const videoNumber = ref(0)
  const messages = ref([])
  const gameStatusQueue = ref([])
  const enqueueGameStatus = (status) => {
    gameStatusQueue.value.push(status)
  }
  const dequeueGameStatus = () => {
    return gameStatusQueue.value.shift()
  }
  const updateShowSecretTable = (value) => (showSecretTable.value = value)
  const updateTmpGameStatus = (value) => (tmpGameStatus.value = value)
  const restoreGameStatus = () => setGameStatus(tmpGameStatus.value)
  const playMagicVideo = (n) => {
    videoNumber.value = n
    showVideo.value = true
  }
  const playFailAnimation = () => {
    showFailAnimation.value = true
    setTimeout(() => {
      showFailAnimation.value = false
      processing.value = false
      restoreGameStatus()
      processGameStatus()
    }, 1500)
  }
  const afterAction = ref(false) 
  const diceNumber = ref(0)
  const showDice = ref(false)
  const setPlayDice = (number) => {
    diceNumber.value = number
    console.log('diceNumber: ', diceNumber.value)
  }
  const setShowDice = (value) => showDice.value = value
  const processing = ref(false)
  const processGameStatus = () => {
    if (gameStatusQueue.value.length > 0) {
      const status = dequeueGameStatus()
      console.log('processGameStatus: ', status.action_message)
      processing.value = true
      // if (status.event_name === 'spell_success') {
      //   const number = status.spell_cast_number
      //   if (number == 1 || number == 3){
      //     // dice_result
      //     // event_name: "spell_success" // 施法成功
      //     // event_name: "spell_fail" // 施法失敗
      //     // event_name: "dice_rolled" // 擲骰子
      //     // setPlayDice(newGameStatus.dice_result)
      //   }
      // } else 
      
      if (status.event_name === 'spell_success'){
        const number = status.spell_cast_number
        // if (status.players[status.current_player].player_id !== playingId.value){
        playMagicVideo(Number(number))
        updateTmpGameStatus(status)
        
        // } else {
        //   processing.value = false
        //   setGameStatus(status)
        //   processGameStatus()
        // }
      } else if (status.event_name === 'spelled_fail') {
        updateTmpGameStatus(status)
        playFailAnimation()
      } else if (status.event_name === 'dice_rolled') {
        console.log('dice_rolled: ', status.dice_result)
        setPlayDice(status.dice_result)
        setShowDice(true)
        updateTmpGameStatus(status)
      } else if (status.event_name === 'spell_owl') {
        console.log('select secret')
        updateTmpGameStatus(status)
        if (myTurn.value){
          updateShowSecretTable(true)
        }
      } else {
        setGameStatus(status)
        processing.value = false
        processGameStatus()
      }
    }
  }
  const videoEnded = () => {
    showVideo.value = false
    processing.value = false
    restoreGameStatus()
    processGameStatus()

    // if (videoNumber.value == 1 || gameStore.videoNumber == 3){
    //   gameStore.setShowDice(true)
    // }
  }
  const diceEnded = () => {
    setShowDice(false)
    processing.value = false
    
    restoreGameStatus()
    processGameStatus()
  }
  const selectSecretEnded = () => {
    updateShowSecretTable(false)
    processing.value = false
    restoreGameStatus()
    processGameStatus()
  }
  return {
    gameStatus,
    gameOver,
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
    showVideo,
    showFailAnimation,
    videoNumber,
    playMagicVideo,
    messages,
    afterAction,
    diceNumber,
    showDice,
    setShowDice,
    setPlayDice,
    gameStatusQueue,
    enqueueGameStatus,
    dequeueGameStatus,
    processGameStatus,
    videoEnded,
    processing,
    diceEnded,
    selectSecretEnded,
  }
})