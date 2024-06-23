<template>
    <div id="SpellTenWords">
      <p class="number">{{ index }}/10</p>
        <p class="english">{{ words[index] }}</p>
        <div class="phonetic">
          <p >美式音标：{{ usphone }}</p>
          <p >英式音标：{{ ukphone }}</p>
        </div>
      <button @click="KnowWordButton">认识</button>
      <button @click="UnKnowWordButton">不认识</button>
      <ul>
        <div class="meaning-sentence">
          <li v-for="(value, key, index) in meaning" :key="key">
            {{ index + 1 }}. {{ key }}: {{ value.join(', ') }};<br>
          </li>
          <li v-for="(value, key, index) in example_sentence" :key="key">
            {{ index + 1 }}. {{ key }}: {{ value }}
          </li>
        </div>
      </ul>

      <button @click="NextButton">下一个单词</button>
      <nav>
        <button @click="QuitButton">首页</button>
        <!-- <button @click="KnowWordButton">认识</button>
        <button @click="UnKnowWordButton">不认识</button> -->
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
      index: 0, // 当前背诵的单词id,
      actual_index: 0,
      num: 0, // 列表中的单词数
      usphone: '',
      ukphone: '',
      example_sentence: '', // 待完善
      meaning: '' // 待完善
    }
  },
  mounted () {
    this.num = 0
    this.index = 0
    this.RandomGetTenWords()
    //   console.log("rebuild again");。。。
  },
  methods: {
    async NextButton () {
      this.index = this.actual_index
      if (this.index >= this.num) {
        this.$router.push({ name: 'FinishTenWords' })
      }
      this.get_word_phonetic()
      this.example_sentence = ''
      this.meaning = ''
    },
    async KnowWordButton () {
      this.get_word_example()
      this.get_word_meaning()
      this.DeleteUnmemoriedWord()
      this.AddMemoriedWord()
      this.actual_index += 1
    },
    async QuitButton () {
      this.$router.push({ name: 'HomePage' })
    },
    async UnKnowWordButton () {
      this.get_word_example()
      this.get_word_meaning()
    },
    async DeleteUnmemoriedWord () {
      try {
        await axios.post('http://127.0.0.1:5000/api/delete-unmemorized-word', {
          word: this.words[this.index]
        })
      } catch (error) {
        console.error('Error calling API:', error)
      }
    },
    async AddMemoriedWord () {
      try {
        await axios.post('http://127.0.0.1:5000/api/add-memorized-word', {
          word: this.words[this.index]
        })
      } catch (error) {
        console.error('Error calling API:', error)
      }
    },
    async RandomGetTenWords () {
      try {
        while (this.num < 10) {
          const response = await axios.get('http://127.0.0.1:5000/api/random-get-word-unmemorized')
          const word = response.data.word
          if (!this.words.includes(word)) {
            this.words.push(word)
            if (this.num === 0) {
              this.word = this.words[0]
            }
            this.num += 1
          }
        }
        this.get_word_phonetic()
      } catch (error) {
        console.error('Error calling API:', error)
      }
    },
    async get_word_phonetic () {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/get-word-phonetic', {
          params: { word: this.words[this.index] }
        })
        this.usphone = response.data.usphone
        this.ukphone = response.data.ukphone
      } catch (error) {
        console.error('Error calling API:', error)
      }
    },
    async get_word_example () {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/get-word-example', {
          params: { word: this.words[this.index] }
        })
        this.example_sentence = response.data.example
      } catch (error) {
        console.error('Error calling API:', error)
      }
    },
    async get_word_meaning () {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/get-word-meaning', {
          params: { word: this.words[this.index] }
        })
        this.meaning = response.data.meaning
      } catch (error) {
        console.error('Error calling API:', error)
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

</style>
