<template>
  <div class="portfolio">
    <h1>我的作品集</h1>

    <p>點擊以下按鈕，訪問我的 LINE 作品連結。</p>
    <p>功能基本介紹</p>
    <p>這是line 機器人 套用 gpt-4o api 聊天</p>
    <a
      href="https://line.me/R/ti/p/@109mjice?from=page&liff.referrer=https%3A%2F%2Fpda.104.com.tw%2F&accountId=109mjice"
      target="_blank"
      class="btn primary-btn"
    >
      lineBot連結
    </a>

    <p>點擊下方按鈕查看，訪問我的比特幣分析作品連結。</p>
    <p>功能基本介紹</p>
    <p>這是使用 Python當後端 先去拉出歷史資料 再去做基本的機器學習 判定做多還是做空 並且算出止盈止損點位</p>
    <p>用Vue當前端 去渲染畫面</p>
    <p>使用SMC分析比特比與以太坊</p>

    <router-link to="/bitcoin" class="btn secondary-btn">SMC虛擬貨幣分析</router-link>
  </div>
</template>

<script>
export default {
  name: "ProjectPortfolio",
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
