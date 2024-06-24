<template>
    <div id="AllFrame">
      <PageHeader :userAvatarSrc="userAvatarSrcProp" :userName="'John Doe'"  :logoSrc="logoSrcProp" />
      <div class="container">
        <!-- <div class="box"> -->
          <slot></slot>
        </div>
      <!-- </div> -->
      <router-view/>
    </div>
  </template>

<script>
import PageHeader from '../components/site_header.vue'
export default {
  name: 'AllFrame',
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
