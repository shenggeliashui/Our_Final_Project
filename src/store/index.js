import { createStore } from 'vuex';

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
      { id: 1, name: '词库1', progress: 50 },
      { id: 2, name: '词库2', progress: 75 }
    ]
  },
  mutations: {
    // mutation methods
  },
  actions: {
    // action methods
  }
});

export default store;
