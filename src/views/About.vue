<template>
  <div>
    <h2>This is an About page</h2>
  </div>
</template>


<script>

export default {
  name: 'About',
  components: {

  },
  data(){
    return {
      name: "test"
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