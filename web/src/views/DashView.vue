<script setup>
import { ref } from 'vue'
import HeaderComp from '@/components/Header/HeaderComp.vue'
import FooterComp from '@/components/Footer/FooterComp.vue'

const showBox = ref(false)
const animationClass = ref('')

const toggleBox = () => {
  showBox.value = !showBox.value
  animationClass.value = showBox.value ? 'animate__fadeIn' : 'animate__fadeOut'
}
</script>

<template>
  <HeaderComp />
  <div class="animate__animated animate__fadeIn">
    <button @click="toggleBox">Toggle Box</button>
    <div v-if="showBox" :class="animationClass" class="animate__animated">
      <h1>Hello World!</h1>
    </div>
  </div>

  <FooterComp />
</template>

<style scoped></style>
