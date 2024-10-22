import requests
import pandas as pd
import os

def fetch_historical_data(coin, filename, days="90"):
    """抓取指定加密貨幣的歷史數據並保存到CSV文件"""
    API_URL = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart"
    params = {
        "vs_currency": "usd",
        "days": days,  # 可以抓取更長時間的數據，例如90天、180天等
        "interval": "daily",
    }

    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # 檢查是否有 HTTP 錯誤

        # 檢查返回的 JSON 結構是否有 'prices' 鍵
        data = response.json()
        if "prices" in data:
            prices = data["prices"]
            df = pd.DataFrame(prices, columns=["timestamp", "price"])

            # 將 timestamp 轉換為可讀日期
            df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

            # 檢查文件是否已經存在
            if os.path.exists(filename):
                print(f"警告: '{filename}' 文件已存在，將被覆蓋。")

            # 保存為 CSV 文件
            df.to_csv(filename, index=False)
            print(f"{coin.capitalize()} 歷史數據已保存到 '{filename}'")
        else:
            print("未能獲取價格數據，請檢查API返回的數據結構。")
    except requests.exceptions.RequestException as e:
        print(f"請求失敗: {e}")
    except ValueError as ve:
        print(f"JSON 解碼錯誤: {ve}")
    except Exception as e:
        print(f"發生錯誤: {e}")

# 示例使用
fetch_historical_data("bitcoin", "bitcoin_historical_prices.csv", days="90")
fetch_historical_data("ethereum", "ethereum_historical_prices.csv", days="90")
