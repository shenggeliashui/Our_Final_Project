<template>
    <div id="FinishMemoShow">
      <Frame>
       <FinishTenWords />
      </Frame>
    </div>
 </template>
  
<script>
    import Frame from '@/view/frame.vue';
    import FinishTenWords from '@/components/FinishTenWords.vue';

    export default {
        name: 'FinishMemoShow',
        components: {
            Frame,
            FinishTenWords
        },
    };
</script>