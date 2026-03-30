# 🚀 Crypto Analytics & Risk Management System

A comprehensive Python-based system for analyzing cryptocurrency markets, predicting prices, and managing investment risks.
This project automates real-time data collection using the CoinGecko API, performs risk analysis, generates predictions, and produces detailed reports.

---

## 📌 Features

* 📥 Real-time crypto data collection using CoinGecko API
* 📊 Market snapshot and historical data analysis
* 🤖 Price prediction using machine learning
* ⚠️ Risk analysis and scoring system
* 📉 Portfolio risk evaluation
* 📧 Email alerts for critical updates
* 📑 Automated report generation (CSV format)
* ⚡ Parallel processing for faster computations

---

## 🛠️ Tech Stack

* Python 🐍
* Pandas & NumPy
* Scikit-learn (Machine Learning)
* SQLite (crypto.db)
* CoinGecko API 🌐
* Multithreading / Parallel Processing

---

## 📂 Project Structure

```
CRYPTO PROJECT/
│
├── collect_data.py          # Collects live crypto data (CoinGecko API)
├── fetch_historical_data.py # Fetches historical market data
├── data_loader.py           # Loads and preprocesses data
├── dashboard.py             # Displays insights / summaries
│
├── prediction_engine.py     # ML model for price prediction
├── risk_engine.py           # Core risk calculation logic
├── risk_checker.py          # Validates risk conditions
├── parallel_risk.py         # Parallel risk execution
├── parallel_tasks.py        # Handles multithreading tasks
│
├── invest_mix_cal.py        # Investment allocation logic
├── report_generator.py      # Generates CSV reports
├── email_alerts.py          # Sends email notifications
│
├── crypto.db                # SQLite database
├── historical_prices.csv    # Historical dataset
├── market_snapshot.csv      # Market snapshot data
├── prediction_report_*.csv  # Prediction outputs
├── risk_report_*.csv        # Risk reports
│
├── eda.ipynb                # Data analysis notebook
├── test.py                  # Testing script
```

---


## ▶️ How to Run

1. Collect live data:

```
python collect_data.py
```

2. Fetch historical data:

```
python fetch_historical_data.py
```

3. Run prediction engine:

```
python prediction_engine.py
```

4. Perform risk analysis:

```
python risk_engine.py
```

5. Generate reports:

```
python report_generator.py
```

---

## 🌐 CoinGecko API Integration

This project uses the CoinGecko API to:

* Fetch real-time cryptocurrency prices
* Retrieve historical market data
* Analyze market trends

No API key is required for basic usage.

---

## 📊 How It Works

1. Data is fetched from CoinGecko API and stored in `crypto.db`
2. Historical data is processed for feature engineering
3. Machine learning model predicts future prices
4. Risk engine evaluates volatility and investment safety
5. Reports are generated in CSV format
6. Alerts are sent for high-risk conditions

---

## 🤖 Machine Learning

* Model Used: Random Forest Regressor
* Input Features:

  * Historical prices (lag features)
  * Market trends
* Output:

  * Predicted cryptocurrency prices

---

## ⚠️ Risk Management

The system evaluates:

* Market volatility
* Risk score for each cryptocurrency
* Investment exposure

---

## 📧 Alerts System

* Sends email notifications for:

  * High-risk assets
  * Prediction updates
  * Important market changes

---

## 📈 Output

* 📊 Prediction Reports
* ⚠️ Risk Reports
* 📉 Market Snapshots

(All outputs are saved as `.csv` files)

---

## 👨‍💻 Author

* Yash Gujarathi

---

## 📜 License

This project is developed for educational and learning purposes.

---
