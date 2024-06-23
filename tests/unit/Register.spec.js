import { mount } from '@vue/test-utils';
import Register from '@/components/RegisterUser.vue';
import api from '@/services/api';
import MockAdapter from 'axios-mock-adapter';

describe('Register.vue', () => {
  let mock;

  beforeEach(() => {
    mock = new MockAdapter(api);
  });

  afterEach(() => {
    mock.restore();
  });

  it('should register successfully with unique username', async () => {
    mock.onPost('/register').reply(200, { message: '注册成功', username: 'newuser', password: 'newpassword' });

    const wrapper = mount(Register);
    await wrapper.setData({ username: 'newuser', password: 'newpassword' });
    await wrapper.find('form').trigger('submit.prevent');

    expect(wrapper.vm.message).toBe('注册成功');
  });

  it('should show error with existing username', async () => {
    mock.onPost('/register').reply(400, { errors: { username: 'username already in use' } });

    const wrapper = mount(Register);
    await wrapper.setData({ username: 'test', password: 'test.com' });
    await wrapper.find('form').trigger('submit.prevent');

    expect(wrapper.vm.error).toBe('username already in use');
  });
});
