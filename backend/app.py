from flask import Flask, jsonify
import requests
import pandas as pd
import joblib
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
CORS(app)

model = joblib.load("bitcoin_price_model.pkl")
eth_model = joblib.load("ethereum_price_model.pkl")

def fetch_and_update_data():
    BITCOIN_API_URL = "https://api.coingecko.com/api/v3/coins/markets"
    PARAMS = {
        "vs_currency": "usd",
        "ids": "bitcoin,ethereum",  
        "order": "market_cap_desc",
        "per_page": 2,
        "page": 1,
        "sparkline": False,
    }

    response = requests.get(BITCOIN_API_URL, params=PARAMS)

    if response.status_code == 200:
        data = response.json()
        if len(data) > 0:
            df = pd.DataFrame(data)
            df.to_csv("cryptocurrency_prices.csv", index=False)
            print("比特幣和以太幣資料已更新")
        else:
            print("未能獲取數據")
    else:
        print(f"請求失敗，狀態碼: {response.status_code}")

@app.route("/cryptocurrency", methods=["GET"])
def get_cryptocurrency_data():
    try:
        df = pd.read_csv("cryptocurrency_prices.csv")
        crypto_info = df[["id", "name", "current_price", "market_cap", "total_volume"]].to_dict(orient="records")
        return jsonify(crypto_info)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def calculate_recommendations(last_price):
    buy_price = last_price * 0.98 
    take_profit_price = buy_price * 1.1  
    stop_loss_price = buy_price * 0.95  

    position = "做多" if last_price > buy_price else "做空"

    return {
        "建議買入價格": buy_price,
        "止盈價格": take_profit_price,
        "止損價格": stop_loss_price,
        "交易建議": position
    }

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

        recommendations = calculate_recommendations(last_price)

        return jsonify({
            "predicted_price": prediction[0],
            "recommendations": recommendations
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

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

        recommendations = calculate_recommendations(last_price)

        return jsonify({
            "predicted_price": prediction[0],
            "recommendations": recommendations
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_and_update_data, "interval", minutes=5)
    scheduler.start()
    fetch_and_update_data()  
    app.run(host="0.0.0.0", port=5000, debug=True)

