<template>
  <header class="site-header" aria-label="网站头部">
    <div class="logo">
      <img :src="logoSrc" >
    </div>
    <div class="user-info" aria-label="用户信息">
        <button class="sign-out-button">个人中心</button>
        <button @click="navigateToYourRoute" class="sign-out-button">反馈</button>
        <button class="sign-out-button">Sign Out</button>
      <div class="user-avatar">
        <img :src="userAvatarSrc" :alt="altText">
      </div>
      <div class="user-name">
        {{ userName }}
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'PageHeader',
  props: {
    logoSrc: {
      type: String,
      required: true
    },
    userAvatarSrc: {
      type: String,
      required: true
    },
    userName: {
      type: String,
      required: true
    }
  },
  computed: {
    altText () {
      return this.userName + '的' + (this.logoSrc.includes('.png') ? '公司标志' : '用户头像')
    }
  },
  methods: {
    navigateToYourRoute () {
      this.$router.push('/freeback')
    }
  }
}
</script>

<style scoped>
.site-header {
  background-color: #f4f4f4;
  padding: 5px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 70px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 可选的阴影效果 */
}

.logo img {
  height: 50px; /* 根据需要调整 logo 的高度 */
}

.user-info {
  display: flex;
  align-items: center;
}

.user-avatar img {
  width: 50px; /* 调整用户头像的尺寸 */
  height: 50px;
  border-radius: 50%; /* 让头像呈现圆形 */
  margin-right: 10px;
}

.user-name {
  font-weight: bold;
}

.sign-out-button {
  background-color: transparent; /* 背景透明 */
  color: black; /* 文字颜色为黑色 */
  border: 2px solid black; /* 边框为黑色，宽度为2px */
  padding: 8px 15px;
  border-radius: 5px;
  margin-right: 20px;
  cursor: pointer;
}

.sign-out-button:hover {
  background-color: rgba(88, 84, 84, 0.1); /* 悬停时背景颜色稍微变暗 */
}

/* 响应式设计 */
@media (max-width: 600px) {
  .site-header {
    flex-direction: column;
    align-items: flex-start;
  }
  .user-info {
    margin-top: 10px;
  }
}

</style>
