<template>
  <div class="user-profile">
    <div class="left-column">
<!--      <img :src="user.avatar" alt="头像" class="avatar" />-->
      <img :src="avatarUrl" alt="用户的头像" class="avatar" />
      <div class="user-info">
        <div>
          <label><strong>头像:</strong></label>
          <input type="file" @change="onFileChange" />
        </div>
        <div>
          <label><strong>昵称:</strong></label>
          <input v-model="editableUser.nickname" />
        </div>
        <div>
          <label><strong>性别:</strong></label>
          <select v-model="editableUser.gender">
            <option value="男">男</option>
            <option value="女">女</option>
          </select>
        </div>
        <div>
          <label><strong>生日:</strong></label>
          <input type="date" v-model="editableUser.birthday" />
        </div>
        <div>
          <label><strong>注册日期:</strong></label>
          <input type="date" v-model="editableUser.registrationDate" disabled />
        </div>
        <button @click="saveProfile">保存</button>
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
import { computed,ref } from 'vue';
import { useStore } from 'vuex';
import Calendar from '../components/Calendar.vue';
import axios from "axios";


export default {
  name: 'UserProfile',
  components: {
    Calendar
  },
  setup() {
    const store = useStore();
    const user = ref({ ...store.state.user });
    const editableUser = ref({ ...user.value });
    const notifications = computed(() => store.state.notifications);
    const studyProgress = computed(() => store.state.studyProgress);

    const avatarUrl = computed(() => {
      // 使用 import 语句来处理 Webpack 静态资源
      return require(`../assets/${editableUser.value.avatar}`);
    });
    // const avatarUrl = computed(() => {
    //   return `/uploads/${editableUser.value.avatar}`;
    // });
    // const avatarUrl = computed(() => {
    //   return new URL(`../assets/${editableUser.value.avatar}`, import.meta.url).href;
    // });
    const saveProfile = async () => {
      try {
        await store.dispatch('saveUserProfile', editableUser.value);
        // Update the user in the store after successful save
        user.value = { ...editableUser.value };
      } catch (error) {
        console.error('Error saving profile:', error);
      }
    };
    // const onFileChange = (e) => {
    //   const file = e.target.files[0];
    //   if (file) {
    //     const reader = new FileReader();
    //     reader.onload = (event) => {
    //       user.value.avatar = event.target.result; // Base64 URL
    //     };
    //     reader.readAsDataURL(file);
    //   }
    // };
    const onFileChange = async (e) => {
      const file = e.target.files[0];
      if (file) {
        const formData = new FormData();
        formData.append('avatar', file);
        try {
          const response = await axios.post('/api/uploadAvatar', formData, {
            headers: {
              'Content-Type': 'multipart/form-data',
            },
          });
          user.value.avatar = response.data.avatar;
        } catch (error) {
          console.error('Error uploading avatar:', error);
        }
      }
    };
    return {
      editableUser,
      notifications,
      studyProgress,
      avatarUrl,
      saveProfile,
      onFileChange
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
