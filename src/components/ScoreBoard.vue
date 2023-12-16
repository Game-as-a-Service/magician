<script setup>
function getImageUrl (name) {
  const url = `/src/assets/images/avatar/${ name }.png`
  return new URL(url, import.meta.url)
}

const players = [
  {
    name: 'Leave3310',
    score: 0,
    imgSrc: getImageUrl('avatar_green'),
  },
  {
    name: 'Cmomo',
    score: 1,
    imgSrc: getImageUrl('avatar_orange'),
  },
  {
    name: 'Teds',
    score: 2,
    imgSrc: getImageUrl('avatar_red'),
  },
  {
    name: 'Yock',
    score: 3,
    imgSrc: getImageUrl('avatar_yellow'),
  },
  {
    name: 'Tux',
    score: 4,
    imgSrc: getImageUrl('avatar_blue')
  },
]
</script>

<template>
  <div class=" bg-grey50 p-[12px] inline-block">
    <div
      v-for="item of players"
      :key="item.name"
      class="flex items-center"
    >
      <div class="w-[30px] h-[40px] mr-[8px] py-[5px]">
        <img :src="item.imgSrc">
      </div>
      <h6 class="flex items-center">
        <div class="truncate w-[110px]">
          {{ item.name }}
        </div>
        : {{ item.score }}分
      </h6>
    </div>
  </div>
</template>