import { mount } from '@vue/test-utils';
import UserProfile from '@/views/UserProfile.vue';
import store from '@/store';
import api from '@/services/api';
import MockAdapter from 'axios-mock-adapter';

describe('UserProfile.vue', () => {
  let mock;

  beforeEach(() => {
    mock = new MockAdapter(api);
  });

  afterEach(() => {
    mock.restore();
  });

  it('should fetch and display user profile data', async () => {
    const userProfile = { nickname: 'testuser', gender: '男', birthday: '1990-01-01', registrationDate: '2020-01-01', avatar: 'avatar.png' };
    mock.onGet('/user/profile').reply(200, userProfile);

    const wrapper = mount(UserProfile, {
      global: {
        plugins: [store]
      }
    });

    await wrapper.vm.$nextTick();
    expect(wrapper.vm.editableUser.nickname).toBe('testuser');
    expect(wrapper.vm.editableUser.gender).toBe('男');
  });

  it('should update user profile data', async () => {
    const userProfile = { nickname: 'testuser', gender: '男', birthday: '1990-01-01', registrationDate: '2020-01-01', avatar: 'avatar.png' };
    mock.onGet('/user/profile').reply(200, userProfile);
    mock.onPost('/user/profile').reply(200, { message: 'Profile updated successfully' });

    const wrapper = mount(UserProfile, {
      global: {
        plugins: [store]
      }
    });

    await wrapper.vm.$nextTick();
    wrapper.setData({ editableUser: { ...userProfile, nickname: 'updatedUser' } });
    await wrapper.find('.save-button').trigger('click');

    expect(wrapper.vm.editableUser.nickname).toBe('updatedUser');
  });

  it('should change word list', async () => {
    const wordLists = [
      { id: 1, name: 'List 1', progress: 50 },
      { id: 2, name: 'List 2', progress: 75 }
    ];
    mock.onGet('/user/wordLists').reply(200, wordLists);
    mock.onPost('/user/changeWordList').reply(200, { message: 'Word list changed successfully' });

    const wrapper = mount(UserProfile, {
      global: {
        plugins: [store]
      }
    });

    await wrapper.vm.$nextTick();
    wrapper.setData({ selectedWordListId: 2 });
    await wrapper.find('.change-wordlist button').trigger('click');

    expect(wrapper.vm.currentWordList.name).toBe('List 2');
  });
});
