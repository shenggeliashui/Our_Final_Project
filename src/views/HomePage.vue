<template>
  <div>
    <h1>欢迎来到App</h1>
    <p><router-link to="/profile">个人中心</router-link></p>
  </div>
</template>

<script>
export default {
  name: 'HomePage'
};
</script>

<style scoped>
.home-container {
  padding: 20px;
  text-align: center;
}
</style>
