import { mount } from '@vue/test-utils';
import UserProfile from '@/views/UserProfile.vue';
import api from '@/services/api';
import { createStore } from 'vuex';
import { nextTick } from 'vue';

// Mock the API
jest.mock('@/services/api');

// Create a mock store
const mockStore = {
  state: {
    user: {
      nickname: 'testuser',
      gender: '男',
      birthday: '2000-01-01',
      registrationDate: '2020-01-01',
      avatar: 'logo.png'
    },
    notifications: [],
    studyProgress: [],
    wordLists: [],
    currentWordList: { id: 1, name: '默认词库' }
  },
  getters: {
    currentWordList: state => state.currentWordList
  },
  actions: {
    saveUserProfile: jest.fn(),
    changeWordList: jest.fn()
  }
};

const store = createStore(mockStore);

describe('UserProfile.vue', () => {
  let wrapper;

  beforeEach(() => {
    wrapper = mount(UserProfile, {
      global: {
        plugins: [store]
      }
    });
  });

  it('should render the user profile', () => {
    expect(wrapper.find('.avatar').exists()).toBe(true);
    expect(wrapper.find('input.info-input').exists()).toBe(true);
  });

  it('should display user info correctly', () => {
    expect(wrapper.find('.info-item').text()).toContain('testuser');
    expect(wrapper.find('select').element.value).toBe('男');
    expect(wrapper.find('input[type="date"]').element.value).toBe('2000-01-01');
  });

  it('should call saveUserProfile action on save', async () => {
    wrapper.vm.editableUser.nickname = 'newnickname';
    wrapper.vm.editableUser.gender = '女';
    wrapper.vm.editableUser.birthday = '1990-01-01';

    await nextTick();
    await wrapper.find('.save-button').trigger('click');

    expect(mockStore.actions.saveUserProfile).toHaveBeenCalledWith(
      expect.anything(), // Vuex context
      {
        nickname: 'newnickname',
        gender: '女',
        birthday: '1990-01-01',
        registrationDate: '2020-01-01',
        avatar: 'logo.png'
      }
    );
  });

  it('should call changeWordList action on change', async () => {
    wrapper.vm.selectedWordListId = 2;

    await nextTick();
    await wrapper.find('.change-wordlist button').trigger('click');

    expect(mockStore.actions.changeWordList).toHaveBeenCalledWith(
      expect.anything(), // Vuex context
      2
    );
  });
});
/*
should render the user profile：测试用户头像和输入框是否正确渲染。
should display user info correctly：测试用户信息是否正确显示。
should call saveUserProfile action on save：测试保存按钮点击时是否调用了保存用户信息的 action。
should call changeWordList action on change：测试更换词库按钮点击时是否调用了更换词库的 action。
 */