<template>
    <div id="HomeShow">
      <Frame>
       <HomePage />
      </Frame>
    </div>
  </template>
  
  <script>
  import Frame from '@/view/frame.vue';
  import HomePage from '@/components/Homepage.vue';
  
  export default {
    components: {
      Frame,
      HomePage,
    },
  };
  </script>