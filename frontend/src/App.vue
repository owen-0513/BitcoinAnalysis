<template>
  <div id="app">
    <AppNavbar />
    <div class="main-content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import AppNavbar from './components/AppNavbar.vue';

export default {
  name: 'App',
  components: {
    AppNavbar,
  },
};
</script>

<style scoped>
#app {
  margin: 0;
  padding: 0;
}

.main-content {
  margin-top: 80px;
  padding: 20px;
  background-color: #f6f9fc;
}

body,
html {
  margin: 0;
  padding: 0;
}
</style>
