<script setup>
import {
  ref, onMounted
} from 'vue'
import { useGameStore } from '@/stores/game'
const gameStore = useGameStore()
const diceValue = ref(0)
onMounted(() => {
  setTimeout(() => {
    diceValue.value = gameStore.diceNumber
  }, 500)
  setTimeout(() => {
    gameStore.setShowDice(false)
    diceValue.value = 0
  }, 3000)
})
</script>

<template>
  <div
    class="dice"
  >
    <input
      id="dice"
      type="checkbox"
    >
    <label for="dice">
      <div
        class="box"
        :class="{ 'dice1': diceValue === 1,
                  'dice2': diceValue === 2,
                  'dice3': diceValue === 3 }"
      >
        <div class="box1"></div>
        <div class="box2"></div>
        <div class="box3"></div>
        <div class="box4"></div>
        <div class="box5"></div>
        <div class="box6"></div>
      </div>
    </label>
  </div>
</template>

<style>
.box {
  width: 100px;
  height: 100px;
  margin: 50px auto;
  /* animation: rotate 6s infinite linear; */
  /* animation: 6s linear; */
  transition: all 2s cubic-bezier(0, 0, 0, 1);
  transform: rotateX(3000deg) rotateY(3000deg) rotateZ(3000deg);
  transform-style: preserve-3d;
}

.box > div {
  position: absolute;
  width: 100px;
  height: 100px;
  /* background-image: url("https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6c0f759864249a39416e3a53e2408f0~tplv-k3u1fbpfcp-watermark.image?"); */
  background-image: url('/src/assets/images/sundries/dice.png');
  background-repeat: no-repeat;
  background-size: cover;
  /* background-color: red; */
  border-radius: 8px;
}

.dice1 {
  transform: rotateX(-50deg) rotateY(calc(50deg + 3600deg)) rotateZ(90deg);
}

.dice2 {
  transform: rotateX(calc(-50deg + 3600deg)) rotateY(50deg) rotateZ(180deg);
}

.dice3 {
  transform: rotateX(40deg) rotateY(0deg) rotateZ(calc(130deg + 3600deg));
}

.box1 {
  background-position: 0 0;
  transform: rotateY(90deg) translateZ(50px);
}

.box2 {
  background-position: -600px 0;
  transform: rotateY(-90deg) translateZ(50px);
}

.box3 {
  background-position: -400px 0;
  transform: rotateX(90deg) translateZ(50px);
}

.box4 {
  background-position: -400px 0;
  transform: rotateX(-90deg) translateZ(50px);
}

.box5 {
  background-position: -800px 0;
  transform: rotateZ(90deg) translateZ(50px);
}

.box6 {
  background-position: -800px 0;
  transform: rotateZ(0) translateZ(-50px);
}

#dice:checked + label .box {
  animation-play-state: paused;
}

#dice {
  display: none;
}

.dice {
  position: absolute;
  top: 430px;
  left: 535px;
  z-index: 100;
  animation: animate-drop 2s infinite linear;
}

@keyframes animate-drop {
  0% {
    translate: 200% -300%;
  }
  10%{
    translate: 180% -240%;
  }
  20%{
    translate: 160% -150%;
  }
  30%{
    translate: 140% -80%;
  }
  40%{
    translate: 120% 0%;
  }
  50%{
    translate: 100% -40%;
  }
  60%{
    translate: 80% -50%;
  }
  70%{
    translate: 60% -40%;
  }
  80%{
    translate: 40% 0;
  }
  90%{
    translate: 20% -20%;
  }
  100% {
    translate: 0% 0;
  }
}



</style>