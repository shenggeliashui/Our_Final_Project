<template>
  <div id="SpellTenWords">
    <p class="number">{{ index }}/10</p>
    
    <div class="input-wrapper">
      <input
        v-model="userInput"
        :placeholder="generatePlaceholder"
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
      </div>
    </ul>

    <button @click="ClearButton">清空</button>
    <button @click="SubmitButton">提交</button>
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
      index: 0,
      actual_index: 0,
      userInput: '',
      num: 0,
      usphone: '',
      ukphone: '',
      example_sentence: '',
      meaning: '',
      inputError: false,
      correctWord: '',
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
      if (this.index >= this.num - 1) {
        this.$router.push({ name: 'FinishMemoShow' });
      } else {
        this.index += 1
        this.word = this.words[this.index]
        await this.get_word_phonetic()
        await this.get_word_meaning()
        this.userInput = ''
      }
    },

    generatePlaceholder() {
      return this.words.length > 0 ? '_'.repeat(this.words[this.index].length) : '';
    },

    async ClearButton() {
      this.userInput = '';
    },

    async SubmitButton () {
      await this.checkSpelling();
      this.NextButton()
    },

    async QuitButton () {
      this.$router.push('/HomeShow')
    },

    async checkSpelling() {
      try {
        const apiUrl = 'http://127.0.0.1:5000/api/dictation_is_word_match';
        const response = await axios.post(apiUrl, { userInput: this.userInput });
        
        if (response.data.match) {
          this.NextButton();
        } else {
          this.inputError = true;
          // this.correctWord = response.data.correct_word;
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
      // try {
      //   const response = await axios.get('http://127.0.0.1:5000/api/dictation_get_phonetics')
      //   this.usphone = response.data.usphone
      //   this.ukphone = response.data.ukphone
      //   console.log(response.data.usphone)
      // } catch (error) {
      //   console.error('Error calling API:', error)
      // }
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

    async get_word_meaning () {
      // try {
      //   const response = await axios.get('http://127.0.0.1:5000/api/dictation_get_pos_and_tran')
      //   this.meaning = response.data
      // } catch (error) {
      //   console.error('Error calling API:', error)
      // }
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
  font-size: 20px;
}
.english {
  font-size: 50px;
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
  background-color: rgb(205, 171, 110);
  color: white;
  border-radius: 5px;
}
button:hover {
  background-color: darkorange;
}
.meaning-sentence {
  text-align: left;
}
.meaning-sentence ul {
  list-style: none;
  padding-left: 0;
}
.meaning-sentence li {
  margin-bottom: 5px;
}
.input-wrapper {
  position: relative;
  margin-bottom: 10px;
}
.underlined-input {
  padding-bottom: 5px;
  background-color: transparent;
  border: none;
  border-bottom: 3px solid #000;
  outline: none;
  width: 150px;
  height: 50px;
  font-size: 32px;
  text-align: center;
}
.error {
  color: red;
}
</style>
