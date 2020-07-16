<template>
  <div id="app">
    <div class="headBlock">
      <!--router-link to="/">Home</router-link-->
      <div css="hl">The - Last - Table - Editor</div>
      <div css="menuBar">
        <div v-for="(elm, idx) in menu" :key="idx" v-on:click="set_hash(elm['lnk'])">{{ elm['txt'] }}</div>
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
      ]
    }
  },
  methods:{
    set_hash(lnk="/"){
      window.location.hash = lnk;
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
  position: absolute;
  left: -8px;
  top: -8px;
  width: 101.5%;
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
</style>
