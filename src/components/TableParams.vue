<template>
  <div class="blocker">
    <div class="actionForm">
      <div css="hl">Edit Table Parameter: {{ tbl }}</div>
      <div v-for="(col, idx) in defiIn" :key="idx">
        <div css="iptHl" >{{ col.hl }}:</div>
        <input v-if="col.type=='static'" type="text" v-model="data[col.col]"  disabled />
        <input v-if="col.type=='text'" type="text" v-model="data[col.col]" v-on:keyup.enter="submit" />
        <!--FormElements v-bind:type="defi[idx]['type']" v-bind:val="data[col.col]" /-->
      </div>
      <div>
        <button v-on:click="submit">ok</button>
        <button v-on:click="callback">cancel</button>
      </div>
    </div>
  </div>
</template>

<script>
import FormElements from '../components/FormElements.vue'

export default {
  name: 'TableParams',
  components: {
    FormElements
  },
  props:{
    idx: null,
    defiIn: Array,
    dataIn: Object,
    callback: Function,
    refresh: Function,
  },
  data(){
    return {
      tbl: "new",
      defi: [],
      data: {}
    }
  },
  methods:{
    call_config(){
      fetch('/api/config/get') 
      .then(resp => resp.json())
      .then(resObj => {
        console.log(resObj);
        this.defi = resObj.data.defi;
        for(var prop in this.defi){
          var curCol = this.defi[prop]["col"];
          this.data[curCol] = "";
        }
        if(this.idx !== "new"){
          this.data = resObj.data.data[this.idx];
          this.tbl = this.data;
        }
      });
    },
    submit(){
      var neededVals = [];
      
      for(var prop in this.defiIn){
        var curDefi = this.defiIn[prop];
        if(curDefi.type == 'static'){
          continue;
        }
        var curVal = this.data[curDefi["col"]];
        //console.log(curVal);
        if(curDefi.manda && curVal == ""){
          neededVals.push( curDefi.hl);
        }
      }

      if(neededVals.length > 0){
        alert("Please enter value for field: " + neededVals.join(", "));
        return;
      }
      
      fetch('/api/config/set', {
        method: 'POST', 
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.data),
      })
      .then(response => response.json())
      .then(data => {
        console.log('Success:', data);
        this.refresh();
        this.callback();
      })
      .catch((error) => {
        console.error('Error:', error);
        alert("Something went wrong while writing changes to api");
        this.callback();
      });
    },  
  },
  mounted: function(){
    //this.call_config();
    //this.data = this.dataIn;
    console.log(typeof(this.dataIn));
    if(typeof(this.dataIn) == 'object'){
      //console.log(JSON.stringify(this.dataIn, null, 2));
      this.data = JSON.parse(JSON.stringify(this.dataIn)); //is das wirklich gut???
      this.tbl = this.data["name"];
    }
  }
}



</script>



<style>
</style>

