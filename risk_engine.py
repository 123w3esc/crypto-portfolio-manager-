import pandas as pd
import statistics

def load_data():
    import pandas as pd

    df = pd.read_csv("historical_prices.csv")

    df = df[df["date"] != "Ticker"]
    df["close"] = pd.to_numeric(df["close"], errors="coerce")
    df = df.dropna(subset=["close"])

    grouped = df.groupby("coin_id")

    data = {}

    for coin, group in grouped:
        prices = group["close"].astype(float).tolist()
        data[coin] = prices

    return data

def calculate_daily_returns(prices):
    returns = []
    for i in range(1, len(prices)):
        r = (prices[i] - prices[i-1]) / prices[i-1]
        returns.append(r)
    return returns


def calculate_volatility(returns):
    if len(returns) < 2:
        return 0
    return statistics.stdev(returns)


def determine_risk_category(volatility):
    if volatility < 0.03:
        return "Low"
    elif volatility < 0.05:
        return "Medium"
    else:
        return "High"


def get_coin_metrics(coin_id, prices):

    returns = calculate_daily_returns(prices)

    if len(returns) == 0:
        return {
            "coin_id": coin_id,
            "avg_daily_return": 0,
            "volatility": 0,
            "risk_category": "Low"
        }

    avg_return = sum(returns) / len(returns)
    volatility = calculate_volatility(returns)
    risk = determine_risk_category(volatility)

    return {
        "coin_id": coin_id,
        "avg_daily_return": avg_return,
        "volatility": volatility,
        "risk_category": risk
    }