import requests
import pandas as pd
import sqlite3

API_URL = "https://api.coingecko.com/api/v3/coins/markets"

def fetch_market_snapshot():
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 250,
        "page": 1,
    }

    response = requests.get(API_URL, params=params)
    data = response.json()

    records = []
    for coin in data:
        records.append({
            "coin_id": coin["id"],
            "symbol": coin["symbol"],
            "name": coin["name"],
            "current_price": coin["current_price"],
            "market_cap": coin["market_cap"],
            "last_updated": coin["last_updated"],
        })

    return pd.DataFrame(records)


def save_to_csv(df):
    df.to_csv("market_snapshot.csv", index=False)


def save_to_db(df):
    conn = sqlite3.connect("crypto.db")
    df.to_sql("market_snapshot", conn, if_exists="replace", index=False)
    conn.close()


if __name__ == "__main__":
    df = fetch_market_snapshot()
    save_to_csv(df)
    save_to_db(df)
    print("Market snapshot saved.")