<template>
  <div>
    <h3>This is a Tables Select page</h3>
    <table border="0"><tr>
      <td>
        <select class="mainSelect" v-model="table">
          <option value="">Please select a table</option>
          <option v-for="(tbl, idx) in data" :key="idx" :value="idx">{{ tbl.name }}</option>
        </select>
      </td>
      <td>
        <button class="mainBtn" v-if="table !== ''" v-on:click="goto_table">ok</button>
      </td>
    </tr></table>
  </div>
</template>

<script>

export default {
  name: 'Tables',
  components: {

  },
  data(){
    return {
      name: "Tables",
      table: "",
      defi: [],
      data: []
    }
  },
  methods:{
    goto_table(){
      if(this.table !== ""){
        window.location.hash = "/table/"+this.table;
      }
    }
  },
  mounted: function(){
    fetch('/api/config/get') 
      .then(resp => resp.json())
      .then(resObj => {
        console.log(resObj);
        this.data = resObj.data;
      });
  }

}
</script>

<style scoped>
table{
  margin: 30px auto auto auto;
}
table td:first-child{
  width:260px;
  padding-left: 190px;
}
table td:nth-child(2){
  width:180px;
}
select{
  padding: 8px;
  min-width: 260px;
  margin: auto;
  border: 0.5px solid #666;
  background-color: #fff;
  box-shadow: 1px 1px 4px #777;
  color: #000;
  font-size: 16px;

}
button{
  padding: 6px;
  min-width: 120px;
  margin:auto;
  border: 1px solid #000;
  border-radius: 6px;
  background-color: #444;
  color: #fff;
  text-align: center;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.5s;
}
.button:hover{
  background-color: #111;
}

</style>