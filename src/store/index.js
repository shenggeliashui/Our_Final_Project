import { createStore } from 'vuex';
// import axios from 'axios';
import api from '../services/api';

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
      { id: 1, name: '词库', progress: 75 },
      { id: 2, name: '词库2', progress: 50 },
      { id: 3, name: '词库3', progress: 30 }
    ],
    currentWordList: { id: 2, name: '词库2' }, // 当前词库 ID
    wordLists: [
      { id: 1, name: '词库a' },
      { id: 2, name: '词库b' },
      { id: 3, name: '词库3' }
    ]
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    setStudyProgress(state, progress) {
      state.studyProgress = progress;
    },
    setCurrentWordList(state, wordListId) {
      state.currentWordList = wordListId;
    }
  },
  actions: {
    async saveUserProfile({ commit }, user) {
      try {
        // 假设你的后端 API 端点是 /api/saveProfile
        // const response = await axios.post('/api/saveProfile', user);
        const response = await api.post('/api/userUpdateInformation', user);//backend
        commit('setUser', response.data);
      } catch (error) {
        console.error('Error saving user profile:', error);
        throw error;
      }
    },
    // async changeWordList({ commit, state }, wordListId) {
    //   const selectedWordList = state.wordLists.find(list => list.id === wordListId);
    //   if (selectedWordList) {
    //     commit('setCurrentWordList', selectedWordList);
    //   }
    // },
    async changeWordList({ commit,state }, wordListId) {
      try {
        await api.post('/api/userUpdateBookId', { wordListId });//backend
        const selectedWordList = state.studyProgress.find(list => list.id === wordListId);
        commit('setCurrentWordList', selectedWordList);
      } catch (error) {
        console.error('Error changing word list:', error);
        throw error;
      }
    },
    async fetchUserProfile({ commit }) {
      try {
        // const response = await axios.get('/api/user/profile', {
        const response = await api.get('/api/profile',{//backend
          headers: {
              Authorization: `Bearer ${localStorage.getItem('token')}`
            }
        });
        commit('setUser', response.data);
      } catch (error) {
        console.error('Error fetching user profile:', error);
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
