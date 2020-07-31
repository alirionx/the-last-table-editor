<template>
  <div class="actionForm">
    <div css="hl">Edit Table Parameter: {{ id }}</div>
    <div>
      <div css="iptHl" >Table Id:</div>
      <input type="text" v-model="id"  disabled />
    </div>
    <div v-for="(col, idx) in defi" :key="idx">
      <div css="iptHl" >{{ col.hl }}:</div>
      <input 
        v-if="col.type=='static'" 
        v-model="data[col.col]" 
        type="text"
        :id="'ipt_'+col.col"
        ref="iptIds"
        disabled />
      <input 
        v-if="col.type=='text'" 
        type="text" 
        :id="'ipt_'+col.col"
        v-model="data[col.col]" 
        v-on:keyup.enter="submit" 
        />
    </div>
    <div>
      <button v-on:click="validate">ok</button>
      <button v-on:click="backto">cancel</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TableParas',
  props:{
  },
  data(){
    return {
      id: this.$route.params.id,
      defi: [
        {
          col: "name",
          hl: "Table name",
          type: "text",
          manda: true
        },
        {
          col: "description",
          hl: "Description",
          type: "text",
          manda: false
        },
        {
          col: "comment",
          hl: "Comment",
          type: "text",
          manda: false
        }
      ],
      data: {}
    }
  },
  methods:{
    call_config(){
      fetch('/api/tableparas/get/'+this.id) 
      .then(resp => resp.json())
      .then(resObj => {
        console.log(resObj);
        //this.defi = resObj.data.defi;
        this.data = resObj.data;
      });
    },
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
      //console.log(jsonData);
      if(this.id == "new"){
        this.data.id = "new";
        var reqUrl = '/api/tableparas/add' 
      }
      else{
        var reqUrl = '/api/tableparas/edit' 
      }

      var jsonData = JSON.stringify(this.data, null, 2)

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
        this.backto();
      })
      .catch((error) => {
        console.error('Error:', error);
        alert("Something went wrong while writing changes to api");
        this.backto();
      });
    },
    backto(){
      window.location.hash = '/configure';
    }
  },
  mounted: function(){
    if(this.id !== "new"){
      this.call_config();
    }
  }
}
</script>


<style>
.newClass{
  text-align: center;
}
</style>
