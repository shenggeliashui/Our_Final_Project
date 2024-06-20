import axios from 'axios';

// 创建一个 Axios 实例
const api = axios.create({
  baseURL: 'http://your-api-url.com', // 替换为你的后端服务器 URL
  timeout: 10000, // 请求超时时间
  headers: {
    'Content-Type': 'application/json'
  }
});

export default api;
