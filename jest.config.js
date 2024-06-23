// module.exports = {
//   preset: '@vue/cli-plugin-unit-jest'
// }
module.exports = {
  preset: '@vue/cli-plugin-unit-jest/presets/default',
  transform: {
    '^.+\\.vue$': '@vue/vue3-jest',
    '^.+\\.js$': 'babel-jest' // 处理 JavaScript 文件
  },
  moduleFileExtensions: ['js', 'jsx', 'json', 'vue'],
  testEnvironment: 'jsdom'
};
