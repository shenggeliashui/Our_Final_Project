<template>
  <div class="user-profile">
    <div class="left-column">
<!--      <img :src="user.avatar" alt="头像" class="avatar" />-->
      <img :src="avatarUrl" alt="用户的头像" class="avatar" />
      <div class="user-info">
        <p><strong>昵称:</strong> {{ user.nickname }}</p>
        <p><strong>性别:</strong> {{ user.gender }}</p>
        <p><strong>生日:</strong> {{ user.birthday }}</p>
        <p><strong>注册日期:</strong> {{ user.registrationDate }}</p>
      </div>
    </div>
    <div class="center-column">
      <div class="notification">
        <h3>官方消息通知</h3>
        <ul>
          <li v-for="message in notifications" :key="message.id">{{ message.text }}</li>
        </ul>
      </div>
      <div class="study-progress">
        <h3>词库学习进度</h3>
        <ul>
          <li v-for="wordList in studyProgress" :key="wordList.id">{{ wordList.name }}: {{ wordList.progress }}%</li>
        </ul>
      </div>
    </div>
    <div class="right-column">
      <Calendar />
    </div>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useStore } from 'vuex';
import Calendar from '../components/Calendar.vue';

export default {
  name: 'UserProfile',
  components: {
    Calendar
  },
  setup() {
    const store = useStore();
    const user = computed(() => store.state.user);
    const notifications = computed(() => store.state.notifications);
    const studyProgress = computed(() => store.state.studyProgress);

    const avatarUrl = computed(() => {
      // 使用 import 语句来处理 Webpack 静态资源
      return require(`../assets/${user.value.avatar}`);
    });
    return {
      user,
      notifications,
      studyProgress,
      avatarUrl
    };
  }
};
</script>

<style scoped>
.user-profile {
  display: flex;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  gap: 20px;
}

.left-column, .center-column, .right-column {
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.left-column {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.avatar {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  margin-bottom: 20px;
}

.user-info p {
  margin: 10px 0;
}

.center-column {
  flex: 2;
}

.notification, .study-progress {
  margin-bottom: 20px;
}

.notification ul, .study-progress ul {
  list-style-type: none;
  padding: 0;
}

.notification li, .study-progress li {
  background: #fff;
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 4px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.right-column {
  flex: 2;
}
</style>
