<template>
  <div class="crypto-data">
    <h1>加密貨幣資訊</h1>

    <img
      v-if="cryptoImage"
      :src="cryptoImage"
      alt="Cryptocurrency"
      class="crypto-image"
    />

    <div class="tabs">
      <button
        @click="updateTab('btc')"
        :class="{ active: activeTab === 'btc' }"
      >
        比特幣資料
      </button>
      <button
        @click="updateTab('eth')"
        :class="{ active: activeTab === 'eth' }"
      >
        以太幣資料
      </button>
      <button
        @click="updateTab('btc_predict')"
        :class="{ active: activeTab === 'btc_predict' }"
      >
        比特幣預測
      </button>
      <button
        @click="updateTab('eth_predict')"
        :class="{ active: activeTab === 'eth_predict' }"
      >
        以太幣預測
      </button>
    </div>

    <div class="tab-content">
      <div v-if="activeTab === 'btc'">
        <div class="data-section" v-if="bitcoin">
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
        <div class="data-section" v-if="ethereum">
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
        <div class="data-section" v-if="predictedBtcPrice !== null">
          <p><strong>預測價格:</strong> ${{ predictedBtcPrice }}</p>
          <p>
            <strong>建議買入價格:</strong> ${{
              recommendations["建議買入價格"]
            }}
          </p>
          <p><strong>止盈價格:</strong> ${{ recommendations["止盈價格"] }}</p>
          <p><strong>止損價格:</strong> ${{ recommendations["止損價格"] }}</p>
          <p><strong>交易建議:</strong> {{ recommendations["交易建議"] }}</p>
          <p><strong>預測生成時間:</strong> {{ predictionTime }}</p>
          <p class="risk-warning">風險提示：本預測僅供參考，實際交易需謹慎。</p>
        </div>
        <div v-else>
          <p>預測資料載入中...</p>
        </div>
      </div>

      <div v-if="activeTab === 'eth_predict'">
        <h2>以太幣未來價格預測</h2>
        <div class="data-section" v-if="predictedEthPrice !== null">
          <p><strong>預測價格:</strong> ${{ predictedEthPrice }}</p>
          <p>
            <strong>建議買入價格:</strong> ${{
              ethRecommendations["建議買入價格"]
            }}
          </p>
          <p>
            <strong>止盈價格:</strong> ${{ ethRecommendations["止盈價格"] }}
          </p>
          <p>
            <strong>止損價格:</strong> ${{ ethRecommendations["止損價格"] }}
          </p>
          <p><strong>交易建議:</strong> {{ ethRecommendations["交易建議"] }}</p>
          <p><strong>預測生成時間:</strong> {{ predictionTime }}</p>
          <p class="risk-warning">風險提示：本預測僅供參考，實際交易需謹慎。</p>
        </div>
        <div v-else>
          <p>預測資料載入中...</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      activeTab: "btc",
      bitcoin: null,
      ethereum: null,
      predictedBtcPrice: null,
      predictedEthPrice: null,
      recommendations: {},
      ethRecommendations: {},
      predictionTime: null, // 新增預測生成時間
    };
  },
  mounted() {
    this.fetchCryptocurrencyData();
    this.fetchPredictedPrices();
  },
  computed: {
    cryptoImage() {
      if (this.activeTab === "btc" || this.activeTab === "btc_predict") {
        return require("@/assets/bitcoin.png");
      } else if (this.activeTab === "eth" || this.activeTab === "eth_predict") {
        return require("@/assets/eth.png");
      } else {
        return null;
      }
    },
  },
  methods: {
    async fetchCryptocurrencyData() {
      try {
        const response = await axios.get(
          "https://bitcoinanalysis.onrender.com/cryptocurrency"
        );
        // const response = await axios.get(
        //   "http://192.168.1.125:5000/cryptocurrency"
        // );
        this.bitcoin = response.data.find((coin) => coin.id === "bitcoin");
        this.ethereum = response.data.find((coin) => coin.id === "ethereum");
      } catch (error) {
        console.error("無法獲取加密貨幣資料：", error);
      }
    },
    async fetchPredictedPrices() {
      try {
        const btcResponse = await axios.get(
          "https://bitcoinanalysis.onrender.com/predict"
        );
        // const btcResponse = await axios.get(
        //   "http://192.168.1.125:5000/predict"
        // );
        this.predictedBtcPrice = btcResponse.data.predicted_price;
        this.recommendations = btcResponse.data.recommendations;
        this.predictionTime = new Date().toLocaleString(); // 設定預測生成時間

        const ethResponse = await axios.get(
          "https://bitcoinanalysis.onrender.com/predict_eth"
        );
        // const ethResponse = await axios.get(
        //   "http://192.168.1.125:5000/predict_eth"
        // );
        this.predictedEthPrice = ethResponse.data.predicted_price;
        this.ethRecommendations = ethResponse.data.recommendations;
      } catch (error) {
        console.error("無法獲取預測價格：", error);
      }
    },
    updateTab(tab) {
      this.activeTab = tab;
      console.log("Active Tab:", this.activeTab);
    },
  },
};
</script>

<style scoped>
.crypto-data {
  text-align: center;
  margin-top: 50px;
}

.crypto-image {
  max-width: 250px;
  margin-bottom: 30px;
  display: block;
  margin-left: auto;
  margin-right: auto;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.tabs {
  margin-bottom: 30px;
}

.tabs button {
  background-color: #f1f1f1;
  border: 2px solid #007bff;
  border-radius: 25px;
  padding: 10px 20px;
  margin: 0 10px;
  font-size: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.tabs button.active {
  background-color: #007bff;
  color: #fff;
  font-weight: bold;
}

.tabs button:hover {
  background-color: #0056b3;
  color: white;
  transform: translateY(-2px);
}

.data-section {
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 600px;
  margin: 20px auto;
}

.data-section p {
  font-size: 18px;
  line-height: 1.6;
}

h1 {
  font-size: 28px;
  margin-bottom: 20px;
}

h2 {
  font-size: 24px;
  margin-bottom: 15px;
}

.risk-warning {
  color: red;
  font-weight: bold;
}
</style>
