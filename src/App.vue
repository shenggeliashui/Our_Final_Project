<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
import PageHeader from './components/site_header.vue'
export default {
  name: 'App',
  components: {
    PageHeader
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
