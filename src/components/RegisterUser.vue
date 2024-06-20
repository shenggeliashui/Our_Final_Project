<template>
  <div class="register-container">
    <h2>注册</h2>
    <form @submit.prevent="handleRegister">
      <div class="form-group">
        <label for="username">用户名:</label>
        <input type="text" v-model="username" id="username" @blur="validateUsername" required />
        <span v-if="errors.username" class="error-message">{{ errors.username }}</span>
      </div>
      <div class="form-group">
        <label for="email">电子邮件:</label>
        <input type="email" v-model="email" id="email" @blur="validateEmail" required />
        <span v-if="errors.email" class="error-message">{{ errors.email }}</span>
      </div>
      <div class="form-group">
        <label for="password">密码:</label>
        <input type="password" v-model="password" id="password" @blur="validatePassword" required />
        <span v-if="errors.password" class="error-message">{{ errors.password }}</span>
      </div>
      <div class="form-group">
        <label for="confirmPassword">确认密码:</label>
        <input type="password" v-model="confirmPassword" id="confirmPassword" @blur="validateConfirmPassword" required />
        <span v-if="errors.confirmPassword" class="error-message">{{ errors.confirmPassword }}</span>
      </div>
      <button type="submit">注册</button>
    </form>
  </div>
</template>

<script>
import api from '../services/api';

export default {
  name: 'RegisterUser',
  data() {
    return {
      username: '',
      email: '',
      password: '',
      confirmPassword: '',
      errors: {}
    };
  },
  methods: {
    validateUsername() {
      if (!this.username) {
        this.errors.username = '用户名不能为空';
      } else {
        delete this.errors.username;
      }
    },
    validateEmail() {
      const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
      if (!this.email) {
        this.errors.email = '电子邮件不能为空';
      } else if (!emailPattern.test(this.email)) {
        this.errors.email = '电子邮件格式不正确';
      } else {
        delete this.errors.email;
      }
    },
    validatePassword() {
      if (!this.password) {
        this.errors.password = '密码不能为空';
      } else if (this.password.length < 6) {
        this.errors.password = '密码长度不能少于6位';
      } else {
        delete this.errors.password;
      }
    },
    validateConfirmPassword() {
      if (!this.confirmPassword) {
        this.errors.confirmPassword = '请确认密码';
      } else if (this.confirmPassword !== this.password) {
        this.errors.confirmPassword = '密码不匹配';
      } else {
        delete this.errors.confirmPassword;
      }
    },
    async handleRegister() {
      this.validateUsername();
      this.validateEmail();
      this.validatePassword();
      this.validateConfirmPassword();

      if (Object.keys(this.errors).length === 0) {
        try {
          const response = await api.post('/register', {
            username: this.username,
            email: this.email,
            password: this.password
          });

          console.log('注册成功:', response.data);
          // 注册成功后重定向到登录页面
          this.$router.push('/');
        } catch (error) {
          console.error('注册失败:', error.response.data);
          // 处理后端返回的错误信息
          if (error.response.data.errors) {
            this.errors = error.response.data.errors;
          }
        }
      }
    }
  }
};
</script>

<!--<script>-->
<!--export default {-->
<!--  name: 'RegisterUser',-->
<!--  data() {-->
<!--    return {-->
<!--      username: '',-->
<!--      email: '',-->
<!--      password: '',-->
<!--      confirmPassword: '',-->
<!--      errors: {}-->
<!--    };-->
<!--  },-->
<!--  methods: {-->
<!--    validateUsername() {-->
<!--      if (!this.username) {-->
<!--        this.errors.username = '用户名不能为空';-->
<!--      } else {-->
<!--        delete this.errors.username;-->
<!--      }-->
<!--    },-->
<!--    validateEmail() {-->
<!--      const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;-->
<!--      if (!this.email) {-->
<!--        this.errors.email = '电子邮件不能为空';-->
<!--      } else if (!emailPattern.test(this.email)) {-->
<!--        this.errors.email = '电子邮件格式不正确';-->
<!--      } else {-->
<!--        delete this.errors.email;-->
<!--      }-->
<!--    },-->
<!--    validatePassword() {-->
<!--      if (!this.password) {-->
<!--        this.errors.password = '密码不能为空';-->
<!--      } else if (this.password.length < 6) {-->
<!--        this.errors.password = '密码长度不能少于6位';-->
<!--      } else {-->
<!--        delete this.errors.password;-->
<!--      }-->
<!--    },-->
<!--    validateConfirmPassword() {-->
<!--      if (!this.confirmPassword) {-->
<!--        this.errors.confirmPassword = '请确认密码';-->
<!--      } else if (this.confirmPassword !== this.password) {-->
<!--        this.errors.confirmPassword = '密码不匹配';-->
<!--      } else {-->
<!--        delete this.errors.confirmPassword;-->
<!--      }-->
<!--    },-->
<!--    handleRegister() {-->
<!--      this.validateUsername();-->
<!--      this.validateEmail();-->
<!--      this.validatePassword();-->
<!--      this.validateConfirmPassword();-->

<!--      if (Object.keys(this.errors).length === 0) {-->
<!--        // 在这里处理注册逻辑，比如发送请求到服务器创建新用户-->
<!--        console.log('Username:', this.username);-->
<!--        console.log('Email:', this.email);-->
<!--        console.log('Password:', this.password);-->
<!--        // 假设注册成功，重定向到登录页面-->
<!--        this.$router.push('/');-->
<!--      }-->
<!--    }-->
<!--  }-->
<!--};-->
<!--</script>-->

<!--<script>-->
<!--export default {-->
<!--  name: 'RegisterUser',-->
<!--  data() {-->
<!--    return {-->
<!--      username: '',-->
<!--      email: '',-->
<!--      password: '',-->
<!--      confirmPassword: ''-->
<!--    };-->
<!--  },-->
<!--  methods: {-->
<!--    handleRegister() {-->
<!--      if (this.password !== this.confirmPassword) {-->
<!--        alert('密码不匹配');-->
<!--        return;-->
<!--      }-->
<!--      // 在这里处理注册逻辑，比如发送请求到服务器创建新用户-->
<!--      console.log('Username:', this.username);-->
<!--      console.log('Email:', this.email);-->
<!--      console.log('Password:', this.password);-->
<!--      // 假设注册成功，重定向到登录页面-->
<!--      this.$router.push('/');-->
<!--    }-->
<!--  }-->
<!--};-->
<!--</script>-->

<style scoped>
.register-container {
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

.error-message {
  color: red;
  font-size: 0.9em;
}
</style>
