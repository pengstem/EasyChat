<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h3>what comes from my father:{{ count }}</h3>
    <button @click="handler">button</button>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String,
    count:{
      type:[Number,String],
      default:0,
      required:true
    }
  },
  data() {
    return {
      childrencount: 0
    }
  },
  methods: {
    handler() {
      this.childrencount++;
      this.$emit('child-count-change', this.childrencount);
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.hello {
  background-color: #09b187;
  color: #12374e;
  font-weight: bold;
  font-size: 2em;
}
</style>
