<template>
    <nav class="navbar">
        <router-link to="/" class="nav-link">首頁</router-link>
        <router-link to="/about" class="nav-link">關於我</router-link>
        <router-link to="/Portfolio" class="nav-link">作品集</router-link>
    </nav>
</template>

<script>
export default {
    name: 'AppNavbar',
};
</script>

<style scoped>
.navbar {
    background-color: #9da1a5;
    padding: 20px;
    position: fixed;
    top: 0;
    width: 100%;
    text-align: center;
    z-index: 1000;
    border-bottom: none;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.nav-link {
    color: white;
    margin: 0 20px;
    font-size: 18px;
    text-decoration: none;
    font-weight: bold;
}

.nav-link:hover {
    text-decoration: underline;
}

body,
html {
    margin: 0;
    padding: 0;
}
</style>
