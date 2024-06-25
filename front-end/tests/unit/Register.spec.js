import { mount } from '@vue/test-utils';
import RegisterUser from '@/components/RegisterUser.vue';
import api from '@/services/api';

// Mock the API
jest.mock('@/services/api');

// Mock Vue Router
const mockRouter = {
  push: jest.fn()
};

describe('RegisterUser.vue', () => {
  let wrapper;

  beforeEach(() => {
    wrapper = mount(RegisterUser, {
      global: {
        mocks: {
          $router: mockRouter
        }
      }
    });
  });

  it('should display validation errors for empty password', async () => {
    // Set username but leave password empty
    await wrapper.find('#username').setValue('testuser');

    // Trigger form submit
    await wrapper.find('form').trigger('submit.prevent');

    // Assert that the error message for password is shown
    expect(wrapper.find('.error-message').text()).toContain('密码不能为空');
  });

  it('should display validation errors for empty username', async () => {
    // Set password but leave username empty
    await wrapper.find('#password').setValue('password123');

    // Trigger form submit
    await wrapper.find('form').trigger('submit.prevent');

    // Assert that the error message for username is shown
    expect(wrapper.find('.error-message').text()).toContain('用户名不能为空');
  });

  it('should call register API on valid form submission', async () => {
    // Set valid input values
    await wrapper.find('#username').setValue('testuser');
    await wrapper.find('#password').setValue('password123');
    await wrapper.find('#confirmPassword').setValue('password123');

    // Mock API response
    api.post.mockResolvedValue({ data: { success: true } });

    // Submit the form
    await wrapper.find('form').trigger('submit.prevent');

    // Check if API was called with correct parameters
    expect(api.post).toHaveBeenCalledWith('/register', {
      username: 'testuser',
      password: 'password123'
    });

    // Check if router push was called to redirect user
    expect(mockRouter.push).toHaveBeenCalledWith('/');
  });

  // Add more tests as needed for other scenarios

});
/*测试空密码字段验证错误：

使用 setValue 方法设置用户名，但不设置密码。
触发表单提交事件，然后断言应显示 "密码不能为空" 的错误消息。
测试空用户名字段验证错误：

使用 setValue 方法设置密码，但不设置用户名。
触发表单提交事件，然后断言应显示 "用户名不能为空" 的错误消息。
测试有效表单提交：

设置有效的用户名和密码。
模拟 API 成功响应。
触发表单提交事件，然后检查 API 调用的参数和 router.push 方法的调用。
*/