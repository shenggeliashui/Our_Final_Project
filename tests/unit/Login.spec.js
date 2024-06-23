import { mount } from '@vue/test-utils';
import Login from '@/components/UserLogin.vue';
import api from '@/services/api';
import MockAdapter from 'axios-mock-adapter';

describe('Login.vue', () => {
  let mock;

  beforeEach(() => {
    mock = new MockAdapter(api);
  });

  afterEach(() => {
    mock.restore();
  });

  it('should login successfully with correct credentials', async () => {
    mock.onPost('/login').reply(200, { token: 'mock-token' });

    const wrapper = mount(Login);
    await wrapper.setData({ username: 'test', password: 'test.com' });
    await wrapper.find('form').trigger('submit.prevent');

    expect(wrapper.emitted('login-success')).toBeTruthy();
  });

  it('should show error with incorrect credentials', async () => {
    mock.onPost('/login').reply(401, { errors: { username: 'Invalid username or password' } });

    const wrapper = mount(Login);
    await wrapper.setData({ username: 'wrong', password: 'wrong' });
    await wrapper.find('form').trigger('submit.prevent');

    expect(wrapper.vm.error).toBe('Invalid username or password');
  });
});
