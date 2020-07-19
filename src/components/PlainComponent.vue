<template>
  <div class="newClass">
  
  </div>
</template>

<script>
export default {
  name: 'PlainComponent',
  props:{
    id: String
  },
  data(){
    return {
      name: "plain"
    }
  },
  methods:{
  
  }
}
</script>


<style>
.newClass{
  text-align: center;
}
</style>
