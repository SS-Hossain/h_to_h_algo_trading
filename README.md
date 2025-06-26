# 📈 Algo Trading Automation – H To H Internship Assignment

A Python-based mini algo-trading system that:

- Fetches stock data from Yahoo Finance using `yfinance`
- Implements a strategy (RSI < 40 + 20-DMA > 50-DMA)
- Logs buy signals to Google Sheets with timestamp
- Predicts next-day stock movement using a basic ML model
- Supports modular, testable architecture

---

## 🚀 Features

- ✅ Automated backtesting of a technical strategy over 6 months
- ✅ Logs buy signals to Google Sheets with timestamp
- ✅ Uses RSI, SMA indicators from `ta` library
- ✅ Includes a Decision Tree Classifier model for price prediction
- ✅ Clean folder structure, modular code, easy to extend

---

## 🧠 Strategy Logic

A **buy signal** is generated when:
- RSI < 40 *(relaxed for testing/demo)*
- 20-day SMA > 50-day SMA

This ensures we identify **momentum shifts** and potential bullish trends.

---

## 🧪 ML Logic

- Fetches 6 months of data for a selected stock (`TCS.NS`)
- Extracts indicators: RSI, MACD, and Volume
- Trains a Decision Tree Classifier to predict if next-day price will rise
- Prints prediction accuracy at each run

---

## 📂 Folder Structure

```
h_to_h_algo_trading/
├── data/             # Reserved for future data files or exports
├── models/           # Stores trained ML models (e.g., decision_tree_model.pkl)
├── utils/            # Utility scripts (e.g., telegram_alert, Google Sheet logger)
├── strategy.py       # Strategy logic using RSI and SMA indicators
├── ml_model.py       # ML logic to predict next-day price movement
├── main.py           # Entry point to run the full pipeline
├── credentials.json  # Google Sheets API credentials
├── requirements.txt  # Python dependencies
├── README.md         # Project documentation
```

---

## 📊 Google Sheets Logging

Buy signals are logged to a sheet named **`Algo_Trading_Log`**. Each row contains:

- `Timestamp` (e.g., `2025-06-26 15:24:09`)
- `Ticker` (e.g., `RELIANCE.NS`)
- `Signal` (BUY)
- `Price` (rounded 2 decimals)

> ℹ️ Make sure your sheet is shared with the `client_email` inside `credentials.json`.

---

## 🛠️ Setup Instructions

### 1. 📦 Install Dependencies

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 2. 🔑 Set Up Google Sheets API

- Create a service account on Google Cloud Console
- Download `credentials.json`
- Share your Google Sheet with the `client_email` from that file

### 3. ▶️ Run the Script

```bash
python main.py
```

---


---

## 💬 Telegram Alerts

This project includes real-time **Telegram notifications** whenever a buy signal is generated.

### 🔧 Setup Instructions

1. **Create a Telegram bot**
   - Open [@BotFather](https://t.me/BotFather)
   - Create a new bot and copy the **token**

2. **Get your Chat ID**
   - Start a chat with your bot and send any message (e.g., "Hi bot")
   - Open this URL in your browser (replace `YOUR_BOT_TOKEN`):
     ```
     https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates
     ```
   - Look for `"chat": {"id": YOUR_CHAT_ID}` in the JSON

3. **Add to `.env` file**
   ```env
   TELEGRAM_TOKEN=your_telegram_token_id
   TELEGRAM_CHAT_ID=your_telegram_chat_id
   ```


## 📌 Notes

- The strategy currently runs once and backtests over the last 6 months
- You can modify `strategy.py` to change indicators, thresholds, or add SELL logic
- `models/` is reserved for saving ML models in `.pkl` format (not used yet)
- .env improves security for API tokens

---

## 🙌 Author

**SK Shaid Hossain**  
B.Tech (IT), RCCIIT, Kolkata  
📧 Email: skshaidhossain777@gmail.com  
🔗 GitHub: https://github.com/SS-Hossain  
🔗 LinkedIn: https://linkedin.com/in/skshaidhossain

---
