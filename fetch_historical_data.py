import yfinance as yf
import pandas as pd

symbol_map = {
    "bitcoin": "BTC-USD",
    "ethereum": "ETH-USD",
    "binancecoin": "BNB-USD",
    "solana": "SOL-USD",
    "ripple": "XRP-USD",
    "cardano": "ADA-USD",
    "dogecoin": "DOGE-USD",
    "polkadot": "DOT-USD",
    "litecoin": "LTC-USD",
    "tron": "TRX-USD"
}

all_rows = []

for coin_id, symbol in symbol_map.items():
    print(f"Fetching {coin_id}...")

    data = yf.download(symbol, period="1y", interval="1d", progress=False)

    if data.empty:
        print(f"No data for {coin_id}")
        continue

    # 🔥 FIX MULTIINDEX PROBLEM
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data = data.reset_index()

    for _, row in data.iterrows():
        all_rows.append({
            "coin_id": coin_id,
            "date": row["Date"],
            "open": row["Open"],
            "high": row["High"],
            "low": row["Low"],
            "close": row["Close"],
            "volume": row["Volume"]
        })

df = pd.DataFrame(all_rows)

df.to_csv("historical_prices.csv", index=False)

print("✅ Historical data saved correctly.")