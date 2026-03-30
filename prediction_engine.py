import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from data_loader import load_data


# -----------------------------
# Feature Engineering
# -----------------------------
def create_features(series):

    df = pd.DataFrame({"price": series})

    # Lag features (previous prices)
    df["lag1"] = df["price"].shift(1)
    df["lag2"] = df["price"].shift(2)
    df["lag3"] = df["price"].shift(3)

    # Moving average (trend indicator)
    df["ma7"] = df["price"].rolling(7).mean()

    # Volatility (risk indicator)
    df["volatility"] = df["price"].pct_change().rolling(7).std()

    df = df.dropna()

    X = df[["lag1", "lag2", "lag3", "ma7", "volatility"]]
    y = df["price"]

    return X, y


# -----------------------------
# Prediction Function
# -----------------------------
def predict_next_day():

    prices, _ = load_data()

    predictions = []

    for coin in prices.columns:

        series = prices[coin].dropna()

        # Skip if insufficient data
        if len(series) < 15:
            continue

        # Create ML features
        X, y = create_features(series)

        # Train model
        model = RandomForestRegressor(
            n_estimators=200,
            random_state=42
        )

        model.fit(X, y)

        # Evaluate model accuracy
        train_pred = model.predict(X)
        mae = mean_absolute_error(y, train_pred)

        # Prepare latest values for prediction
        last_values = series.tail(7)

        lag1 = last_values.iloc[-1]
        lag2 = last_values.iloc[-2]
        lag3 = last_values.iloc[-3]

        ma7 = last_values.mean()
        volatility = last_values.pct_change().std()

        # Create dataframe for prediction (avoids sklearn warning)
        input_df = pd.DataFrame(
            [[lag1, lag2, lag3, ma7, volatility]],
            columns=["lag1", "lag2", "lag3", "ma7", "volatility"]
        )

        next_price = model.predict(input_df)[0]

        current_price = series.iloc[-1]

        change = ((next_price - current_price) / current_price) * 100

        predictions.append({
            "coin": coin,
            "current_price": round(current_price, 4),
            "predicted_price": round(next_price, 4),
            "expected_change_%": round(change, 2),
            "model_mae": round(mae, 4)
        })

    return pd.DataFrame(predictions)