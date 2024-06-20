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
mock.onPost('/login').reply(200, {
  token: 'mock-token'
});

// 模拟注册请求
mock.onPost('/register').reply(200, {
  message: '注册成功'
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
