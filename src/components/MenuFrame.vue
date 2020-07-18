<template>
  <div class="menuFrame" >
    <div 
      v-for="(act, idx) in actionObj[type]" :key=idx 
      v-on:click="action_fw(act)" 
    >{{ act }}</div>
  </div>
</template>

<script>
export default {
  name: 'MenuBtn',
  props: {
    id: Number,
    type: String,
    callback: Function
  },
  data(){
    return{
      actionObj: {
        "configure": [ "edit", "define", "delete" ],
        "table": [ "edit", "delete" ],
      }
    }
  },
  methods:{
    action_fw(act){
      console.log(act + ": " + this.id);
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.menuFrame{
  position: absolute;
  left: 46px;
  top: 4px;
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
