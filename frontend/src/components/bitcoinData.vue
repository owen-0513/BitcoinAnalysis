<template>
  <div class="crypto-data">
    <h1>加密貨幣資訊</h1>
    <div class="tabs">
      <button @click="activeTab = 'btc'" :class="{ active: activeTab === 'btc' }">比特幣資料</button>
      <button @click="activeTab = 'eth'" :class="{ active: activeTab === 'eth' }">以太幣資料</button>
      <button @click="activeTab = 'btc_predict'" :class="{ active: activeTab === 'btc_predict' }">比特幣預測</button>
      <button @click="activeTab = 'eth_predict'" :class="{ active: activeTab === 'eth_predict' }">以太幣預測</button>
    </div>

    <div class="tab-content">
      <div v-if="activeTab === 'btc'">
        <div v-if="bitcoin">
          <p><strong>名稱:</strong> {{ bitcoin.name }}</p>
          <p><strong>價格:</strong> ${{ bitcoin.current_price }}</p>
          <p><strong>市值:</strong> {{ bitcoin.market_cap }}</p>
          <p><strong>交易量:</strong> {{ bitcoin.total_volume }}</p>
        </div>
        <div v-else>
          <p>載入中...</p>
        </div>
      </div>

      <div v-if="activeTab === 'eth'">
        <div v-if="ethereum">
          <p><strong>名稱:</strong> {{ ethereum.name }}</p>
          <p><strong>價格:</strong> ${{ ethereum.current_price }}</p>
          <p><strong>市值:</strong> {{ ethereum.market_cap }}</p>
          <p><strong>交易量:</strong> {{ ethereum.total_volume }}</p>
        </div>
        <div v-else>
          <p>載入中...</p>
        </div>
      </div>

      <div v-if="activeTab === 'btc_predict'">
        <h2>比特幣未來價格預測</h2>
        <div v-if="predictedBtcPrice !== null">
          <p><strong>預測價格:</strong> ${{ predictedBtcPrice }}</p>
        </div>
        <div v-else>
          <p>預測資料載入中...</p>
        </div>
      </div>

      <div v-if="activeTab === 'eth_predict'">
        <h2>以太幣未來價格預測</h2>
        <div v-if="predictedEthPrice !== null">
          <p><strong>預測價格:</strong> ${{ predictedEthPrice }}</p>
        </div>
        <div v-else>
          <p>預測資料載入中...</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CryptoData',
  data() {
    return {
      bitcoin: null,
      ethereum: null,
      predictedBtcPrice: null,
      predictedEthPrice: null,
      activeTab: 'btc',  // 初始顯示比特幣資料
    };
  },
  mounted() {
    this.fetchCryptocurrencyData();
    this.fetchPredictedPrices();
  },
  methods: {
    async fetchCryptocurrencyData() {
      try {
        const response = await axios.get('http://172.20.10.6:5000/cryptocurrency');
        this.bitcoin = response.data.find(coin => coin.id === 'bitcoin');
        this.ethereum = response.data.find(coin => coin.id === 'ethereum');
      } catch (error) {
        console.error("無法獲取加密貨幣資料：", error);
      }
    },
    async fetchPredictedPrices() {
      try {
        const btcResponse = await axios.get('http://172.20.10.6:5000/predict');
        this.predictedBtcPrice = btcResponse.data.predicted_price;

        const ethResponse = await axios.get('http://172.20.10.6:5000/predict_eth');
        this.predictedEthPrice = ethResponse.data.predicted_price;
      } catch (error) {
        console.error("無法獲取預測價格：", error);
      }
    },
  },
};
</script>

<style scoped>
.crypto-data {
  text-align: center;
  margin-top: 50px;
}

.tabs {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.tabs button {
  background-color: #f1f1f1;
  border: none;
  border-radius: 5px;
  color: #333;
  padding: 10px 20px;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s;
  font-size: 16px;
  margin: 0 5px;
}

.tabs button:hover {
  background-color: #e0e0e0;
}

.tabs button.active {
  background-color: #007bff;
  color: white;
  font-weight: bold;
}

.tab-content {
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 20px;
  background-color: #fff;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}
</style>
