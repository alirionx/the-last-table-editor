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
      v-bind:id="activeEdit"
      v-bind:defi="defi"   
      v-bind:dataIn="data[activeEdit]"
      v-bind:callback="reset_edit"
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
    <button class="mainBtn" v-on:click="call_add" >add table</button>
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
      console.log("Delete Row: " + this.activeMenu);
    }
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
