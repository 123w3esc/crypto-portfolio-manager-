import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import parallel_risk
import prediction_engine
import invest_mix_cal
from data_loader import load_data

st.set_page_config(page_title="CRYPTO PORTFOLIO DASHBOARD", layout="wide")

st.title(" CRYPTO PORTFOLIO ANALYSIS DASHBOARD")

# Load data
prices, returns = load_data()

# ------------------------------------------------
# Risk Metrics
# ------------------------------------------------
st.header(" RISK METRICS")

metrics = parallel_risk.compute_all_metrics()
metrics_df = pd.DataFrame(metrics)

st.dataframe(metrics_df)

# ------------------------------------------------
# Price Chart
# ------------------------------------------------
st.header(" PRICE HISTORY")

coin = st.selectbox("Select Cryptocurrency", prices.columns)

fig, ax = plt.subplots()
ax.plot(prices.index, prices[coin])
ax.set_title(f"{coin} Price History")
ax.set_xlabel("Date")
ax.set_ylabel("Price")

st.pyplot(fig)

# ------------------------------------------------
# Volatility Chart
# ------------------------------------------------
st.header("VOLATILITY COMPERISION")

vol_df = metrics_df.set_index("coin_id")["volatility"]

st.bar_chart(vol_df)

# ------------------------------------------------
# Risk vs Return Scatter Plot
# ------------------------------------------------
st.header(" Risk vs Return Analysis")

metrics_df["annual_return"] = metrics_df["avg_daily_return"] * 365

fig2, ax2 = plt.subplots()

ax2.scatter(metrics_df["volatility"], metrics_df["annual_return"])

for i, coin in enumerate(metrics_df["coin_id"]):
    ax2.annotate(
        coin,
        (metrics_df["volatility"][i], metrics_df["annual_return"][i])
    )

ax2.set_xlabel("Volatility (Risk)")
ax2.set_ylabel("Annual Return")
ax2.set_title("Risk vs Return Scatter Plot")

st.pyplot(fig2)

# ------------------------------------------------
# Machine Learning Predictions
# ------------------------------------------------
st.header("ML PRICE PRIDICTION ")
predictions = prediction_engine.predict_next_day()

predictions = predictions.sort_values(
    "expected_change_%",
    ascending=False
)

st.dataframe(predictions)

# ------------------------------------------------
# Portfolio Allocation
# ------------------------------------------------
st.header(" Portfolio Allocation")

investment = st.number_input("Total Investment ($)", value=100000)

profile = st.selectbox("Risk Profile", ["Low", "Medium", "High"])

allocation = invest_mix_cal.allocate_portfolio(
    metrics,
    total_investment=investment,
    profile=profile
)

alloc_df = pd.DataFrame(allocation)

st.dataframe(alloc_df)

# ------------------------------------------------
# Top Coins Analysis
# ------------------------------------------------
st.header("Top Coins Analysis")
top_return = metrics_df.sort_values("annual_return", ascending=False).head(3)
top_risk = metrics_df.sort_values("volatility", ascending=False).head(3)

col1, col2 = st.columns(2)

with col1:
    st.subheader(" Top 3 Highest Return Coins")
    st.bar_chart(top_return.set_index("coin_id")["annual_return"])

with col2:
    st.subheader(" Top 3 Riskiest Coins")
    st.bar_chart(top_risk.set_index("coin_id")["volatility"])


st.success("Dashboard Loaded Successfully")
