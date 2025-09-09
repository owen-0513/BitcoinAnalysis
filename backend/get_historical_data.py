import requests
import pandas as pd
import os
from datetime import datetime, timedelta

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


def calculate_time_range(filename, days=90):
    """根據當前時間計算需要抓取的時間範圍"""
    end_time = datetime.utcnow()
    if os.path.exists(filename):
        try:
            df = pd.read_csv(filename)
            last_time = pd.to_datetime(df["timestamp"]).max()
            start_time = last_time if pd.notnull(last_time) else end_time - timedelta(days=days)
        except Exception:
            start_time = end_time - timedelta(days=days)
    else:
        start_time = end_time - timedelta(days=days)
    return int(start_time.timestamp()), int(end_time.timestamp())


def update_historical_data(coin, filename, days=90):
    """根據最新時間範圍抓取並更新歷史數據"""
    start_ts, end_ts = calculate_time_range(filename, days)
    API_URL = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart/range"
    params = {
        "vs_currency": "usd",
        "from": start_ts,
        "to": end_ts,
    }

    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        if "prices" in data:
            prices = data["prices"]
            df = pd.DataFrame(prices, columns=["timestamp", "price"])
            df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

            if os.path.exists(filename):
                existing = pd.read_csv(filename)
                combined = pd.concat([existing, df])
                combined.drop_duplicates(subset="timestamp", inplace=True)
                combined.sort_values("timestamp", inplace=True)
                combined.to_csv(filename, index=False)
            else:
                df.to_csv(filename, index=False)
            print(f"{coin.capitalize()} 歷史數據已更新到 '{filename}'")
        else:
            print("未能獲取價格數據，請檢查API返回的數據結構。")
    except requests.exceptions.RequestException as e:
        print(f"請求失敗: {e}")
    except ValueError as ve:
        print(f"JSON 解碼錯誤: {ve}")
    except Exception as e:
        print(f"發生錯誤: {e}")


if __name__ == "__main__":
    update_historical_data("bitcoin", "bitcoin_historical_prices.csv")
    update_historical_data("ethereum", "ethereum_historical_prices.csv")
