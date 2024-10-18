<template>
    <div class="home">
        <div class="quote">
            <p>願我們的才能，都閃閃發光，且發揚光大。</p>
            <span class="author">— Owen 曾證蒼</span>
        </div>
    </div>
</template>

<script>
export default {
    name: 'HomePage'
};
</script>

<style scoped>
.home {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background: linear-gradient(to right, #6b16db, #ab47bc);
    text-align: center;
    color: white;
}

.quote p {
    font-size: 32px;
    font-weight: bold;
    margin: 0;
    padding: 0;
}

.author {
    display: block;
    margin-top: 10px;
    font-size: 18px;
    font-style: italic;
    text-align: right;
    width: 100%;
    padding-right: 20px;
}
</style>
