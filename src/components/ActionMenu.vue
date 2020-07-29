<template>
  <div class="menuBtnFrame" v-if="activeMenu !== id" v-on:click="set_menu_callback(id)">
    <div></div>
    <div></div>
    <div></div>
  </div>
  <div v-else class="menuBtnActive" v-on:click="()=>{}" >
    <div class="menuFrame">
      <div v-for="(act, idx) in menuActions" :key="idx" v-on:click="act.func()" >{{ act.txt }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ActionMenu',
  props:{
    activeMenu: "",
    id: Number,
    set_menu_callback: Function,
    actions: Array
  },
  data(){
    return {
      menuActions: [ ]
    }
  },
  methods:{
    test_alert(msg="test"){
      alert(msg);
    }
  },
  mounted: function(){
    this.menuActions = this.actions;
  }
}
</script>


<style scoped>

.menuBtnFrame{
  width: 20px;
  padding: 1px;
  margin: -4px auto -4px auto;
  text-align: center;
  border: 0.5px solid #999;
  border-radius: 4px;
  cursor: pointer;
  transition:  background-color 0.5s;
}
.menuBtnFrame div{
  width: 14px;
  height: 5px;
  border-radius: 3px;
  background-color: #666;
  margin: 2px auto 2px auto;
  transition:  background-color 0.5s;
}
.menuBtnFrame:hover{
  background-color: #666;
  border: 0.5px solid #666;
}
.menuBtnFrame:hover div{
  background-color: #fff;
}
.menuBtnActive{
  position: relative;
  margin: -4px auto -4px auto;
  width: 0;
  height: 0;
  border-top: 8px solid transparent;
  border-left: 18px solid #444;
  border-bottom: 8px solid transparent;
}

.menuFrame{
  position: absolute;
  left: 22px;
  top: -12px;
  width: 90px;
  margin: auto;
  text-align: center;
}
.menuFrame div{
  padding: 3px;
  margin-bottom: -1px;
  border: 1px solid #fff;
  border-radius: 4px;
  background-color: #444;
  color: #fff;
  text-align: center;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.5s;
}

.menuFrame div:hover{
  background-color: #000;
}

</style>
