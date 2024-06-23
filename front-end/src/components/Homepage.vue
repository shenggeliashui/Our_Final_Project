<template>
    <div id="HomePage">
      <!-- 显示已背单词数、未背单词数和总单词数 -->
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
  
      <!-- 设置跳转链接按钮 -->
      <nav>
        <button @click="MemoryWordButton">背单词</button>
        <button @click="WriteFromMemoryButton">默写单词</button>
      </nav>
  
      <!-- 路由视图，用于显示跳转页面的内容 -->
      <router-view />
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
          name: 'Spell'
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
  }
  </script>
  
  <style scoped>
  /* 样式可以根据需求自行调整 */
  #HomePage {
    max-width: 800px;
    margin-top: 200px;
    margin-left: 300px;
  }
  
  .word-stats {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
  }
  
  .number {
    font-size: 40px; /* 设置数字的字体大小 */
  }
  
  .chinese {
    font-size: 20px; /* 设置中文的字体大小 */
  }
  .stat {
    flex: 1;
    text-align: center;
  }
  
  button {
    padding: 10px 20px;
    margin-left: 50px;
    margin-right: 50px;
    margin-bottom: 10px; 
    font-size: 1rem;
    border: none;
    cursor: pointer;
    background-color: orange; /* 设置按钮背景颜色为橙色 */
    color: white; /* 设置文字颜色为白色，以增加对比度 */
    border-radius: 5px; /* 设置按钮圆角 */
  }
  /* 悬停时按钮颜色变暗 */
  button:hover {
    background-color: darkorange;
  }
  
  
  </style>
  