<template>
  <div style="position:relative;">
    <MsgBox 
      v-if="msgText !== null"
      v-bind:msg="msgText" 
      v-bind:callback="msgCallback" 
    />
    <h3>Edit Table Definition {{ name }}</h3> 
    <table>
      <tr>
        <th css="top">Option</th>
        <th css="col" v-for="(col, idx) in defi" :key="idx">col{{idx+1}}: {{ col.col }}
          <div class="plusminus" css="minus" v-on:click="del_col(idx)"><div></div></div>
        </th>
        <th>
          <div class="plusminus" v-on:click="add_col"><div></div><div></div></div>
        </th>
      </tr>
      <tr>
        <th css="left">Column Name</th>
        <td v-for="(col, idx) in defi" :key="idx">
          <input type="text" v-model="col.col" placeholder="avoid special characters" />
        </td>
      </tr>
      <tr>
        <th css="left">Column Headline</th>
        <td v-for="(col, idx) in defi" :key="idx">
          <input type="text" v-model="col.hl" />
        </td>
      </tr>
      <tr>
        <th css="left">Column Type</th>
        <td v-for="(col, idx) in defi" :key="idx">
          <select type="dropdown" v-model="col.type" >
            <option v-for="opt in dropdowns.coltype" :key="opt.val" :value="opt.val">{{ opt.txt }}</option>
          </select>
        </td>
      </tr>
      <tr>
        <th css="left">Text Alignment</th>
        <td v-for="(col, idx) in defi" :key="idx">
          <select type="dropdown" v-model="col.align" >
            <option v-for="opt in dropdowns.colalign" :key="opt.val" :value="opt.val">{{ opt.txt }}</option>
          </select>
        </td>
      </tr>
      <tr>
        <th css="left">Mandatory</th>
        <td v-for="(col, idx) in defi" :key="idx">
          <input type="checkbox" v-model="col.manda" />
        </td>
      </tr>
    </table>
    <button class="mainBtn" v-on:click="config_apply">apply</button>
    <button class="mainBtn" v-on:click="config_cancel">back</button>
  </div>
</template>

<script>
import MsgBox from '../components/MsgBox.vue'

export default {
  name: 'TableConfiguration',
  components: {
    MsgBox
  },
  props:{

  },
  data(){
    return {
      id: this.$route.params.id,
      name: String,
      defi:[],
      dropdowns:{
        coltype:[
          {
            val: "text",
            txt: "Text input"
          },
          {
            val: "number",
            txt: "Full number"
          },
          {
            val: "date",
            txt: "Date"
          },
          {
            val: "checkbox",
            txt: "Checkbox"
          },
          {
            val: "select",
            txt: "dropdown list"
          }
        ],
        colalign:[
          {
            val: "left",
            txt: "left"
          },
          {
            val: "center",
            txt: "center"
          },
          {
            val: "right",
            txt: "right"
          }
        ]
      },
      msgText: null,
      msgCallback: Function
    }
  },
  methods:{
    call_defi(){
      fetch('/api/tableparas/get/'+this.id) 
      .then(resp => resp.json())
      .then(resObj => {
        console.log(resObj);
        this.name = resObj.data.name; 
        this.defi = resObj.data.definition;
      });
    },

    add_col(){
      var colObj = {
        col: "",
        hl: "",
        type: "text",
        align: "left",
        manda: false
      }
      this.defi.push(colObj);
    },

    del_col(idx){
      var tmpObj = this.defi;
      this.defi = [];
      for(var prop in tmpObj){
        if(prop != idx){
          this.defi.push(tmpObj[prop]);
        }
      }
    },

    config_apply(){
      var jsonData = JSON.stringify( this.defi, null, 2);
      console.log(jsonData);

      fetch('/api/tableconfig/apply/'+this.id, {
        method: 'POST', 
        headers: {
          'Content-Type': 'application/json',
        },
        body: jsonData,
      })
      .then(response => response.json())
      .then(data => {
        console.log('Success:', data);
        this.msgText = "changes are successfully applied";
        this.msgCallback = () => {this.msgText = null};
        this.call_defi();
      })
      .catch((error) => {
        console.error('Error:', error);
        alert("Something went wrong while writing changes to api");
      });
    },

    config_cancel(){
      window.location.hash = '/configure';
    }

  },
  mounted: function(){
    this.call_defi();
  }
}
</script>


<style scoped>
.newClass{
  text-align: center;
}

table{
  margin: 40px auto 20px auto;
  font-size: 15px;
}
table th{
  padding:10px;
  background-color: #eee;
  color: #000;
  font-weight: bold;
  font-size: 14px;
  border: 1px solid #444;
}
table th[css=top]{
  text-align: center;
  background-color: #333;
  color: #fff;
}
table th[css=col]{
  text-align: left;
  background-color: #eee;
}
table th[css=left]{
  text-align: right;
  width:120px;
}
table td{
  padding:10px;
  border: 1px solid #444;
  color: #000;
  min-width:100px;
  text-align: left;
}
table input[type="text"]{
  margin:-6px;
  padding:4px 4px 4px 8px;
  border: 0.5px solid #aaa;
  background-color: rgb(247, 250, 255);
  width:98%;
  font-size: 15px;
  color:#000;
}
table input[type="checkbox"]{
  margin:-4px auto -4px 2px;
  transform: scale(1.3);
}
table select[type="dropdown"]{
  margin:-6px;
  padding:4px 4px 4px 8px;
  border: 0.5px solid #aaa;
  background-color: rgb(247, 250, 255);
  width:104%;
  font-size: 15px;
  color:#000;
}
.plusminus{
  position: relative;
  float:right;
  width:18px;
  height: 18px;
  margin:-8px auto -8px auto;
  background-color: #eee;
  border-radius: 12px;
  border:2px solid #000;
  cursor:pointer;
  transition: background-color 0.5s;
}
.plusminus[css=minus]{
  margin-top: -3px;
  margin-right: -6px;
}
.plusminus:hover{
  background-color: #555;
}
.plusminus:hover div{
  background-color: #eee;
}
.plusminus div{
  position:absolute;
  background-color: #000;
  transition: background-color 0.5s;
}
.plusminus div:first-child{
  left: 10%;
  top: 42%;
  height: 20%;
  width: 80%;
}
.plusminus div:nth-child(2){
  left: 40%;
  top: 10%;
  height: 80%;
  width: 20%;
}




</style>
