<template>
  <div>
    <h3>This is an Configure page</h3>
    <table css="std">
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
          <td>
            <button>x</button>
          </td>
        </tr>
      </tbody>
    </table>

  </div>
</template>

<script>

export default {
  name: 'Configure',
  components: {

  },
  data(){
    return {
      name: "Tables",
      defi: [],
      data: []
    }
  },
  mounted: function(){
    fetch('/api/config/get') 
      .then(resp => resp.json())
      .then(resObj => {
        console.log(resObj);
        this.defi = resObj.data.defi;
        this.data = resObj.data.data;
      });
  }

}
</script>

