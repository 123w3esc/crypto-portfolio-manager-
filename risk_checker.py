import pandas as pd
import numpy as np
from datetime import datetime
from data_loader import load_data

def load_returns():
    import pandas as pd

    df = pd.read_csv("historical_prices.csv")

    # 🔥 Remove bad header rows like "Ticker"
    df = df[df["date"] != "Ticker"]

    # 🔥 Convert date safely
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # 🔥 Convert close to numeric safely
    df["close"] = pd.to_numeric(df["close"], errors="coerce")

    # 🔥 Drop invalid rows
    df = df.dropna(subset=["date", "close"])

    # 🔥 Pivot properly
    pivot = df.pivot(index="date", columns="coin_id", values="close")
    pivot = pivot.sort_index()

    # 🔥 Ensure numeric type everywhere
    pivot = pivot.astype(float)

    returns = pivot.pct_change().dropna()

    return pivot, returns


def classify_risk(volatility):
    if volatility < 0.03:
        return "Low"
    elif volatility < 0.06:
        return "Medium"
    else:
        return "High"


def generate_risk_report():

    prices, returns = load_data()   # ✅ FIX HERE

    if returns.empty:
        raise ValueError("No return data found.")

    report = []

    for coin in returns.columns:

        avg_return = returns[coin].mean()
        volatility = returns[coin].std()
        latest_return = returns[coin].iloc[-1]

        risk_level = classify_risk(volatility)

        crash_flag = latest_return < -0.07
        spike_flag = latest_return > 0.07

        report.append({
            "coin": coin,
            "avg_daily_return": round(avg_return, 5),
            "volatility": round(volatility, 5),
            "risk_level": risk_level,
            "latest_daily_return": round(latest_return, 5),
            "daily_crash": crash_flag,
            "daily_spike": spike_flag
        })

    return pd.DataFrame(report)

def save_csv_report(report_df):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"risk_report_{timestamp}.csv"

    report_df.to_csv(filename, index=False)
    print(f"CSV Report Saved: {filename}")