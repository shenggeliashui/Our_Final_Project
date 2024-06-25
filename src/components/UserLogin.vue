<template>
  <div class="login-container">
    <h2>登录</h2>
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <label for="username">用户名:</label>
        <input type="text" v-model="username" id="username"  required />
        <span v-if="errors.username" class="error-message">{{ errors.username }}</span>
      </div>
<!--      <div class="form-group">-->
<!--        <label for="email">电子邮件:</label>-->
<!--        <input type="email" v-model="email" id="email" required />-->
<!--        <span v-if="errors.email" class="error-message">{{ errors.email }}</span>-->
<!--      </div>-->
      <div class="form-group">
        <label for="password">密码:</label>
        <input type="password" v-model="password" id="password" required />
        <span v-if="errors.password" class="error-message">{{ errors.password }}</span>
      </div>
      <button type="submit">登录</button>
      <p>还没有账号？<router-link to="/register">注册</router-link></p>
    </form>
  </div>
</template>

<script>
import api from '../services/api';

export default {
  name: 'UserLogin',
  data() {
    return {
      username: '',
      password: '',
      errors: {}
    };
  },
  methods: {
    async handleLogin() {
      try {
        const response = await api.post('/api/login', {//backend
          username: this.username,
          password: this.password
        });

        console.log('登录成功:', response.data);
        // 假设后端返回的是 JWT 或其他会话令牌
        const token = response.data.token;
        // 存储令牌，比如存储在 localStorage 中
        localStorage.setItem('token', token);

         // 获取用户信息
        const userResponse = await api.get('/api/profile', {//backend
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        this.$store.commit('setUser', userResponse.data);
        // 登录成功后重定向到主页
        this.$router.push('/home');
      } catch (error) {
        console.error('登录失败:', error.response.data);
        // 处理后端返回的错误信息
        if (error.response.data.errors) {
          this.errors = error.response.data.errors;
        }
      }
    }
  }
};
</script>



<style scoped>
.login-container {
  max-width: 400px;
  margin: 100px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 15px;
}

form label {
  display: block;
  margin-bottom: 5px;
}

form input {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
}

button {
  width: 100%;
  padding: 10px;
  background-color: lightsalmon;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: coral;
}

p {
  margin-top: 15px;
  text-align: center;
}

.error-message {
  color: red;
  font-size: 0.9em;
}
</style>
