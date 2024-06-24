<template>
    <div id="MemoryTenWords">
      <main>
        <div class="content-box">
          <header class="task-header">
            <h2>— 本次背词进度 —</h2>
            <p class="number">{{ index }}/10</p>
          </header>
  
          <p class="word">{{ words[index] }}</p>
  
          <div class="phonetic">
            <p>美式音标：{{ usphone }}</p>
            <p>英式音标：{{ ukphone }}</p>
          </div>
  
          <ul class="meaning-sentence">
            <li v-for="(value, key) in meaning" :key="key">
              {{ key }}: {{ value.join(', ') }}
            </li>
            <li v-for="(value, key) in example_sentence" :key="key">
              {{ key }}: {{ value }}
            </li>
          </ul>
  
          <div class="middle-buttons">
            <button @click="KnowWordButton">认识</button>
            <button @click="UnKnowWordButton">不认识</button>
          </div>
  
          <div class="bottom-buttons">
            <button @click="NextButton">下一个单词</button>
            <button @click="QuitButton">首页</button>
          </div>
        </div>
        <!-- <router-view /> -->
      </main>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'MemoryTenWords',
    data() {
      return {
        words: [],
        index: 0,
        actual_index: 0,
        num: 0,
        usphone: "",
        ukphone: "",
        example_sentence: "",
        meaning: ""
      };
    },
    mounted() {
      this.num = 0;
      this.index = 0;
      this.RandomGetTenWords();
    },
    methods: {
      NextButton() {
        this.index = this.actual_index;
        if (this.index >= this.num) {
          this.$router.push({ name: 'FinishMemoShow' });
        }
        this.get_word_phonetic();
        this.example_sentence = "";
        this.meaning = "";
      },
      async KnowWordButton() {
        await this.get_word_example();
        await this.get_word_meaning();
        await this.DeleteUnmemoriedWord();
        await this.AddMemoriedWord();
        this.actual_index += 1;
      },
      QuitButton() {
        this.$router.push('/')
      },
      async UnKnowWordButton() {
        await this.get_word_example();
        await this.get_word_meaning();
      },
      async DeleteUnmemoriedWord() {
        try {
          await axios.post('http://127.0.0.1:5000/api/delete-unmemorized-word', {
            word: this.words[this.index]
          });
        } catch (error) {
          console.error('Error calling API:', error);
        }
      },
      async AddMemoriedWord() {
        try {
          await axios.post('http://127.0.0.1:5000/api/add-memorized-word', {
            word: this.words[this.index]
          });
        } catch (error) {
          console.error('Error calling API:', error);
        }
      },
      async RandomGetTenWords() {
        try {
          while (this.num < 10) {
            const response = await axios.get('http://127.0.0.1:5000/api/random-get-word-unmemorized');
            const word = response.data.word;
            if (!this.words.includes(word)) {
              this.words.push(word);
              if (this.num === 0) {
                this.word = this.words[0];
              }
              this.num += 1;
            }
          }
          this.get_word_phonetic();
        } catch (error) {
          console.error('Error calling API:', error);
        }
      },
      async get_word_phonetic() {
        try {
          const response = await axios.get('http://127.0.0.1:5000/api/get-word-phonetic', {
            params: { word: this.words[this.index] }
          });
          this.usphone = response.data.usphone;
          this.ukphone = response.data.ukphone;
        } catch (error) {
          console.error('Error calling API:', error);
        }
      },
      async get_word_example() {
        try {
          const response = await axios.get('http://127.0.0.1:5000/api/get-word-example', {
            params: { word: this.words[this.index] }
          });
          this.example_sentence = response.data.example;
        } catch (error) {
          console.error('Error calling API:', error);
        }
      },
      async get_word_meaning() {
        try {
          const response = await axios.get('http://127.0.0.1:5000/api/get-word-meaning', {
            params: { word: this.words[this.index] }
          });
          this.meaning = response.data.meaning;
        } catch (error) {
          console.error('Error calling API:', error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  #MemoryTenWords {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100vw;
    height: 100vh;
    padding: 20px;
    box-sizing: border-box;
  }
  
  main {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-grow: 1;
  }
  
  .content-box {
    width: 100%;
    max-width: 600px;
    padding: 20px;
    background-color: #fff;
    border: 2px solid #ffa500;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  
  .task-header {
    margin-bottom: 20px;
  }
  
  .task-header h2 {
    font-size: 18px;
    color: #999;
  }
  
  .number {
    font-size: 24px;
    color: #333;
  }
  
  .word {
    font-size: 40px;
    margin-bottom: 10px;
  }
  
  .phonetic {
    display: flex;
    justify-content: space-between;
    font-size: 18px;
    margin-bottom: 10px;
  }
  
  .meaning-sentence {
    text-align: left;
    margin-top: 20px;
  }
  
  .meaning-sentence li {
    margin-bottom: 8px;
  }
  
  .middle-buttons {
    width: calc(100%); /* 减去左边距 */
    max-width: 600px; /* 与 content-box 的最大宽度保持一致 */
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    margin-top: 20px;
    margin-left: 0px; /* 与 content-box 左边框相隔 6px */
  }
  
  .middle-buttons button {
    width: 100%;
    padding: 10px 20px;
    margin-bottom: 10px;
    font-size: 16px;
    background-color: lightsalmon;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  
  .middle-buttons button:hover {
    background-color: coral;
  }
  
  .bottom-buttons {
    display: flex;
    justify-content: center; /* 水平居中 */
    width: 100%;
    max-width: 600px; /* 与 content-box 的最大宽度保持一致 */
    margin-top: 20px;
  }
  
  .bottom-buttons button {
    flex: 1; /* 均分宽度 */
    margin: 0 5px; /* 按钮之间的间距 */
    padding: 10px 20px;
    font-size: 16px;
    background-color: orange;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .bottom-buttons button:first-child {
    margin-left: 0;
  }
  
  .bottom-buttons button:last-child {
    margin-right: 0;
  }
  
  .bottom-buttons button:hover {
    background-color: darkorange;
  }
  </style>