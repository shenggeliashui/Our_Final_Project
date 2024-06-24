<template>
    <div class="user-profile">
      <Frame>
      <h2>个人中心</h2>
      <div class="profile-section">
        <label for="nickname">用户昵称:</label>
        <input type="text" id="nickname" v-model="nickname" @blur="updateNickname" />
      </div>
      <div class="profile-section">
        <label for="avatar">用户头像:</label>
        <input type="file" id="avatar" @change="onAvatarChange" />
        <img :src="avatar" alt="用户头像" v-if="avatar" />
      </div>
      <div class="profile-section">
        <button @click="showCurrentWordList">当前词库</button>
        <button @click="changeWordList">修改词库</button>
      </div>
      <div class="profile-section">
        <h3>背书日历</h3>
        <ul>
          <li v-for="entry in studyCalendar" :key="entry.date">
            {{ entry.date }}: {{ entry.completed ? '完成' : '未完成' }}
          </li>
        </ul>
      </div>
    </Frame>
    </div>
  </template>
  
  <script>
  import { computed } from 'vue';
  import { useStore } from 'vuex';
  
  export default {
    name: 'UserProfile',
    setup() {
      const store = useStore();
  
      const nickname = computed({
        get: () => store.state.user.nickname,
        set: value => store.dispatch('updateNickname', value)
      });
  
      const avatar = computed(() => store.state.user.avatar);
  
      const onAvatarChange = event => {
        const file = event.target.files[0];
        if (file) {
          const reader = new FileReader();
          reader.onload = e => {
            store.dispatch('updateAvatar', e.target.result);
          };
          reader.readAsDataURL(file);
        }
      };
  
      const showCurrentWordList = () => {
        alert(`当前词库: ${store.state.wordList}`);
      };
  
      const changeWordList = () => {
        const newWordList = prompt('请输入新的词库名:');
        if (newWordList) {
          store.dispatch('updateWordList', newWordList);
        }
      };
  
      const studyCalendar = computed(() => store.state.studyCalendar);
  
      return {
        nickname,
        avatar,
        onAvatarChange,
        showCurrentWordList,
        changeWordList,
        studyCalendar
      };
    }
  };
  </script>
  
  <style scoped>
  .user-profile {
    /* max-width: 1200px;
    margin: 50px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); */
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
  
  .profile-section {
    margin-bottom: 20px;
  }
  
  .profile-section label {
    display: block;
    margin-bottom: 5px;
  }
  
  .profile-section input[type="text"] {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
  }
  
  .profile-section img {
    display: block;
    margin-top: 10px;
    max-width: 100px;
    border-radius: 50%;
  }
  
  .profile-section button {
    padding: 10px 15px;
    margin-right: 10px;
    background-color: lightsalmon;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .profile-section button:hover {
    background-color: coral;
  }
  </style>
  