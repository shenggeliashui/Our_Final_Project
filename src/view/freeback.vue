<template>
  <div id="Frame">
    <PageHeader :userAvatarSrc="userAvatarSrcProp" :userName="'John Doe'" :logoSrc="logoSrcProp" />
    <div class="container">
      <div class="box">
        <form>
          <div class="form-group">
            <label for="name">姓名:</label>
            <input type="text" id="name" placeholder="请输入姓名">
          </div>
          <div class="form-group">
            <label for="email">邮箱:</label>
            <input type="email" id="email" placeholder="请输入邮箱">
          </div>
          <div class="form-group">
            <label for="feedback">反馈建议:</label>
            <textarea id="feedback" placeholder="请输入您的反馈建议"></textarea>
          </div>
          <button type="submit">提交</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import PageHeader from '../components/site_header.vue'
export default {
  name: 'Frame',
  components: {
    PageHeader
  },
  data () {
    return {
      userAvatarSrcProp: require('@/assets/photo1.png'),
      logoSrcProp: require('@/assets/logo1.png')
    }
  }
}
</script>

<style scoped>
html, body {
  height: 100%;
  margin: 0;
  padding: 0;
}

form {
  display: flex;
  flex-direction: column;
}

.form-group {
  display: flex;
  align-items: center;
  margin-bottom: 16px;
  width: 100%;
}

label {
  margin-right: 10px;
  font-weight: bold;
  color: #333;
  flex: 0 0 80px; /* 固定标签宽度 */
  text-align: left; /* 确保文本左对齐 */
}

input, textarea {
  flex: 1;
  padding: 10px;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 100%; /* 确保输入框占据剩余宽度 */
}

textarea {
  height: 100px; /* 设置文本域高度 */
}

button {
  padding: 8px 20px; /* 调整按钮的内边距 */
  font-size: 14px; /* 调整按钮的字体大小 */
  border: none;
  border-radius: 4px;
  background-color: #007BFF;
  color: white;
  cursor: pointer;
  width: 120px; /* 设置按钮的宽度 */
  margin: 0 auto; /* 将按钮居中 */
}

button:hover {
  background-color: #0056b3;
}
</style>
