<template>
  <div style="position:relative;">
    <MsgBox 
      v-if="msgText !== null"
      v-bind:msg="msgText" 
      v-bind:callback="msgCallback" 
      v-bind:confirm="msgConfirm"   
    />
    <RowEdit 
      v-if="activeEdit !== null"
      v-bind:tbl="id"
      v-bind:id="activeEdit"
      v-bind:defi="defi"   
      v-bind:dataIn="data[activeEdit]"
      v-bind:callback="reset_edit"
      v-bind:refresh="call_table"
    />
    <h3>This is a Table page</h3>
    <table css="std" v-on:click="(event)=>{reset_menu(event)}">
      <tr>
        <th v-for="(col, idx) in defi" :key="idx" :style="{ textAlign: col.align }">{{col.hl}}</th>
        <th>Act</th>
      </tr>
      <tr v-for="(row, idx) in data" :key="idx">
        <td v-for="(col, idx2) in defi" :key="idx2" :style="{ textAlign: col.align }">{{row[col.col]}}</td>
        <td component="yes">
          <ActionMenu
            v-bind:id="idx"
            v-bind:activeMenu="activeMenu"
            v-bind:actions="actions"
            v-bind:set_menu_callback="set_menu"
          />
        </td>
      </tr>
    </table>
    <button class="mainBtn" v-on:click="call_add" >add row</button>
  </div>
</template>

<script>
import ActionMenu from '../components/ActionMenu.vue'
import MsgBox from '../components/MsgBox.vue'
import RowEdit from '../components/RowEdit.vue'

export default {
  name: 'Table',
  components:{
    ActionMenu,
    MsgBox,
    RowEdit
  },
  props:{
    
  },
  data(){
    return {
      id: this.$route.params.id,
      name: "",
      defi: [],
      data: [],
      activeMenu: null,
      activeEdit: null,
      msgText: null,
      actions: [
        {
          txt: "edit",
          func: this.call_edit,
        },
        {
          txt: "delete",
          func: this.call_delete,
        }
      ],
      msgCallback: Function,
      msgConfirm: Function
    }
  },
  methods:{

    call_table(){
      fetch('/api/table/get/'+this.id) 
        .then(resp => resp.json())
        .then(resObj => {
          console.log(resObj);
          this.defi = resObj.data.definition;
          this.data = resObj.data.data;
        });
    },

    set_menu(idx=null){
      this.activeMenu = idx;
    },
    reset_menu(event){
      let tgtElm = event.target;
      if(tgtElm.parentNode !== null){ //immer noch SCHROTT
        if( !tgtElm.parentNode.hasAttribute("component") ){
          //console.log(tgtElm.tagName);
          this.activeMenu = Number;
        }
      }    
    },
    
    call_edit(){
      console.log("Edit Row: " + this.activeMenu);
      this.activeEdit = this.activeMenu;
    },
    call_add(){
      console.log("Add new Row: ");
      this.activeEdit = "new";
    },
    reset_edit(){
      this.activeEdit = null;
    },
    
    call_delete(){
      var rowId = this.activeMenu;
      this.msgText = "Do you really want to delete row ("+this.activeMenu+") ?";
      this.msgCallback = ()=>{ this.msgText = null };
      this.msgConfirm = ()=>{ this.submit_delete(rowId) };
    },
    submit_delete(rowId){
      var reqUrl = '/api/table/row/delete';

      var dataObj = {
        tblId: this.id,
        rowId: rowId
      } 
      var jsonData = JSON.stringify(dataObj, null, 2);
      console.log(jsonData);
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
        this.call_table();
      })
      .catch((error) => {
        console.error('Error:', error);
        alert("Something went wrong while writing changes to api");
      });
    },
  },

  mounted: function(){
    this.call_table();
  }
}
</script>


<style>
.newClass{
  text-align: center;
}
</style>
