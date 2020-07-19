<template>
  <div class="blocker">
    <div class="actionForm">
      <div css="hl">Edit Table Parameter: {{ data["name"] }}</div>
      <div v-for="(col, idx) in defiIn" :key="idx">
        <div css="iptHl" >{{ col.hl }}:</div>
        <input type="text" v-model="data[col.col]" />
      </div>
      <div>
        <button>ok</button>
        <button v-on:click="callback">cancel</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TableParams',
  props:{
    defiIn: Array,
    dataIn: Object,
    callback: Function
  },
  data(){
    return {
      tbl: "new",
      data: {}
    }
  },
  methods:{
  
  },
  mounted: function(){
    if(this.dataIn !== undefined){
      this.data = this.dataIn;
    }
  }
}
</script>


<style>

</style>
