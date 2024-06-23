// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true
// })

// vue.config.js

const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  // 配置选项
  devServer: {
    // 开发服务器配置
    port: 8080,
    proxy: 'http://127.0.0.1:5000' // 示例：代理后端请求到本地端口5000
  }
})


