<template>
  <div style="position:relative;">
    <div class="blocker">
      <div class="actionForm">
        <div css="hl">Edit Row: {{ id }}</div>
        <div v-for="(col, idx) in defi" :key="idx">
          <div css="iptHl" >{{col.hl}}:</div>
          <input type="text" v-model="data[col.col]" />
        </div>
        <div>
          <button v-on:click="validate">ok</button>
          <button v-on:click="callback">cancel</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RowEdit',
  props:{
    id: "",
    defi: Array,
    dataIn: Object,
    callback: Function
  },
  data(){
    return {
      name: "plaim",
      data: {} 
    }
  },
  methods:{
    validate(){
      console.log(JSON.stringify(this.data, null, 2));
    }
  },
  mounted: function(){
    if(this.id !== "new"){
      var dataStr = JSON.stringify(this.dataIn, null, 2);
      this.data = JSON.parse(dataStr);
      for(var prop in this.dataIn){
        var curVal = this.dataIn[prop];
        this.data[prop] = curVal;
      }
    }
    for(var prop in this.defi){
      var curDefi = this.defi[prop];
      if( this.data[curDefi["col"]] === undefined){
        this.data[curDefi["col"]] = "";
      }
    }
    console.log(this.data);
  }
}
</script>


<style>
.newClass{
  text-align: center;
}
</style>
