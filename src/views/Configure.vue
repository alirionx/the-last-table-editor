<template>
  <div>
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
            <MenuBtn 
              v-bind:idx="idx"
              v-bind:menu="menu"
              v-bind:callback="set_menu" />
            <MenuFrame 
              v-if="menu == idx" 
              v-bind:callback="()=>{}" 
              v-bind:type="'configure'" 
              />
          </td>
        </tr>
      </tbody>
    </table>

  </div>
</template>

<script>
import MenuBtn from '../components/MenuBtn.vue'
import MenuFrame from '../components/MenuFrame.vue'

export default {
  name: 'Configure',
  components: {
    MenuBtn,
    MenuFrame
  },
  data(){
    return {
      name: "Tables",
      defi: [],
      data: [],
      menu: Number
    }
  },
  methods:{
    
    call_config(){
      fetch('/api/config/get') 
      .then(resp => resp.json())
      .then(resObj => {
        console.log(resObj);
        this.defi = resObj.data.defi;
        this.data = resObj.data.data;
      });
    },

    set_menu(tbl=Number){
      this.menu = tbl;
      console.log("actibe Menu: "+this.menu)
    },

    reset_menu(event){
      let tgtElm = event.target;
      if(tgtElm.parentNode !== null){ //SCHROTT
        if( !tgtElm.parentNode.hasAttribute("component") ){
          //console.log(tgtElm.tagName);
          this.menu = Number;
        }
      }    
    }
  },
  mounted: function(){
    this.call_config();
  }

}
</script>

