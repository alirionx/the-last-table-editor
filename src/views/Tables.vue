<template>
  <div>
    <h3>This is an Tables page</h3>
  </div>
</template>

<script>

export default {
  name: 'Tables',
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
    fetch('/api/test') 
      .then(resp => resp.json())
      .then(resObj => {
        console.log(resObj);
      });
  }

}
</script>

