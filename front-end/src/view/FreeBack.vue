<template>
    <div id="FreeBackShow">
      <Frame>
        <div class="box">
       <FreeBack />
      </div>
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