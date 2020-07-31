<template>
  <div style="position:relative;">
    <div class="blocker">
      <div class="actionForm">
        <div css="hl">Edit Row: {{ id }}</div>
        <div v-for="(col, idx) in defi" :key="idx">
          <div css="iptHl" >{{col.hl}}:</div>
          <!--IptTest v-bind:val="data[col.col]" /-->

          <input 
            v-if="col.type == 'text'" 
            type="text" 
            :id="'ipt_'+col.col" 
            v-model="data[col.col]" 
            v-on:keyup.enter="submit" />

          <input 
            v-if="col.type == 'number'" 
            type="number" 
            :id="'ipt_'+col.col" 
            v-model="data[col.col]" 
            v-on:keyup.enter="submit" />
          
          <input 
            v-if="col.type == 'checkbox'" 
            type="checkbox" 
            :id="'ipt_'+col.col" 
            v-model="data[col.col]" />
          
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
    tbl: String,
    id: "",
    defi: Array,
    dataIn: Object,
    callback: Function,
    refresh: Function
  },
  data(){
    return {
      data: {} 
    }
  },
  methods:{
    validate(){
      var chk = false;
      for(var prop in this.defi){
        var curDefi = this.defi[prop];
        var curCol = curDefi["col"]
        //console.log(curDefi.hl);
        if(curDefi.manda && (this.data[curCol] === "" || this.data[curCol] === undefined) ){
          this.redHighLight("ipt_"+curCol);
          chk = true;
        }
      }
      if(chk){return;}
      this.submit();
    },
    redHighLight(elmId){
      var elm = document.getElementById(elmId);
      var tmpBgCol = elm.style.backgroundColor;
      elm.style.backgroundColor = "#ffe6e6";
      elm.focus();
      setTimeout(function(){elm.style.backgroundColor = tmpBgCol}, 400);
    },
    submit(){
      var reqUrl = '/api/table/row/edit';

      var dataObj = {
        tblId: this.tbl,
        rowId: this.id,
        data: this.data
      } 
      var jsonData = JSON.stringify(dataObj, null, 2);
     
      fetch(reqUrl, {
        method: 'POST', 
        headers: {
          'Content-Type': 'application/json',
        },
        body: jsonData,
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
      });
    },
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
  },
  
}

/*
import Vue from 'vue'
Vue.component('IptTest', {
  props: {
    val: String
  },
  render: function (createElement) {
    var self = this
    return createElement('input', {
      domProps: {
        type: 'text',
        value: self.val
      }
    })
  }
})
*/

</script>


<style>
.newClass{
  text-align: center;
}
</style>
