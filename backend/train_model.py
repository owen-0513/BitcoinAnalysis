import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

btc_df = pd.read_csv("bitcoin_features.csv")
eth_df = pd.read_csv("ethereum_features.csv")  

X_btc = btc_df[
    ["price_lag_1", "price_lag_2", "rolling_mean_5", "rolling_mean_10", "rsi"]
]
y_btc = btc_df["price"]

X_eth = eth_df[
    ["price_lag_1", "price_lag_2", "rolling_mean_5", "rolling_mean_10", "rsi"]
]
y_eth = eth_df["price"]

X_btc_train, X_btc_test, y_btc_train, y_btc_test = train_test_split(
    X_btc, y_btc, test_size=0.2, random_state=42
)
X_eth_train, X_eth_test, y_eth_train, y_eth_test = train_test_split(
    X_eth, y_eth, test_size=0.2, random_state=42
)

btc_model = RandomForestRegressor()
btc_model.fit(X_btc_train, y_btc_train)
eth_model = RandomForestRegressor()
eth_model.fit(X_eth_train, y_eth_train)

joblib.dump(btc_model, "bitcoin_price_model.pkl")
joblib.dump(eth_model, "ethereum_price_model.pkl")
print("比特幣和以太幣的模型已保存")
