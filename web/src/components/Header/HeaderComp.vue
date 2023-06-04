<template>
  <header class="bg-pink-400 select-none">
    <div class="p-4 h-16 flex flex-row items-center content-center justify-evenly">
      <div class="h-12 w-12 items-center rounded-full outline-1">
        <button class="h-12 w-12 mx-3 items-center flex">
          <MenuIcon />
        </button>
      </div>
      <div>
        <h1 class="mx-4 font-semibold text-xl">Account</h1>
      </div>
      <div class="grow"></div>
      <div class="items-center">
        <img
          alt="Profile image"
          class="h-12 w-12 rounded-full shadow object-cover ring ring-pink-500 hover:ring-pink-300"
          src="src/assets/1.png"
        />
      </div>
    </div>
  </header>
</template>

<script setup>
import MenuIcon from 'vue-material-design-icons/Menu.vue'
</script>
