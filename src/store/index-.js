// src/store/index.js
import { createStore } from 'vuex';

const store = createStore({
  state: {
    user: {
      nickname: '默认昵称',
      avatar: '默认头像URL'
    },
    wordList: '默认词库',
    studyCalendar: [
      // 示例数据
      { date: '2023-06-01', completed: true },
      { date: '2023-06-02', completed: false }
    ]
  },
  mutations: {
    SET_NICKNAME(state, nickname) {
      state.user.nickname = nickname;
    },
    SET_AVATAR(state, avatar) {
      state.user.avatar = avatar;
    },
    SET_WORD_LIST(state, wordList) {
      state.wordList = wordList;
    }
  },
  actions: {
    updateNickname({ commit }, nickname) {
      commit('SET_NICKNAME', nickname);
    },
    updateAvatar({ commit }, avatar) {
      commit('SET_AVATAR', avatar);
    },
    updateWordList({ commit }, wordList) {
      commit('SET_WORD_LIST', wordList);
    }
  }
});

export default store;
