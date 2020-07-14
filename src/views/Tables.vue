<template>
  <div>
    <h2>This is an Tables page</h2>
  </div>
</template>

<script>

export default {
  name: 'Tables',
  components: {

  },
  data(){
    return {
      name: "Tables"
    }
  },
  mounted: function(){
    fetch('/api/test') 
      .then(resp => resp.json())
      .then(data => {
        console.log(data);
      });
  }

}
</script>

