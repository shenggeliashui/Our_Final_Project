<template>
  <div>
    <h1>write from memory(other groupmembers' work)</h1>
    <nav>
      <button @click="QuitButton">回到首页</button>
     </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'WriteFromMemory',
  methods:{
    QuitButton(){
       this.$router.push({
        name: 'HomePage'
      });
    }
  }
}
</script>

<style scoped>
h1 {
  color: blue;
}
</style>
