<template>
    <div class="portfolio">
        <h1>我的作品集</h1>

        <p>點擊以下按鈕，訪問我的 LINE 作品集連結。</p>
        <a href="https://line.me/R/ti/p/@109mjice?from=page&liff.referrer=https%3A%2F%2Fpda.104.com.tw%2F&accountId=109mjice"
            target="_blank" class="btn primary-btn">
            前往作品集
        </a>

        <p>點擊下方按鈕查看，訪問我的比特幣分析作品集連結。</p>
        <router-link to="/bitcoin" class="btn secondary-btn">比特幣分析</router-link>
    </div>
</template>

<script>
export default {
    name: 'ProjectPortfolio',
};
</script>

<style scoped>
.portfolio {
    text-align: center;
    padding: 60px 20px;
    background: linear-gradient(to right, #f6f9fc, #e9f3fa);
    min-height: 100vh;
}

h1 {
    font-size: 36px;
    font-weight: bold;
    margin-bottom: 30px;
    color: #333;
}

p {
    font-size: 18px;
    color: #666;
    margin-bottom: 20px;
}

.btn {
    display: inline-block;
    padding: 15px 50px;
    font-size: 18px;
    border-radius: 10px;
    font-weight: bold;
    text-decoration: none;
    transition: background-color 0.3s, transform 0.2s, box-shadow 0.3s;
    margin-bottom: 30px;
    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
}

.primary-btn {
    background: linear-gradient(to right, #007bff, #00d4ff);
    color: white;
}

.primary-btn:hover {
    background: linear-gradient(to right, #0056b3, #009dd4);
    transform: translateY(-3px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

.secondary-btn {
    background: linear-gradient(to right, #28a745, #34d058);
    color: white;
}

.secondary-btn:hover {
    background: linear-gradient(to right, #218838, #2ebf4f);
    transform: translateY(-3px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}
</style>