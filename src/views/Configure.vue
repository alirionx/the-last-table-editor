<template>
  <div>
    <h2>This is an Configure page</h2>
  </div>
</template>


<script>

export default {
  name: 'Configure',
  components: {

  },
  data(){
    return {
      name: "Configure"
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