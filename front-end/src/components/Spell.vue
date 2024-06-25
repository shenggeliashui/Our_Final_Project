<template>
  <div id="SpellTenWords">
    <p class="number">{{ index }}/10</p>
    
    <div class="input-wrapper">
      <input
        v-model="userInput"
        :placeholder="placeholderText"
        class="underlined-input"
        :class="{ error: inputError }"
      >
    </div>

    <div class="phonetic">
      <p>美式音标：{{ usphone }}</p>
      <p>英式音标：{{ ukphone }}</p>
    </div>

    <ul>
      <div class="meaning-sentence">
        <li v-for="(value, key, index) in meaning" :key="key">
          {{ index + 1 }}. {{ key }}: {{ value.join(', ') }};<br>
        </li>
        <!-- <li v-for="(value, key, index) in example_sentence" :key="key">
          {{ index + 1 }}. {{ key }}: {{ value }}
        </li> -->
      </div>
    </ul>

    <button @click="ClearButton">清空</button>
    <button @click="SubmitButton">提交</button>

    <!-- <button @click="NextButton">下一个单词</button> -->
    <nav>
      <button @click="QuitButton">首页</button>
    </nav>

    <router-view />
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'SpellTenWords',
  data () {
    return {
      words: [],
      index: 0,       // 当前默写的单词id,
      actual_index: 0,
      userInput: '',
      num: 0,         // 列表中的单词数
      usphone: '',
      ukphone: '',
      example_sentence: '', // 待完善
      meaning: '' ,         // 待完善
      inputError: false
    }
  },
  mounted () {
    this.num = 0
    this.index = 0
    this.RandomGetTenWords()
  },
  methods: {
    async RandomGetTenWords () {
      console.log("ok");
      try {
        const response1 = await axios.get('http://127.0.0.1:5000/api/dictation_fetch_random_words')
        console.log(response1.data.message);
        if (response1.data.message === 'Random words fetched successfully') {
          
          while (this.num < 10) {
            console.log(this.num);
            const response = await axios.get('http://127.0.0.1:5000/api/dictation_get_current_word')
            const word = response.data.word
            if (!this.words.includes(word)) {
              this.words.push(word)
              this.num += 1
            }
            await axios.get('http://127.0.0.1:5000/api/dictation_move_to_next_word')
          }
          this.word = this.words[this.index]
          console.log(this.word)
          await this.get_word_phonetic()
          await this.get_word_meaning()
          console.log(this.usphone)
        }
      } catch (error) {
        console.error('Error calling API:', error)
      }
    },


    async NextButton () {
      this.index = this.actual_index
      if (this.index >= this.num) {
        this.$router.push({ name: 'FinishMemoShow' });
      }
      this.get_word_phonetic()
      this.get_word_meaning()
      this.example_sentence = ''
      this.userInput = '' // 清空输入框
      this.actual_index += 1
    },

    generatePlaceholder() {
      // 生成输入框的占位符
      return '_'.repeat(this.words[this.index].length);
    },

    async ClearButton() {
      this.userInput = '';
    },

    async SubmitButton () {
      this.checkSpelling();
  
    },

    async QuitButton () {
      this.$router.push('/HomeShow')
    },

    async checkSpelling() {
      try {
        const apiUrl = `http://127.0.0.1:5000/api/dictation_is_word_match?current_word=${this.word}`;
        const response = await axios.post(apiUrl, { userInput: this.userInput });
        console.log(response.data.match);
        if (response.data.match == true) {
          // console.log("True");
          this.NextButton();
        } else {
          // console.log("False");
          this.inputError = true;
          // this.correctWord = response.data.correct_word; // 可选：将正确的单词显示在页面上
          setTimeout(() => {
            this.userInput = '';
            this.inputError = false;
          }, 1000);
        }
      } catch (error) {
        console.error('Error checking spelling:', error);
      }
    },

    async get_word_phonetic () {
      try {
          const response = await axios.get('http://127.0.0.1:5001/api/get-word-phonetic', {
            params: { word: this.words[this.index] }
          });
          this.usphone = response.data.usphone;
          this.ukphone = response.data.ukphone;
        } catch (error) {
          console.error('Error calling API:', error);
        }
    },

    async get_word_example () {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/dictation_get_example', {
          params: { word: this.words[this.index] }
        })
        this.example_sentence = response.data.example
      } catch (error) {
        console.error('Error calling API:', error)
      }
    },

    async get_word_meaning () {
      try {
          const response = await axios.get('http://127.0.0.1:5001/api/get-word-meaning', {
            params: { word: this.words[this.index] }
          });
          this.meaning = response.data.meaning;
        } catch (error) {
          console.error('Error calling API:', error);
        }
    }
  }
}
</script>

<style scoped>
  /* 页面整体样式 */
  #MemoryTenWords {
    max-width: 800px;
    margin-top: 100px;
    margin-left: 300px;
  }
  .phonetic {
    display: flex;
    justify-content: space-between;
    margin-bottom: 10px;
    font-size: 20px;
     margin-right: 0px;
  }
  .number {
    font-size: 20px; /* 设置数字的字体大小 */
  }

  .english {
    font-size: 50px; /* 设置中文的字体大小 */
  }

  button {
    padding: 10px 20px;
    margin-left: 200px;
    margin-right: 100px;
    margin-bottom: 10px;
    margin-top: 100px;
    font-size: 1rem;
    border: none;
    cursor: pointer;
    background-color: rgb(205, 171, 110); /* 设置按钮背景颜色为橙色 */
    color: white; /* 设置文字颜色为白色，以增加对比度 */
    border-radius: 5px; /* 设置按钮圆角 */
  }
  /* 悬停时按钮颜色变暗 */
  button:hover {
    background-color: darkorange;
  }
  .meaning-sentence {
    text-align: left; /* 对齐内容靠左 */
  }

  .meaning-sentence ul {
    list-style: none; /* 去除默认的列表样式 */
    padding-left: 0; /* 去除列表项的默认缩进 */
  }

  .meaning-sentence li {
    margin-bottom: 5px; /* 列表项之间的间距 */
  }

  .input-wrapper {
  position: relative;
  margin-bottom: 10px;
}

.underlined-input {
  padding-bottom: 5px; /* 与下划线高度相匹配 */
  background-color: transparent;
  border: none;
  border-bottom: 3px solid #000; /* 下划线样式 */
  outline: none;
  width: 150px; /* 根据需要调整宽度 */
  height: 50px; /* 根据需要调整宽度 */
  font-size: 32px; /* 根据需要调整字体大小 */
  text-align: center;
}

.error {
  color: red;
}
</style>