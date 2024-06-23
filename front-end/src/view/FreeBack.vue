<template>
    <div id="FreeBackShow">
      <Frame>
       <FreeBack />
      </Frame>
    </div>
  </template>
  
  <script>
  import Frame from '@/view/frame.vue';
  import FreeBack from '@/components/freeback.vue';
  
  export default {
    components: {
      Frame,
      FreeBack,
    },
  };
  </script>