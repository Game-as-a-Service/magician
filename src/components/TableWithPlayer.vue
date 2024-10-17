<script setup>
import { computed } from 'vue'
import TableDesk from '@/components/TableDesk.vue'
import { useGameStore } from '@/stores/game'
import imgSrcs from '@/models/Avatars.js'
const gameStore = useGameStore()
const playerClasses = [
  'player-green',
  'player-orange',
  'player-red',
  'player-yellow',
  'player-blue',
]
const players = computed(() =>
  gameStore.gameStatus.players.map((player, i) => ({
    name: player.player_id,
    hp: player.HP,
    score: player.score,
    holdStones: player.spells.length,
    imgSrc: imgSrcs[i],
    playerClass: playerClasses[i],
    attackable: attackable(i, gameStore.hoverMagic, gameStore.playingIndex),
    healable: healable(i, gameStore.hoverMagic, gameStore.playingIndex),
    isPlaying: i === gameStore.gameStatus.current_player,
  }))
)

const attackable = (playerIndex, magicNumber, playingIndex) => {
  if (magicNumber === 1 || magicNumber === 2) {
    return playerIndex !== playingIndex
  }
  if (magicNumber === 5) {
    return (
      playerIndex == (4 + playingIndex) % 5 ||
      playerIndex == (6 + playingIndex) % 5
    )
  }
  if (magicNumber === 6) {
    return playerIndex == (6 + playingIndex) % 5
  }
  if (magicNumber === 7) {
    return playerIndex == (4 + playingIndex) % 5
  }
}
const healable = (playerIndex, magicNumber, playingIndex) => {
  if (magicNumber === 2 || magicNumber === 3 || magicNumber === 8) {
    return playerIndex == playingIndex
  }
}
// function getImageUrl (name) {
//   const url = `/src/assets/images/avatar/${ name }.png`
//   return new URL(url, import.meta.url)
// }

// const players = [
//   {
//     name: 'Leave3310',
//     hp: 6,
//     imgSrc: getImageUrl('avatar_green'),
//     playerClass: 'player-green',
//   },
//   {
//     name: 'Yock',
//     hp: 6,
//     imgSrc: getImageUrl('avatar_yellow'),
//     playerClass: 'player-yellow',
//   },
//   {
//     name: 'Teds',
//     hp: 6,
//     imgSrc: getImageUrl('avatar_red'),
//     playerClass: 'player-red',
//   },
//   {
//     name: 'Cmomo',
//     hp: 6,
//     imgSrc: getImageUrl('avatar_orange'),
//     playerClass: 'player-orange',
//   },
//   {
//     name: 'Tux',
//     hp: 5,
//     imgSrc: getImageUrl('avatar_blue'),
//     playerClass: 'player-blue',
//   },
// ]
</script>

<template>
  <div class="w-[480px] h-[480px] relative flex justify-center items-center">
    <div
      v-for="player of players"
      :key="player.name"
      class="w-[100px] h-[100px] absolute hover-player"
      :class="player.playerClass"
    >
      <img :src="player.imgSrc">
      <div
        class="transition duration-500 ease-linear"
        :class="{ healable: player.healable,
                  attackable: player.attackable }"
      ></div>
      <div
        v-if="player.isPlaying"
        class="w-[80px] h-[100px] absolute top-3 -left-8 -rotate-[18deg]"
      >
        <img src="/src/assets/images/table/magicWand.svg">
      </div>
      <div
        v-if="player.isPlaying && gameStore.showFailAnimation"
        class="absolute -rotate-[18deg] spell-wrong"
      >
        <img src="/src/assets/images/sundries/smoke.png">
      </div>
      <div
        v-if="player.isPlaying && gameStore.showFailAnimation"
        class="absolute blood"
      >
        <img src="/src/assets/images/sundries/blood.png">
      </div>
      <div class="info-box absolute">
        <div class="bg-white info">
          <div class="block whitespace-nowrap">
            玩家：{{ player.name }}
          </div>
          <div>手牌數：{{ player.holdStones }}</div>
          <div>分數：{{ player.score }}</div>
        </div>
        <div
          class="info-box-triangle-left inline-block w-[30px] h-[20px]"
        ></div>
        <div
          class="info-box-triangle-right inline-block w-[30px] h-[20px]"
        ></div>
      </div>
    </div>
    <div
      v-for="item of players"
      :key="item.name"
      class="absolute"
      :class="`hp-${item.playerClass}`"
    >
      <div class="text-5xl font-bold">
        {{ item.hp }}
      </div>
    </div>
    <TableDesk></TableDesk>
  </div>
