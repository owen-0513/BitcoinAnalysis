import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# 讀取比特幣和以太坊的特徵數據
btc_df = pd.read_csv("btc_features.csv")  # 修正檔案名稱
eth_df = pd.read_csv("eth_features.csv")  # 修正檔案名稱

# 確認數據是否有缺失值
print("BTC 缺失值檢查:")
print(btc_df.isna().sum())  # 檢查比特幣數據中的缺失值
print("\nETH 缺失值檢查:")
print(eth_df.isna().sum())  # 檢查以太坊數據中的缺失值

# 檢查數據框是否包含所有需要的欄位
print("BTC 欄位名稱:")
print(btc_df.columns)
print("ETH 欄位名稱:")
print(eth_df.columns)

# 填補缺失值（如果有的話）
btc_df.fillna(0, inplace=True)
eth_df.fillna(0, inplace=True)

# 選擇特徵和標籤
X_btc = btc_df[
    ["price_lag_1", "price_lag_2", "rolling_mean_5", "rolling_mean_10", "rsi", "macd", "signal_line", "smc_support", "smc_resistance"]
]
y_btc = btc_df["price"]

X_eth = eth_df[
    ["price_lag_1", "price_lag_2", "rolling_mean_5", "rolling_mean_10", "rsi", "macd", "signal_line", "smc_support", "smc_resistance"]
]
y_eth = eth_df["price"]

# 拆分訓練集和測試集
X_btc_train, X_btc_test, y_btc_train, y_btc_test = train_test_split(
    X_btc, y_btc, test_size=0.2, random_state=42
)
X_eth_train, X_eth_test, y_eth_train, y_eth_test = train_test_split(
    X_eth, y_eth, test_size=0.2, random_state=42
)

# 訓練模型
btc_model = RandomForestRegressor()
btc_model.fit(X_btc_train, y_btc_train)

eth_model = RandomForestRegressor()
eth_model.fit(X_eth_train, y_eth_train)

# 保存模型
joblib.dump(btc_model, "bitcoin_price_model.pkl")
joblib.dump(eth_model, "ethereum_price_model.pkl")

print("比特幣和以太幣的模型已保存")

# 驗證模型
btc_score = btc_model.score(X_btc_test, y_btc_test)
eth_score = eth_model.score(X_eth_test, y_eth_test)

print(f"比特幣模型測試集分數: {btc_score}")
print(f"以太幣模型測試集分數: {eth_score}")
