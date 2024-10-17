<template>
  <div id="app">
    <img alt="Bitcoin" src="./assets/logo.png" class="bitcoin-image">
    <HelloWorld msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
import HelloWorld from './components/bitcoinData.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
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
  padding: 20px;
  /* 增加內邊距 */
  background-color: #f9f9f9;
  /* 背景顏色 */
  border-radius: 10px;
  /* 圓角邊框 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  /* 添加陰影 */
}

.bitcoin-image {
  max-width: 300px;
  height: auto;
  margin: 20px auto;
  display: block;
  border: 2px solid #007bff;
  /* 增加邊框 */
  border-radius: 10px;
  /* 圓角邊框 */
}
</style>