</template>

<style>
.attackable {
  position: absolute;
  top: 0;
  z-index: -1;
  width: 100px;
  height: 100px;
  filter: blur(5px);
  border: 13px solid #ff0000;
  border-radius: 100%;
  opacity: 1;
  transform: scale(1.2);
}

.healable {
  position: absolute;
  top: 0;
  z-index: -1;
  width: 100px;
  height: 100px;
  filter: blur(5px);
  border: 10px solid #fff;
  border-radius: 100%;
  opacity: 1;
  transform: scale(1.1);
}

.player-green {
  top: 295px;
  left: 60px;
}

.player-orange {
  top: 100px;
  left: 45px;
}

.player-red {
  top: 30px;
  left: 225px;
}

.player-yellow {
  top: 190px;
  left: 360px;
}

.player-blue {
  top: 345px;
  left: 245px;
}

.hp-player-green {
  top: calc(
    var(--center-y) + var(--length) * sin(72deg * 1 + var(--deg-angle))
  );
  left: calc(
    var(--center-x) + var(--length) * cos(72deg * 1 + var(--deg-angle))
  );
}

.hp-player-orange {
  top: calc(
    var(--center-y) + var(--length) * sin(72deg * 2 + var(--deg-angle))
  );
  left: calc(
    var(--center-x) + var(--length) * cos(72deg * 2 + var(--deg-angle))
  );
}

.hp-player-red {
  top: calc(
    var(--center-y) + var(--length) * sin(72deg * 3 + var(--deg-angle))
  );
  left: calc(
    var(--center-x) + var(--length) * cos(72deg * 3 + var(--deg-angle))
  );
}

.hp-player-yellow {
  top: calc(
    var(--center-y) + var(--length) * sin(72deg * 4 + var(--deg-angle))
  );
  left: calc(
    var(--center-x) + var(--length) * cos(72deg * 4 + var(--deg-angle))
  );
}

.hp-player-blue {
  top: calc(
    var(--center-y) + var(--length) * sin(72deg * 0 + var(--deg-angle))
  );
  left: calc(
    var(--center-x) + var(--length) * cos(72deg * 0 + var(--deg-angle))
  );
}

.info-box {
  top: 0px;
  z-index: 200;
  display: block;
  padding: 5px 10px;
  opacity: 0;
  transition: all .3s;
}

.hover-player:hover .info-box {
  top: -100px;
  z-index: 200;
  display: block;
  opacity: .9;
}

.info {
  min-width: 140px;
  padding: 10px;
  border-radius: 5px;
  box-shadow: 2px 0px 5px rgba(0, 0, 0, .3);
}

.info-box-triangle-left,
.info-box-triangle-right {
  overflow: hidden;
}

.info-box-triangle-left::before {
  content: '';
  display: block;
  width: 60px;
  height: 40px;
  border-radius: 50%;
  box-shadow: 20px -10px 0px #fbfbfb;
  transform: translateX(-50%);
}

.info-box-triangle-right::before {
  content: '';
  display: block;
  width: 60px;
  height: 40px;
  border-radius: 50%;
  box-shadow: -20px -10px 0px #fbfbfb;
}

:root {
  --deg-angle: 69deg;
  --length: 90px;
  --center-x: 227px;
  --center-y: 215px;
}

/* 播放失敗動畫要調整時長時要記得調整 stores/game.js 的 showFailAnimation 時長 */
.spell-wrong {
  top: 45px;
  left: -20px;
  animation: animate-smoke 1.5s 1 ease-in-out forwards;
}

.blood {
  top: 60px;
  left: 20px;
  animation: animate-blood 1.5s infinite ease-in-out forwards;
}

@keyframes animate-smoke {
  0% {
    width: 40px;
    height: 40px;
    opacity: 0;
    transform: translate(0px, 0px);
  }

  50% {
    width: 80px;
    height: 100px;
    opacity: 1;
    transform: translate(-30px, -40px);
  }

  100% {
    width: 120px;
    height: 150px;
    opacity: 0;
    transform: translate(-50px, -60px);
  }
}

@keyframes animate-blood {
  0% {
    width: 15px;
    height: 20px;
    opacity: 0;
    transform: translate(18px, 8px);
  }

  50% {
    width: 20px;
    height: 30px;
    opacity: 1;
    transform: translate(15px, 40px);
  }

  100% {
    width: 25px;
    height: 35px;
    opacity: 0;
    transform: translate(15px, 50px);
  }
}
</style>