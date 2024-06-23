<template>
    <div id="SpellWords">
      <Frame>
       <SpellTenWords />
      </Frame>
    </div>
  </template>
  
  <script>
  import Frame from '@/view/frame.vue';
  import SpellTenWords from '@/components/Spell.vue';
  
  export default {
    components: {
      Frame,
      SpellTenWords,
    },
  };
  </script>