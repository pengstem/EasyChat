<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <p>father get the childrencount:{{childrendata}}</p>
  <HelloWorld msg="Welcome to EasyChat App" 
              count="29" 
              @child-count-change="handler"
              />
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  data() {
    return {
      childrendata: 0
    }
  },
  methods: {
    handler(childrencount) {
      this.childrendata = childrencount;
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
  color: #2c3e50;
  margin-top: 60px;
}
</style>
