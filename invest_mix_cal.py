def allocate_portfolio(metrics, total_investment, profile="Medium"):

    if not metrics:
        raise ValueError("Metrics list is empty. Run risk engine first.")

    profiles = {
        "Low": {"Low":0.6, "Medium":0.3, "High":0.1},
        "Medium": {"Low":0.4, "Medium":0.4, "High":0.2},
        "High": {"Low":0.2, "Medium":0.4, "High":0.4},
    }

    allocation = profiles.get(profile)

    if allocation is None:
        raise ValueError("Invalid profile. Choose from Low, Medium, High")

    grouped = {"Low":[], "Medium":[], "High":[]}

    for m in metrics:
        grouped[m["risk_category"]].append(m)

    result = []

    for category, coins in grouped.items():

        if coins:

            budget = total_investment * allocation[category]
            per_coin = budget / len(coins)

            for coin in coins:
                result.append({
                    "coin_id": coin["coin_id"],
                    "investment": per_coin,
                    "expected_return": coin["avg_daily_return"],
                    "volatility": coin["volatility"]
                })

    return result