import { mount } from '@vue/test-utils';
import UserLogin from '@/components/UserLogin.vue';
import api from '@/services/api';

jest.mock('@/services/api');

describe('UserLogin.vue', () => {
  let wrapper;

  beforeEach(() => {
    wrapper = mount(UserLogin);
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  it('should render the login form', () => {
    expect(wrapper.find('h2').text()).toBe('登录');
    expect(wrapper.find('input#username').exists()).toBe(true);
    expect(wrapper.find('input#password').exists()).toBe(true);
    expect(wrapper.find('button').text()).toBe('登录');
  });

  it('should display validation errors', async () => {
    const errorResponse = {
      response: {
        data: {
          errors: {
            username: '用户名不能为空',
            password: '密码不能为空'
          }
        }
      }
    };

    api.post.mockRejectedValueOnce(errorResponse);

    await wrapper.find('form').trigger('submit.prevent');

    await wrapper.vm.$nextTick();

    const usernameError = wrapper.find('.error-message').text();
    const passwordError = wrapper.findAll('.error-message').at(1).text();

    expect(usernameError).toContain('用户名不能为空');
    expect(passwordError).toContain('密码不能为空');
  });

  it('should call the API on form submit', async () => {
    const loginResponse = {
      data: {
        token: 'fake-token'
      }
    };

    const userResponse = {
      data: {
        id: 1,
        username: 'testuser'
      }
    };

    api.post.mockResolvedValueOnce(loginResponse);
    api.get.mockResolvedValueOnce(userResponse);

    await wrapper.setData({
      username: 'testuser',
      password: 'password123'
    });

    await wrapper.find('form').trigger('submit.prevent');

    expect(api.post).toHaveBeenCalledWith('/login', {
      username: 'testuser',
      password: 'password123'
    });

    await wrapper.vm.$nextTick();

    expect(api.get).toHaveBeenCalledWith('/user/profile', {
      headers: {
        Authorization: 'Bearer fake-token'
      }
    });
  });
});
//
// 初始化和清理:
//
// 使用 beforeEach 和 afterEach 来确保每个测试都有一个干净的测试环境，并清理 API 调用的 mock。
// 表单渲染:
//
// 测试表单的基本渲染，检查必要的输入框和按钮是否存在。
// 表单验证错误:
//
// 模拟 API 调用失败并返回验证错误，检查错误消息是否正确显示在页面上。
// 表单提交处理:
//
// 模拟成功的登录 API 调用和用户信息获取 API 调用，检查这些调用是否按预期进行。