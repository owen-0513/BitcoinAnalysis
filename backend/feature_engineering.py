import pandas as pd
import requests

def calculate_rsi(series, window):
    """計算相對強弱指標 (RSI)"""
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def calculate_macd(series, short_window=12, long_window=26, signal_window=9):
    """計算移動平均收斂擴散指標 (MACD)"""
    ema_short = series.ewm(span=short_window, adjust=False).mean()
    ema_long = series.ewm(span=long_window, adjust=False).mean()
    macd = ema_short - ema_long
    signal = macd.ewm(span=signal_window, adjust=False).mean()
    return macd, signal, macd - signal

def calculate_smc_support_resistance(df, window=14):
    """計算支撐與阻力位"""
    df['rolling_max'] = df['price'].rolling(window=window).max()
    df['rolling_min'] = df['price'].rolling(window=window).min()
    return df['rolling_max'], df['rolling_min']

def get_current_price(asset_name):
    """從 CoinGecko API 獲取當前價格"""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={asset_name}&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get(asset_name, {}).get("usd", None)
    return None

def calculate_features(df, asset_name):
    """計算指定資產的所有技術指標"""
    if 'price' not in df.columns:
        raise ValueError(f"'{asset_name}' 資料中缺少 'price' 列")
    
    df.dropna(subset=['price'], inplace=True)

    # 計算技術指標
    df["price_change"] = df["price"].pct_change()
    df["rolling_mean_5"] = df["price"].rolling(window=5).mean()
    df["rolling_mean_10"] = df["price"].rolling(window=10).mean()
    df["rsi"] = calculate_rsi(df["price"], window=14)
    df["price_lag_1"] = df["price"].shift(1)
    df["price_lag_2"] = df["price"].shift(2)
    
    # 計算 MACD
    df["macd"], df["signal_line"], _ = calculate_macd(df["price"])
    
    # 計算 SMC 支撐與阻力
    df["smc_resistance"], df["smc_support"] = calculate_smc_support_resistance(df, window=14)

    # 獲取當前價格並添加到數據框中
    df["current_price"] = get_current_price(asset_name.lower())
    
    # 填充 NaN 值
    df.fillna(0, inplace=True)

    # 保存結果
    output_filename = f"{asset_name.lower()}_features.csv"
    df.to_csv(output_filename, index=False)
    print(f"{asset_name} 的特徵數據已保存到 {output_filename}")

def main():
    """主函數：讀取數據並計算特徵"""
    # 讀取數據
    btc_df = pd.read_csv("bitcoin_historical_prices.csv")
    eth_df = pd.read_csv("ethereum_historical_prices.csv")

    # 計算特徵
    calculate_features(btc_df, "BTC")
    calculate_features(eth_df, "ETH")

if __name__ == "__main__":
    main()
