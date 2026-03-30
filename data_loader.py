import pandas as pd

def load_data():
    df = pd.read_csv("historical_prices.csv")

    df["date"] = pd.to_datetime(df["date"])
    df["close"] = pd.to_numeric(df["close"], errors="coerce")

    df = df.dropna(subset=["close"])

    pivot = df.pivot(index="date", columns="coin_id", values="close")
    pivot = pivot.sort_index()

    returns = pivot.pct_change().dropna()

    return pivot, returns