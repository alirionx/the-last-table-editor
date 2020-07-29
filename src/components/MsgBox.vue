<template>
  <div class="blocker">
    <div class="msgBox">
      <div css="hl">System Message</div>
      <div css="msg">{{msg}}</div>
      <div v-if="confirm != undefined">
        <button v-on:click="callback(); confirm()">ok</button>
        <button v-on:click="callback">cancel</button>
      </div>
      <button v-else v-on:click="callback">ok</button>
    </div>  
  </div>
</template>

<script>
export default {
  name: 'MsgBox',
  props:{
    msg: String,
    callback: Function,
    confirm: Function
  },
  data(){
    return {
      name: "MsgBox"
    }
  },
  methods:{
  
  }
}
</script>


<style scoped>
.msgBox{
  display:inline-block;
  margin: 40px auto auto auto;
  padding:1.5%;
  min-width: 500px;
  min-height: 80px;
  background-color: #fafafa;
  border: 1px solid #666;
  border-radius: 8px;
  box-shadow: 1px 10px 20px #444;
  font-size: 14px;
}
.msgBox div[css=hl]{
  width: 97%;
  padding:1.5%;
  margin: auto auto 14px auto;
  border-radius: 4px;
  background-color:#333;
  color: #fff;
  font-weight: bold;
  text-align: center;
}
.msgBox div[css=msg]{
  width: 92%;
  min-height: 30px;
  padding:3%;
  margin: auto auto 14px auto;
  border-radius: 4px;
  border: 0.5px solid #999;
  background-color:#f6f6f6;
  color: #000;
  font-size: 16px;
  text-align: center;
}
.msgBox button{
  padding: 6px;
  min-width: 120px;
  margin:12px;
  border: 1px solid #000;
  border-radius: 4px;
  background-color: #444;
  color: #fff;
  text-align: center;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.5s;
}
.msgBox button:hover{
  background-color: #111;
}
</style>
