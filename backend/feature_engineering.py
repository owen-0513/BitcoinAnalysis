import pandas as pd


def calculate_rsi(series, window):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

try:
    btc_df = pd.read_csv("bitcoin_historical_prices.csv")
    eth_df = pd.read_csv("ethereum_historical_prices.csv")
except FileNotFoundError as e:
    print(f"文件未找到: {e}")
    exit()

btc_df["price_change"] = btc_df["price"].pct_change()
btc_df["rolling_mean_5"] = btc_df["price"].rolling(window=5).mean()
btc_df["rolling_mean_10"] = btc_df["price"].rolling(window=10).mean()
btc_df["rsi"] = calculate_rsi(btc_df["price"], window=14)
btc_df["price_lag_1"] = btc_df["price"].shift(1)
btc_df["price_lag_2"] = btc_df["price"].shift(2)

eth_df["price_change"] = eth_df["price"].pct_change()
eth_df["rolling_mean_5"] = eth_df["price"].rolling(window=5).mean()
eth_df["rolling_mean_10"] = eth_df["price"].rolling(window=10).mean()
eth_df["rsi"] = calculate_rsi(eth_df["price"], window=14)
eth_df["price_lag_1"] = eth_df["price"].shift(1)
eth_df["price_lag_2"] = eth_df["price"].shift(2)

btc_df.dropna(inplace=True)
eth_df.dropna(inplace=True)

btc_df.to_csv("bitcoin_features.csv", index=False)
eth_df.to_csv("ethereum_features.csv", index=False)
print("比特幣和以太幣的特徵數據已保存")
