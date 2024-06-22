<template>
  <div id="app">
    <PageHeader :userAvatarSrc="userAvatarSrcProp" :userName="'John Doe'"  :logoSrc="logoSrcProp" />
    <div class="container">
      <div class="box">
      </div>
    </div>
    <router-view/>
  </div>
</template>

<script>
import PageHeader from './components/site_header.vue'
export default {
  name: 'App',
  components: {
    PageHeader
  },
  data () {
    return {
      userAvatarSrcProp: require('@/assets/photo1.png'),
      logoSrcProp: require('@/assets/logo1.png') // 使用 require 导入图片路径
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
  padding:0px;
  border: radius 5px;
}
</style>
