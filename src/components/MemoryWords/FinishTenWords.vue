<template>
  <div id="FinishTenWords">
    <main>
      <div class="outer-box">
        <div class="left-section"></div>
        <!-- 打印已背单词数/未背单词数/总单词数-->
        <div class="content-box">
          <div class="chinese">
            <h1>你已经背完10个新单词</h1>
            <h1>真是太棒啦！！！</h1>
          </div>
          <!--设置跳转链接-->
          <div class="buttons">
            <button @click="ContinueButton">再背十个</button>
            <button @click="QuitButton">回到首页</button>
          </div>
        </div>
        <div class="right-section"></div>
      </div>
    </main>
    <router-view />
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'FinishTenWords',
  data() {
    return {
      unmemoriedNum: null,
      memoriedNum: null
    };
  },
  mounted() {
    this.getUnmemoriedNum();
    this.getMemoriedNum();
  },
  methods: {
    ContinueButton() {
      this.$router.push({
        name: 'MemoryTenWords'
      });
    },
    QuitButton() {
      this.$router.push({
        name: 'HomePage'
      });
    },
    async getMemoriedNum() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/get-memorized-num');
        this.memoriedNum = response.data.number;
      } catch (error) {
        console.error('Error calling greet API:', error);
      }
    },
    async getUnmemoriedNum() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/get-unmemorized-num');
        this.unmemoriedNum = response.data.number;
      } catch (error) {
        console.error('Error calling greet API:', error);
      }
    }
  }
}
</script>

<style>
/* 页面整体样式 */
#FinishTenWords {
  font-family: Arial, sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 100vh;
}

main {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  width: 100%;
  height: 100%;
}

.outer-box {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 80%; /* 设置适合的宽度 */
  background-color: #f9f3ea; /* 浅橙色背景 */
  padding: 20px; /* 外部填充 */
  border: 2px solid #ffa500; /* 橙色边框 */
  border-radius: 10px; /* 圆角 */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* 阴影 */
}

.left-section,
.right-section {
  width: 20%; /* 左右各占20% */
  height: 100%; /* 高度与外部框一致 */
}

.left-section {
  background-image: url('../../assets/homepage_bg_left.png'); /* 左侧背景图片 */
  background-size: cover;
  background-position: center;
}

.right-section {
  background-image: url('../../assets/homepage_bg_left.png'); /* 右侧背景图片 */
  background-size: cover;
  background-position: center;
  
} 

.content-box {
  width: 60%; /* 设置内容框的宽度为60% */
  max-width: 600px;
  padding: 20px;
  background-color: #fff;

  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.chinese {
  margin-bottom: 20px; /* 添加中文内容与按钮之间的垂直间距 */
}

.chinese h1 {
  font-size: 24px;
  color: #333;
  margin: 0; /* 清除标题默认的上下间距 */
}

.buttons {
  display: flex;
  justify-content: space-around; /* 按钮水平居中排列 */
}

.buttons button {
  padding: 10px 20px;
  font-size: 16px;
  border: none;
  cursor: pointer;
  background-color: orange;
  color: white;
  border-radius: 5px;
}

.buttons button:hover {
  background-color: darkorange;
}
</style>
