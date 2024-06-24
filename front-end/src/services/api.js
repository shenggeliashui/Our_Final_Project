import axios from 'axios';
import MockAdapter from 'axios-mock-adapter';

const api = axios.create({
  baseURL: 'http://localhost:3000', // 示例URL
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json'
  }
});

// 创建 MockAdapter 实例
const mock = new MockAdapter(api);

// 模拟登录请求
mock.onPost('/login').reply(config => {
  const { username, password } = JSON.parse(config.data);
  if (username === 'test' && password === 'test.com') {
    return [200, { token: 'mock-token' }];
  } else {
    return [401, { errors: { username: 'Invalid username or password' } }];
  }
});

// 模拟注册请求
mock.onPost('/register').reply(config => {
  const { username, password } = JSON.parse(config.data);
  if (username !== 'test') {
    const response = { message: '注册成功' };
    response.username = username;
    response.password = password;
    return [200, response];
  } else {
    return [400, { errors: { username: 'username already in use' } }];
  }
});

// 模拟获取用户信息的请求
mock.onGet('/user/profile').reply(config => {
  const token = config.headers.Authorization;
  if (token === 'Bearer mock-token') {
    const user = {
      avatar: 'cloud.jpg',
      nickname: '小阿灯',
      gender: '女',
      birthday: '1990-01-01',
      registrationDate: '2020-01-01'
    };
    return [200, user];
  } else {
    return [401, { error: 'Unauthorized' }];
  }
});

// 模拟保存用户信息的请求
mock.onPost('/api/saveProfile').reply(config => {
  const user = JSON.parse(config.data);
  return [200, user]; // 返回修改后的用户信息
});

// 模拟上传头像的请求
mock.onPost('/api/uploadAvatar').reply(() => {
  const avatar = 'new-avatar.jpg'; // 模拟上传后的新头像
  return [200, { avatar }];
});

// 模拟获取用户词库学习进度的请求
mock.onGet('/user/studyProgress').reply(config => {
  const token = config.headers.Authorization;
  if (token === 'Bearer mock-token') {
    const studyProgress = [
      { id: 1, name: '词库1', progress: 50 },
      { id: 2, name: '词库2', progress: 7 },
      { id: 3, name: '词库3', progress: 10 }
    ];
    return [200, studyProgress];
  } else {
    return [401, { error: 'Unauthorized' }];
  }
});

// 模拟更换词库的请求
mock.onPost('/api/changeWordList').reply(config => {
  const { wordListId } = JSON.parse(config.data);
  // 模拟更换词库的成功响应
  return [200, { success: true, wordListId }];
});

export default api;
