import requests
import pandas as pd


def fetch_historical_data(coin, filename):
    """抓取指定加密貨幣的歷史數據並保存到CSV文件"""
    API_URL = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart"
    params = {
        "vs_currency": "usd",
        "days": "30",  # 取最近30天的數據
        "interval": "daily",
    }

    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # 檢查請求是否成功
        data = response.json()

        # 確保數據結構正確
        if "prices" in data:
            prices = data["prices"]
            df = pd.DataFrame(prices, columns=["timestamp", "price"])
            df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

            # 儲存到 CSV
            df.to_csv(filename, index=False)
            print(f"{coin.capitalize()} 歷史數據已保存到 '{filename}'")
        else:
            print("未能獲取價格數據，請檢查API返回的數據結構。")
    except requests.exceptions.RequestException as e:
        print(f"請求失敗: {e}")
    except Exception as e:
        print(f"發生錯誤: {e}")


if __name__ == "__main__":
    fetch_historical_data("bitcoin", "bitcoin_historical_prices.csv")
    fetch_historical_data("ethereum", "ethereum_historical_prices.csv")
