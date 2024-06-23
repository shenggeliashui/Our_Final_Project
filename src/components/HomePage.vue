<template>
  <div id="HomePage">
    <main>
      <div class="outer-box">
        <div class="left-section"></div>
        <div class="content-box">
          <header class="task-header">
            <h2>— 当前进度 —</h2>
          </header>
          <div class="word-stats">
            <div class="stat">
              <p class="number">{{ memoriedNum }}</p>
              <h1 class="chinese">已背单词数</h1>
            </div>
            <div class="stat">
              <p class="number">{{ unmemoriedNum }}</p>
              <h1 class="chinese">未背单词数</h1>
            </div>
            <div class="stat">
              <p class="number">{{ unmemoriedNum + memoriedNum }}</p>
              <h1 class="chinese">单词总数</h1>
            </div>
          </div>

          <div class="buttons">
            <button @click="MemoryWordButton">背单词</button>
            <button @click="WriteFromMemoryButton">默写单词</button>
          </div>
        </div>
        <div class="right-section"></div>
      </div>
      <router-view />
    </main>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HomePage',
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
    MemoryWordButton() {
      this.$router.push({
        name: 'MemoryTenWords'
      });
    },
    WriteFromMemoryButton() {
      this.$router.push({
        name: 'WriteFromMemory'
      });
    },
    async getMemoriedNum() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/get-memorized-num');
        this.memoriedNum = response.data.number;
      } catch (error) {
        console.error('Error calling API:', error);
      }
    },
    async getUnmemoriedNum() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/get-unmemorized-num');
        this.unmemoriedNum = response.data.number;
      } catch (error) {
        console.error('Error calling API:', error);
      }
    }
  }
};
</script>

<style scoped>
#HomePage {
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
}

.outer-box {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100vh;
  height: auto; /* 高度自适应 */
  background-color: #f9f3ea; /* 浅橙色背景 */
  padding: 20px; /* 外部填充 */
  border: 2px solid #ffa500; /* 橙色边框 */
  border-radius: 10px; /* 圆角 */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* 阴影 */
}

.left-section,
.right-section {
  width: 20%; /* 左右各占1/10 */
  height: 100%; /* 高度与外部框一致 */
}

.left-section {
  background-image: url('../assets/homepage_bg_left.png'); /* 左侧背景图片 */
  background-size: cover;
  background-position: center;
}

.right-section {
  background-image: url('../assets/homepage_bg_left.png'); /* 右侧背景图片 */
  background-size: cover;
  background-position: center;
}

.content-box {
  flex-grow: 1; /* 让内容框填充剩余空间 */
  border: 2px solid #ccc;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  background-color: #fff;
}

.task-header h2 {
  font-size: 18px;
  color: #999;
  margin-bottom: 10px;
}

.word-stats {
  display: flex;
  justify-content: center;
  align-items: flex-start; /* 顶部对齐 */
  margin-bottom: 10px;
}

.stat {
  margin: 0 15px;
}

.number {
  font-size: 36px;
  color: #333;
  font-weight: bold;
}

.chinese {
  font-size: 16px;
  color: #666;
}

.buttons {
  display: flex;
  justify-content: center;
  margin-top: 10px;
}

button {
  padding: 10px 20px;
  margin-left: 20px;
  margin-right: 20px;
  font-size: 1rem;
  border: none;
  cursor: pointer;
  background-color: orange;
  color: white;
  border-radius: 5px;
}

button:hover {
  background-color: darkorange;
}
</style>
