<script setup>
import { ref } from 'vue'

const email = ref('')
const password = ref('')

const handleLogin = () => {
  console.log('login')
}
</script>

<template>
  <div class="flex flex-col h-screen animate__animated animate__fadeIn">
    <div class="flex flex-col h-full">
      <div
        class="m-auto rounded-xl outline outline-pink-500/50 outline-2 h-4/5 w-6/12 min-h-[70%] min-w-[30%]"
      >
        <div class="flex flex-col text-center h-full">
          <div class="my-auto">
            <div class="">
              <h1 class="text-3xl font-normal py-4">登录</h1>
              <p>登录到您的 ShuYing Account</p>
            </div>

            <form @submit.prevent="handleLogin">
              <div class="py-12 mx-auto flex flex-col space-y-6 w-2/3">
                <input
                  v-model.trim="email"
                  class="px-4 py-3 border border-gray-300 rounded-md"
                  placeholder="邮箱"
                  required
                  type="email"
                />
                <input
                  v-model="password"
                  class="px-4 py-3 border border-gray-300 rounded-md"
                  placeholder="密码"
                  required
                  type="password"
                />
              </div>
              <div class="flex flex-row mx-auto w-2/3 text-center items-center">
                <a class="text-sm text-pink-500" href="">恢复账号</a>
                <div class="grow"></div>
                <button
                  class="px-6 py-2.5 text-white bg-pink-400 active:bg-pink-600 rounded-md"
                  type="submit"
                >
                  登录
                </button>
              </div>
            </form>

            <div class="py-8">
              没有账号？
              <RouterLink class="text-pink-600" to="/register">点此注册</RouterLink>
            </div>
          </div>
        </div>

        <div class="flex flex-row w-full space-x-8 py-4">
          <a class="text-sm text-pink-500" href="">需要帮助？</a>
          <div class="grow"></div>
          <a class="text-sm text-pink-500" href="">隐私协议</a>
          <a class="text-sm text-pink-500" href="">服务条款</a>
        </div>
      </div>
    </div>
    <!-- <FooterComp /> -->
  </div>
</template>

<style scoped></style>
