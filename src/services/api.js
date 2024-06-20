// src/services/api.js
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

export default api;


// import axios from 'axios';
//
// // 创建一个 Axios 实例
// const api = axios.create({
//   baseURL: 'http://your-api-url.com', // 替换为你的后端服务器 URL
//   timeout: 10000, // 请求超时时间
//   headers: {
//     'Content-Type': 'application/json'
//   }
// });
//
// export default api;
