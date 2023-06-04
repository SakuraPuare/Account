<script setup>
import { computed, ref } from 'vue'

const username = ref('SakuraPuare')
const email = ref('java20131114@gmail.com')
const password = ref('1234567qwertyuio')
const slogan = ref('114514意义是')
const captcha = ref('12345678')

const animationType = ref('')

const RegisterState = ref(0)

const handleRegister = () => {
  nextStep()
  console.log('Register')
}

const handelCaptcha = () => {
  nextStep()
  console.log('Captcha')
}

const handelResend = () => {}

// function string2int(str) {
//   return Boolean(str) ? 1 : 0
// }

const verifyCaptcha = computed(() => {
  function sendVerifyCaptchaRequest(str) {
    return true
  }

  console.log(
    captcha.value,
    String(captcha.value).length === 8,
    sendVerifyCaptchaRequest(captcha.value)
  )
  return String(captcha.value).length === 8 && sendVerifyCaptchaRequest(captcha.value)
})

const nextStep = () => {
  function verifyEmail(str) {
    const re = /\S+@\S+\.\S+/
    return re.test(str)
  }

  // verify email
  if (RegisterState.value === 6) return RegisterState.value
  else if (RegisterState.value === 0 && !verifyEmail(email.value)) {
    alert('邮箱格式不正确')
  } else if (RegisterState.value === 1 && password.value.length <= 8) {
    alert('密码长度小于8位')
  } else if (RegisterState.value === 2 && !Boolean(username.value)) {
    alert('请填写用户名')
  } else {
    // animation
    animationType.value = 'animate__slideOutLeft'
    setTimeout(() => {
      RegisterState.value++
      animationType.value = 'animate__slideInRight'
    }, 600)

    console.log(RegisterState.value)
  }

  return RegisterState.value
}

const prevStep = () => {
  // animation
  animationType.value = 'animate__slideOutRight'
  setTimeout(() => {
    RegisterState.value--
    animationType.value = 'animate__slideInLeft'
  }, 600)

  console.log(RegisterState.value)

  return RegisterState.value
}

