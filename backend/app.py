from flask import Flask, jsonify
import requests
import pandas as pd
import joblib
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
CORS(app)

# 載入模型
model = joblib.load("bitcoin_price_model.pkl")
eth_model = joblib.load("ethereum_price_model.pkl")


# 設定資料更新的時間間隔
def fetch_and_update_data():
    BITCOIN_API_URL = "https://api.coingecko.com/api/v3/coins/markets"
    PARAMS = {
        "vs_currency": "usd",
        "ids": "bitcoin,ethereum",  # 同時抓取 BTC 和 ETH
        "order": "market_cap_desc",
        "per_page": 2,
        "page": 1,
        "sparkline": False,
    }

    response = requests.get(BITCOIN_API_URL, params=PARAMS)

    # 檢查請求是否成功
    if response.status_code == 200:
        data = response.json()

        # 確保我們獲取到正確的數據結構
        if len(data) > 0:
            # 將 BTC 和 ETH 數據儲存到 DataFrame
            df = pd.DataFrame(data)

            # 儲存比特幣和以太幣資料到 CSV 檔案
            df.to_csv("cryptocurrency_prices.csv", index=False)
            print("比特幣和以太幣資料已更新")
        else:
            print("未能獲取數據")
    else:
        print(f"請求失敗，狀態碼: {response.status_code}")


# 這個路由提供加密貨幣的即時數據
@app.route("/cryptocurrency", methods=["GET"])
def get_cryptocurrency_data():
    try:
        df = pd.read_csv("cryptocurrency_prices.csv")
        # 獲取 BTC 和 ETH 的資料
        crypto_info = df[
            ["id", "name", "current_price", "market_cap", "total_volume"]
        ].to_dict(orient="records")
        return jsonify(crypto_info)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# 這個路由提供未來比特幣價格預測
@app.route("/predict", methods=["GET"])
def predict():
    try:
        df = pd.read_csv("bitcoin_features.csv")
        last_price = df["price"].iloc[-1]
        features = {
            "price_lag_1": last_price,
            "price_lag_2": df["price"].iloc[-2],
            "rolling_mean_5": df["rolling_mean_5"].iloc[-1],
            "rolling_mean_10": df["rolling_mean_10"].iloc[-1],
            "rsi": df["rsi"].iloc[-1],
        }
        features_df = pd.DataFrame([features])
        prediction = model.predict(features_df)
        return jsonify({"predicted_price": prediction[0]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# 這個路由提供未來以太幣價格預測
@app.route("/predict_eth", methods=["GET"])
def predict_eth():
    try:
        df = pd.read_csv("ethereum_features.csv")
        last_price = df["price"].iloc[-1]
        features = {
            "price_lag_1": last_price,
            "price_lag_2": df["price"].iloc[-2],
            "rolling_mean_5": df["rolling_mean_5"].iloc[-1],
            "rolling_mean_10": df["rolling_mean_10"].iloc[-1],
            "rsi": df["rsi"].iloc[-1],
        }
        features_df = pd.DataFrame([features])
        prediction = eth_model.predict(features_df)
        return jsonify({"predicted_price": prediction[0]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # 每小時更新數據
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_and_update_data, "interval", hours=1)
    scheduler.start()
    fetch_and_update_data()  # 初始抓取數據
    app.run(host="0.0.0.0", port=5000, debug=True)
