import pandas as pd
import joblib

# 加載模型
btc_model = joblib.load("bitcoin_price_model.pkl")
eth_model = joblib.load("ethereum_price_model.pkl")

# 加載比特幣特徵數據
btc_df = pd.read_csv("bitcoin_features.csv")

# 提取比特幣的最新特徵
btc_last_price = btc_df["price"].iloc[-1]
btc_features = {
    "price_lag_1": btc_last_price,
    "price_lag_2": btc_df["price"].iloc[-2],
    "rolling_mean_5": btc_df["rolling_mean_5"].iloc[-1],
    "rolling_mean_10": btc_df["rolling_mean_10"].iloc[-1],
    "rsi": btc_df["rsi"].iloc[-1],
}
btc_features_df = pd.DataFrame([btc_features])

# 比特幣預測
btc_prediction = btc_model.predict(btc_features_df)
print(f"比特幣未來預測價格: {btc_prediction[0]}")

# 加載以太幣特徵數據
eth_df = pd.read_csv("ethereum_features.csv")

# 提取以太幣的最新特徵
eth_last_price = eth_df["price"].iloc[-1]
eth_features = {
    "price_lag_1": eth_last_price,
    "price_lag_2": eth_df["price"].iloc[-2],
    "rolling_mean_5": eth_df["rolling_mean_5"].iloc[-1],
    "rolling_mean_10": eth_df["rolling_mean_10"].iloc[-1],
    "rsi": eth_df["rsi"].iloc[-1],
}
eth_features_df = pd.DataFrame([eth_features])

# 以太幣預測
eth_prediction = eth_model.predict(eth_features_df)
print(f"以太幣未來預測價格: {eth_prediction[0]}")
