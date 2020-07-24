<template>
  <div style="position:relative;">
    <TableParams 
      v-if="activeEdit !== null" 
      v-bind:idx="activeEdit" 
      v-bind:defiIn="defi" 
      v-bind:dataIn="data[activeEdit]" 
      v-bind:callback="()=>{activeEdit = null }"
      v-bind:refresh="call_config"
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
import TableParams from '../components/TableParams.vue'

export default {
  name: 'Configure',
  components: {
    ActionMenu,
    TableParams
  },
  data(){
    return {
      name: "Tables",
      defi: [
        {
          col: "id",
          hl: "Id",
          align: "center",
          type: "static",
          manda: true
        },
        {
          col: "name",
          hl: "Table name",
          align: "left",
          type: "text",
          manda: true
        },
        {
          col: "description",
          hl: "Description",
          align: "left",
          type: "text",
          manda: false
        },
        {
          col: "comment",
          hl: "Comment",
          align: "left",
          type: "text",
          manda: false
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
      activeEdit: null
    }
  },
  methods:{
    
    call_config(){
      fetch('/api/config/get') 
      .then(resp => resp.json())
      .then(resObj => {
        console.log(resObj);
        //this.defi = resObj.data.defi;
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
      this.activeEdit = idx;
    },
    call_configure(){
      console.log("Configure table: "+ this.activeMenu);
    },
    call_delete(){
      console.log("Delete table: "+ this.activeMenu);
    },
    call_add(){
      console.log("Add table: ");
      this.activeMenu = Number;
      this.activeEdit = "new";
    },
  },

  mounted: function(){
    this.call_config();
  }

}
</script>

