<template>
  <div v-if="idx!=menu" class="menuBtnFrame" v-on:click="callback(idx)">
    <div></div>
    <div></div>
    <div></div>
  </div>
  <div v-else class="menuBtnActive" v-on:click="callback()" ></div>
</template>

<script>
export default {
  name: 'MenuBtn',
  props: {
    idx: Number,
    menu: "",
    callback: Function
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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
  margin: -4px auto -4px auto;
  width: 0;
  height: 0;
  border-top: 8px solid transparent;
  border-left: 18px solid #444;
  border-bottom: 8px solid transparent;
}
</style>
