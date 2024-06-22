import { createStore } from 'vuex';
import axios from 'axios';

const store = createStore({
  state: {
    user: {
      avatar: 'cloud.jpg',
      nickname: '小灯',
      gender: '女',
      birthday: '1990-01-01',
      registrationDate: '2020-01-01'
    },
    notifications: [
      { id: 1, text: '欢迎使用我们的应用！' },
      { id: 2, text: '新版本已经上线，快来体验吧！' }
    ],
    studyProgress: [
      { id: 1, name: '词库1', progress: 75 },
      { id: 2, name: '词库2', progress: 50 },
      { id: 3, name: '词库3', progress: 30 }
    ],
    currentWordList: { id: 1, name: '词库1' }, // 当前词库 ID
    wordLists: [
      { id: 1, name: '词库1' },
      { id: 2, name: '词库2' },
      { id: 3, name: '词库3' }
    ]
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    setCurrentWordList(state, wordListId) {
      state.currentWordList = wordListId;
    }
  },
  actions: {
    async saveUserProfile({ commit }, user) {
      try {
        // 假设你的后端 API 端点是 /api/saveProfile
        const response = await axios.post('/api/saveProfile', user);
        commit('setUser', response.data);
      } catch (error) {
        console.error('Error saving user profile:', error);
        throw error;
      }
    },
    async changeWordList({ commit, state }, wordListId) {
      const selectedWordList = state.wordLists.find(list => list.id === wordListId);
      if (selectedWordList) {
        commit('setCurrentWordList', selectedWordList);
      }
    }
  },
  // getters: {
  //   currentWordList(state) {
  //     return state.wordLists.find(list => list.id === state.currentWordList);
  //   }
  // },
   getters: {
    currentWordList: (state) => state.currentWordList
  }
});

export default store;
