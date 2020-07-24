<template>
  <div id="app">
    <div class="headBlock">
      <!--router-link to="/">Home</router-link-->
      <div css="hl">The - Last - Table - Editor</div>
      <div css="menuBar">
        <div 
          v-for="(elm, idx) in menu" :key="idx" 
          v-on:click="set_hash(elm['lnk'])" 
          v-bind:style="chk_active(elm['lnk'])" 
        >{{ elm['txt'] }}</div>
      </div>
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: "App",
  data(){
    return{
      menu: [
        {
          "txt": "Tables",
          "lnk": "/"
        },
        {
          "txt": "Configure",
          "lnk": "/config"
        },
        {
          "txt": "About",
          "lnk": "/about"
        }
      ],
      active: String,

    }
  },
  methods:{
    set_hash(lnk="/"){
      window.location.hash = lnk;
      this.active = lnk;
      //console.log(this.active);
    },
    chk_active(lnk){
      if (window.location.hash === "#"+lnk){
        return { textDecoration: 'underline' };
      }
      else{
        return {};
      }
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  padding-top: 100px;
}

#app{
  position: relative;
}
.headBlock{
  position: fixed;
  left: 0px;
  top: 0px;
  width: 100%;
  height: 90px;
  background-color: #2c3e50;
  text-align: center;
  color: #fff;
}
.headBlock div[css=hl]{
  font-size: 22px;
  padding: 34px;
  font-weight: 500;
  display:inline-block;
  *background-color: #35485c;
}
.headBlock div[css=menuBar]{
  position:absolute;
  right:0.5%;
  bottom: 2px;
  min-width: 100px;
}
.headBlock div[css=menuBar] div{
  display:inline-block;
  padding:2px;
  min-width: 100px;
  font-size: 14px;
  font-weight: 500;
  border-right: 1.5px solid #fff;
  background-color: #2c3e50;
  cursor: pointer;
  transition: background-color 0.5s;
}
.headBlock div[css=menuBar] div:hover{
  background-color: #576c83;
}
.headBlock div[css=menuBar] div:last-child{
  border-right: none;
}

table[css=std]{
  min-width: 600px;
  margin: 30px auto 20px auto;
  font-size: 16px;
}
table[css=std] th {
  padding:8px;
  background-color: #333;
  color: #fff;
  font-weight: bold;
}
table[css=std] td {
  padding:8px;
  background-color: #fff;
  color: #000;
  border: 1px solid #777;
}
table[css=std] td:last-child {
  text-align: center;
  width: 20px;
  position:relative;
}
.mainBtn{
  padding: 4px;
  min-width: 100px;
  margin:auto;
  border: 1px solid #000;
  border-radius: 4px;
  background-color: #444;
  color: #fff;
  text-align: center;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.5s;
}
.mainBtn:hover{
  background-color: #111;
}
.blocker{
  position:absolute;
  left: 0px;
  top: 0px;
  width: 100%;
  height: 80vh;
  background-color: rgba(255,255,255, 0.8);
  text-align: center;
  z-index: 2;
}
.actionForm{
  display:inline-block;
  margin: auto;
  padding:1.5%;
  min-width: 600px;
  min-height: 80px;
  background-color: #fafafa;
  border: 1px solid #666;
  border-radius: 8px;
  box-shadow: 1px 10px 20px #444;
  font-size: 14px;
  *opacity: 0.5;
}
.actionForm div[css=hl]{
  width: 97%;
  padding:1.5%;
  margin: auto auto 14px auto;
  border-radius: 4px;
  background-color:#333;
  color: #fff;
  font-weight: bold;
  text-align: center;
}
.actionForm div[css=iptHl]{
  text-align: left;
  margin: 12px auto 4px 10px;
  color: #000;
  font-weight: bold;
  *text-decoration: underline;
}
.actionForm button{
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
.actionForm button:hover{
  background-color: #111;
}
.actionForm input[type=text]{
  width: 94%;
  margin: auto auto 14px auto;
  padding: 1.5%;
  text-align: left;
  border: 0.5px solid #aaa;
  background-color: #fff;
  box-shadow: 0px 1px 3px #aaa;
  transition: background-color 0.5s;
}
.actionForm input[type=text]:focus{
  background-color: rgb(232, 241, 255);
}
.actionForm input:disabled{
  background-color: #eee;
}
</style>
