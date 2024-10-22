from flask import Flask, jsonify
import requests
import pandas as pd
import joblib
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
CORS(app)

# 載入預訓練模型
model = joblib.load("bitcoin_price_model.pkl")
eth_model = joblib.load("ethereum_price_model.pkl")

def fetch_and_update_data():
    """抓取比特幣和以太幣的即時市場數據並保存到本地 CSV 文件"""
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
    """返回比特幣和以太幣的市場數據"""
    try:
        df = pd.read_csv("cryptocurrency_prices.csv")
        crypto_info = df[["id", "name", "current_price", "market_cap", "total_volume"]].to_dict(orient="records")
        return jsonify(crypto_info)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def calculate_recommendations(last_price, rsi, macd, signal_line, smc_support, smc_resistance):
    """根據技術指標生成交易建議"""
    buy_price = last_price * 0.98 
    take_profit_price = buy_price * 1.1  
    stop_loss_price = buy_price * 0.95  

    # 使用 RSI 判斷做多或做空
    if rsi < 30:
        position = "做多 (RSI 指標：超賣)"
    elif rsi > 70:
        position = "做空 (RSI 指標：超買)"
    # 使用 MACD 判斷
    elif macd > signal_line:
        position = "做多 (MACD 黃金交叉)"
    elif macd < signal_line:
        position = "做空 (MACD 死亡交叉)"
    # 使用 SMC 判斷
    elif last_price <= smc_support:
        position = "做多 (接近支撐位)"
    elif last_price >= smc_resistance:
        position = "做空 (接近阻力位)"
    else:
        position = "保持觀望"

    return {
        "建議買入價格": buy_price,
        "止盈價格": take_profit_price,
        "止損價格": stop_loss_price,
        "交易建議": position
    }

@app.route("/predict", methods=["GET"])
def predict():
    """預測比特幣價格並生成交易建議"""
    try:
        df = pd.read_csv("btc_features.csv")

        # 檢查 CSV 文件中的欄位是否存在
        print("CSV 文件中的欄位:", df.columns)

        # 確保沒有空值
        df.fillna(0, inplace=True)

        last_price = df["price"].iloc[-1]
        features = {
            "price_lag_1": last_price,
            "price_lag_2": df["price"].iloc[-2],
            "rolling_mean_5": df["rolling_mean_5"].iloc[-1],
            "rolling_mean_10": df["rolling_mean_10"].iloc[-1],
            "rsi": df["rsi"].iloc[-1],
            "macd": df["macd"].iloc[-1],  # 確保此欄位存在
            "signal_line": df["signal_line"].iloc[-1],  # 確保此欄位存在
            "smc_support": df["smc_support"].iloc[-1],
            "smc_resistance": df["smc_resistance"].iloc[-1],
        }
        features_df = pd.DataFrame([features])
        prediction = model.predict(features_df)

        recommendations = calculate_recommendations(
            last_price,
            features["rsi"],
            features["macd"],
            features["signal_line"],
            features["smc_support"],
            features["smc_resistance"]
        )

        return jsonify({
            "predicted_price": prediction[0],
            "recommendations": recommendations
        })
    except KeyError as e:
        # 如果有欄位不存在，打印具體是哪個欄位缺失
        print(f"KeyError - 缺少的欄位: {e}")
        return jsonify({"error": f"缺少的欄位: {e}"}), 500
    except Exception as e:
        print(f"其他錯誤: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/predict_eth", methods=["GET"])
def predict_eth():
    """預測以太幣價格並生成交易建議"""
    try:
        df = pd.read_csv("eth_features.csv")

        # 確保沒有空值
        df.fillna(0, inplace=True)

        last_price = df["price"].iloc[-1]
        features = {
            "price_lag_1": last_price,
            "price_lag_2": df["price"].iloc[-2],
            "rolling_mean_5": df["rolling_mean_5"].iloc[-1],
            "rolling_mean_10": df["rolling_mean_10"].iloc[-1],
            "rsi": df["rsi"].iloc[-1],
            "macd": df["macd"].iloc[-1],
            "signal_line": df["signal_line"].iloc[-1],
            "smc_support": df["smc_support"].iloc[-1],
            "smc_resistance": df["smc_resistance"].iloc[-1],
        }
        features_df = pd.DataFrame([features])
        prediction = eth_model.predict(features_df)

        recommendations = calculate_recommendations(
            last_price,
            features["rsi"],
            features["macd"],
            features["signal_line"],
            features["smc_support"],
            features["smc_resistance"]
        )

        return jsonify({
            "predicted_price": prediction[0],
            "recommendations": recommendations
        })
    except KeyError as e:
        print(f"KeyError - 缺少的欄位: {e}")
        return jsonify({"error": f"缺少的欄位: {e}"}), 500
    except Exception as e:
        print(f"其他錯誤: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # 定時抓取數據
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_and_update_data, "interval", minutes=5)
    scheduler.start()
    fetch_and_update_data()  
    app.run(host="0.0.0.0", port=5000, debug=True)
