<template>
  <div style="position:relative;">
    <MsgBox 
      v-if="msgText !== null"
      v-bind:msg="msgText" 
      v-bind:callback="msgCallback" 
      v-bind:confirm="msgConfirm"   
    />
    <h3>This is an Configure page</h3>
    <table css="std" v-on:click="(event)=>{reset_menu(event)}">
      <thead>
        <tr>
          <th v-for="(col, idx) in defi" :key="idx" v-bind:style="{ textAlign: col.align }">
            {{ col.hl }}
          </th>
          <th>Act</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, idx) in data" :key="idx">
          <td v-for="(col, idx2) in defi" :key="idx2" v-bind:style="{ textAlign: col.align }">
            {{ row[col.col] }}
          </td>
          <td component="yes">
            <ActionMenu
              v-bind:idx="idx"
              v-bind:activeMenu="activeMenu"
              v-bind:actions="actions"
              v-bind:set_menu_callback="set_menu"
            />
          </td>
        </tr>
      </tbody>
    </table>
    <button class="mainBtn" v-on:click="this.call_add" >add table</button>

  </div>
</template>

<script>
import ActionMenu from '../components/ActionMenu.vue'
import MsgBox from '../components/MsgBox.vue'

export default {
  name: 'Configure',
  components: {
    ActionMenu,
    MsgBox
  },
  data(){
    return {
      name: "Tables",
      defi: [
        {
          col: "id",
          hl: "Id",
          align: "center",
        },
        {
          col: "name",
          hl: "Table name",
          align: "left",
        },
        {
          col: "description",
          hl: "Description",
          align: "left",
        },
        {
          col: "comment",
          hl: "Comment",
          align: "left",
        }
      ],
      data: [],
      activeMenu: Number,
      actions: [
        {
          txt: "edit",
          func: this.call_edit,
        },
        {
          txt: "configure",
          func: this.call_configure,
        },
        {
          txt: "delete",
          func: this.call_delete,
        }
      ],
      msgText: null,
      msgCallback: Function,
      msgConfirm: Function
    }
  },
  methods:{
    
    call_config(){
      fetch('/api/config/get') 
      .then(resp => resp.json())
      .then(resObj => {
        console.log(resObj);
        this.data = resObj.data;
      });
    },

    set_menu(tbl=Number){
      this.activeMenu = tbl;
      //console.log("active Menu: "+this.menu)
    },

    reset_menu(event){
      let tgtElm = event.target;
      if(tgtElm.parentNode !== null){ //SCHROTT
        if( !tgtElm.parentNode.hasAttribute("component") ){
          //console.log(tgtElm.tagName);
          this.activeMenu = Number;
        }
      }    
    },

    call_edit(idx=null){
      console.log("Edit table Params of: "+ this.activeMenu);
      window.location.hash = '/config/tableparas/'+idx
    },

    call_configure(){
      console.log("Configure table: "+ this.activeMenu);
    },

    call_delete(){
      var curId = this.activeMenu;
      //console.log("Delete table: "+ curId);
      this.msgText = "Do you really want to delete Table " + this.data[curId]["name"] + "?";
      this.msgCallback = () =>{
        this.msgText = null;
        this.msgCallback = Function;
        this.msgConfirm = Function;
      }
      this.msgConfirm = () =>{
        this.submit_delete(curId);
      }

    },

    submit_delete(id){
      var jsonData = JSON.stringify( { id: id } );
      fetch('/api/tableparas/delete', {
        method: 'POST', 
        headers: {
          'Content-Type': 'application/json',
        },
        body: jsonData,
      })
      .then(response => response.json())
      .then(data => {
        console.log('Success:', data);
        this.call_config();
      })
      .catch((error) => {
        console.error('Error:', error);
        alert("Something went wrong while writing changes to api");
      });
    },

    call_add(){
      this.activeMenu = Number;
      //this.activeEdit = "new";
      window.location.hash = '/config/tableparas/new'
    },
  },

  mounted: function(){
    this.call_config();
  }

}
</script>

