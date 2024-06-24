<template>
    <div id="MemoryShow">
      <Frame>
       <MemoryTenWords />
      </Frame>
    </div>
 </template>
  
<script>
    import Frame from '@/view/frame.vue';
    import MemoryTenWords from '@/components/MemoryTenWords.vue';

    export default {
        name: 'MemoryShow',
        components: {
            Frame,
            MemoryTenWords
        },
    };
</script>