<template>
  <div>
    <input v-if="type=='static'" v-model="val" type="text" disabled />
    <input v-if="type=='text'" v-model="val" type="text" />
  </div>
</template>

<script>
export default {
  name: 'FormElements',
  props:{
    val: "",
    type: String
  },
  data(){
    return {
      value: ""
    }
  },
  methods:{

  },
  mounted: function(){
    this.value = this.val;
  },
  updated: function(){
    //this.value = this.val;
  }
}
</script>


<style>
.newClass{
  text-align: center;
}
</style>
