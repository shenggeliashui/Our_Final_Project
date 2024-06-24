<template>
  <div class="user-profile">
    <div class="left-column">
<!--      <img :src="avatarUrl" alt="用户的头像" class="avatar" />-->
      <div class="avatar-container">
        <img :src="avatarUrl" alt="用户的头像" class="avatar" @click="triggerFileInput" />
        <input type="file" ref="fileInput" @change="onFileChange" style="display: none;" />
      </div>
      <div class="user-info">
        <div class="info-item">
          <label><strong>昵称:</strong></label>
          <span v-show="!editingNickname" @click="editNickname">{{ editableUser.nickname }}</span>
          <input v-show="editingNickname" v-model="editableUser.nickname" class="info-input" @blur="stopEditingNickname" />
        </div>
        <div class="info-item">
          <label><strong>性别:</strong></label>
          <select v-model="editableUser.gender" class="info-input">
            <option value="男">男</option>
            <option value="女">女</option>
          </select>
        </div>
        <div class="info-item">
          <label><strong>生日:</strong></label>
          <input type="date" v-model="editableUser.birthday" class="info-input" />
        </div>
        <div class="info-item">
          <label><strong>注册日期:</strong></label>
          <input type="date" v-model="editableUser.registrationDate" class="info-input" disabled />
        </div>
        <button @click="saveProfile" class="save-button">保存</button>
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
        <div class="change-wordlist">
          <label for="wordlist-select">更换词库:</label>
          <select id="wordlist-select" v-model="selectedWordListId">
            <option v-for="list in studyProgress" :key="list.id" :value="list.id">
              {{ list.name }}<span v-if="list.id === currentWordList.id"> </span>
            </option>
          </select>
          <button @click="changeWordList">确认更换</button>
          <p><strong>当前词库:</strong> {{ currentWordList.name }}</p>
        </div>
      </div>
    </div>
    <div class="right-column">
      <Calendar />
    </div>
  </div>
</template>

<script>
import { computed,ref,onMounted } from 'vue';
import { useStore} from 'vuex';
import Calendar from '../components/Calendar.vue';
// import axios from "axios";
import api from '../services/api';


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
    const wordLists = computed(() => store.state.wordLists);
    const selectedWordListId = ref(store.state.currentWordList.id);
    const currentWordList = computed(() => store.getters.currentWordList);
    // const showInput = ref(false);
    const editingNickname = ref(false);

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
    const fetchStudyProgress = async () => {
      try {
        const response = await api.get('/user/studyProgress', {
          headers: {
            Authorization: `Bearer mock-token`
          }
        });
        // studyProgress.value = response.data;
         store.commit('setStudyProgress', response.data);
      } catch (error) {
        console.error('Error fetching study progress:', error);
      }
    };
    // onMounted(fetchStudyProgress);
    onMounted(() => {
      fetchStudyProgress();
    });
    const saveProfile = async () => {
      try {
        await store.dispatch('saveUserProfile', editableUser.value);
        // Update the user in the store after successful save
        user.value = { ...editableUser.value };
      } catch (error) {
        console.error('Error saving profile:', error);
      }
    };
    const changeWordList = async () => {
      try {
        await store.dispatch('changeWordList', selectedWordListId.value);
      } catch (error) {
        console.error('更换词库失败:', error);
      }
    };
    const onFileChange = async (e) => {
      const file = e.target.files[0];
      if (file) {
        const formData = new FormData();
        formData.append('avatar', file);
        try {
          // const response = await axios.post('/api/uploadAvatar', formData, {
          const response = await api.post('/api/uploadAvatar', formData, {
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

    const triggerFileInput = () => {
      const fileInput = document.querySelector('input[type="file"]');
      if (fileInput) fileInput.click();
    };

    const editNickname = () => {
      editingNickname.value = true;
      onMounted(() => {
        const input = document.querySelector('.info-input');
        if (input) input.focus();
      });
    };
    const stopEditingNickname = () => {
      editingNickname.value = false;
    };

    // onMounted(async () => {
    //   await store.dispatch('fetchUserProfile');
    //   user.value = { ...store.state.user };
    //   editableUser.value = { ...user.value };
    // });
     onMounted(async () => {
      // Fetch user data when component is mounted
      try {
        const token = localStorage.getItem('token');
        if (token) {
          const response = await api.get('/user/profile', {
            headers: { Authorization: `Bearer ${token}` }
          });
          editableUser.value = response.data;
        }
      } catch (error) {
        console.error('Error fetching user data:', error);
      }
    });

    return {
      editableUser,
      notifications,
      studyProgress,
      wordLists,
      selectedWordListId,
      currentWordList,
      avatarUrl,
      saveProfile,
      changeWordList,
      onFileChange,
      triggerFileInput,
      // showInput,
      editingNickname,
      editNickname,
      stopEditingNickname
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

.avatar-container {
  position: relative;
}

.avatar {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  margin-bottom: 20px;
  cursor: pointer; /* Add cursor pointer to indicate clickable */

}

.info-item {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  margin: 10px 0;
}

.info-item label {
  font-weight: bold;
  flex-shrink: 0;
  margin-right: 10px;
}

.info-input {
  width: 100%;
  padding: 5px;
  margin-top: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  transition: border-color 0.3s;
}

.info-input:focus {
  border-color: #4CAF50;
}

.save-button {
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.save-button:hover {
  background-color: #45a049;
}

.info-item span {
  flex-grow: 1;
  cursor: pointer; /* Add cursor pointer to indicate clickable */
}

.info-item input[type="date"] {
  display: inline-block;
  margin-top: 0;
  margin-left: 10px;
}

.info-item span:hover {
  text-decoration: underline;
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

.change-wordlist {
  margin-top: 20px;
}

.right-column {
  flex: 2;
}
</style>