// show the password complexity
const passwordComplexity = computed(() => {
  let complexity = 0
  if (password.value.match(/[a-z]/)) complexity++
  if (password.value.match(/[A-Z]/)) complexity++
  if (password.value.match(/[0-9]/)) complexity++
  if (password.value.match(/[+.$@$!%*#?&]/)) complexity++

  return complexity
})

const calcPasswordColor = computed(() => {
  switch (passwordComplexity.value) {
    case 1:
      return 'bg-red-400'
    case 2:
      return 'bg-yellow-400'
    case 3:
      return 'bg-green-400'
    case 4:
      return 'bg-blue-400'
  }
})
</script>

<template>
  <div class="flex flex-row select-none h-screen animate__animated animate__fadeIn">
    <div class="grow"></div>

    <div class="m-auto h-4/5 w-6/12 min-h-[70%] min-w-[30%]">
      <div
        class="h-full rounded-xl outline outline-pink-500/50 outline-2 overflow-hidden text-center"
      >
        <div class="flex flex-col justify-center items-center h-full">
          <div class="pt-16 text-3xl font-normal">注册 ShuYing Account</div>

          <div
            :class="animationType"
            class="flex flex-col justify-center items-center h-full w-full text-xl font-bold animate__animated"
          >
            <div class="w-full my-10">
              <div v-if="RegisterState === 0">
                <p>首先，我们需要知道你的邮箱</p>
              </div>
              <div v-else-if="RegisterState === 1">
                <p class="text-sm mb-2">{{ email }}</p>
                <p>看起来好极了，不过你还需要一个密码</p>
              </div>
              <div v-else-if="RegisterState === 2"><p>非常好，请问我们怎么称呼你？</p></div>
              <div v-else-if="RegisterState === 3">
                <p class="text-sm mb-2">{{ username }} 你好！</p>
                <p>能用一句话介绍一下自己吗？</p>
              </div>
              <div v-else-if="RegisterState === 4" class="flex flex-col text-base space-y-2">
                <p class="text-xl">来看看你给我们的信息</p>
                <p>
                  用户名：<span class="font-mono">{{ username }}</span>
                </p>
                <p>
                  邮箱：<span class="font-mono">{{ email }}</span>
                </p>
                <p v-if="slogan">
                  个人介绍：<span class="font-mono">{{ slogan }}</span>
                </p>
              </div>

              <div v-else-if="RegisterState === 5">
                <p>就快要完成了！</p>
                <p class="text-sm my-2">我们向 {{ email }} 发送了一封验证码</p>
              </div>

              <div v-else-if="RegisterState === 6" class="flex flex-col space-y-5">
                <p>恭喜！你已注册完成！</p>
                <p class="text-base">
                  <RouterLink to="/login">现在登录</RouterLink>
                </p>
              </div>
            </div>

            <div class="w-full text-base font-normal">
              <form v-if="RegisterState < 5" class="w-2/3 m-auto" @submit.prevent="handleRegister">
                <input
                  v-if="RegisterState === 0"
                  v-model.trim="email"
                  class="px-4 py-3 border border-gray-300 rounded-md w-full"
                  placeholder="邮箱"
                  required
                  type="email"
                />
                <input
                  v-if="RegisterState === 1"
                  v-model.trim="password"
                  class="px-4 py-3 border border-gray-300 rounded-md w-full"
                  placeholder="密码"
                  required
                  type="password"
                />

                <div v-if="RegisterState === 1" class="my-5">
                  <div
                    v-if="passwordComplexity > 0"
                    class="h-1 w-full bg-gray-200 rounded-full overflow-hidden"
                  >
                    <div
                      :class="calcPasswordColor"
                      :style="{ width: passwordComplexity * 25 + '%' }"
                      class="h-full rounded-full"
                    ></div>
                  </div>

                  <div class="text-left text-sm py-2">
                    <div v-if="passwordComplexity === 1" class="text-red-400">密码太简单了哦~</div>
                    <div v-else-if="passwordComplexity === 2" class="text-yellow-400">
                      我觉得还行！
                    </div>
                    <div v-else-if="passwordComplexity === 3" class="text-green-400">
                      已经差不多可以了
                    </div>
                    <div v-else-if="passwordComplexity >= 4" class="text-blue-400">
                      真棒~密码很强哦~
                    </div>
                  </div>
                </div>

                <input
                  v-if="RegisterState === 2"
                  v-model.trim="username"
                  class="px-4 py-3 border border-gray-300 rounded-md w-full"
                  placeholder="用户名"
                  required
                  type="text"
                />

                <input
                  v-if="RegisterState === 3"
                  v-model.trim="slogan"
                  class="px-4 py-3 border border-gray-300 rounded-md w-full"
                  placeholder="个人介绍（可选）"
                  type="text"
                />

                <button
                  v-if="RegisterState === 4"
                  class="px-6 py-2.5 w-1/3 mx-auto text-white bg-pink-400 active:bg-pink-600 rounded-md"
                  type="submit"
                >
                  注册
                </button>
              </form>

              <form
                v-else-if="RegisterState === 5"
                class="flex flex-col space-y-4 w-2/3 m-auto"
                @submit.prevent="handelCaptcha"
              >
                <input
                  v-model.number="captcha"
                  class="px-4 py-3 border border-gray-300 rounded-md w-full text-center"
                  maxlength="8"
                  minlength="8"
                  oninput="this.value = String(this.value.replace(/[^0-9]/g, ''))"
                  placeholder="验证码"
                  required
                  type="text"
                />

                <div v-if="captcha && !verifyCaptcha" class="text-red-500">验证码错误</div>

                <div class="py-5 flex flex-row items-center text-center">
                  <div class="text-sm text-gray-500 active:text-black" onclick="handelResend">
                    没有收到？
                  </div>
                  <div class="grow"></div>
                  <button
                    class="px-6 py-2.5 w-1/3 mx-auto text-white bg-pink-400 active:bg-pink-600 rounded-md"
                    type="submit"
                  >
                    提交
                  </button>
                </div>
              </form>
            </div>

            <div class="w-full"></div>
          </div>

          <div class="py-12 flex flex-row space-x-20">
            <button
              v-if="RegisterState > 0 && RegisterState < 4"
              class="px-6 py-2.5 text-white bg-pink-400 active:bg-pink-600 rounded-md"
              v-on:click="prevStep()"
            >
              上一步
            </button>
            <button
              v-if="RegisterState < 4"
              class="px-6 py-2.5 text-white bg-pink-400 active:bg-pink-600 rounded-md"
              v-on:click="nextStep()"
            >
              下一步
            </button>
          </div>
        </div>
      </div>

      <div class="flex flex-row w-full space-x-8 py-4 text-sm text-pink-500">
        <a href="">需要帮助？</a>
        <div class="grow"></div>
        <a href="">隐私协议</a>
        <a href="">服务条款</a>
      </div>
    </div>
    <div class="grow"></div>
  </div>
</template>

<style scoped></style>
