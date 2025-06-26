from utils.telegram_alert import send_telegram_alert
import yfinance as yf
import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import SMAIndicator
from utils.sheet_logger import log_to_sheet
from datetime import datetime
from utils.telegram_alert import send_telegram_alert

def run_strategy():
    send_telegram_alert("🚀 Strategy is working. This is a test alert.")

    tickers = [
        'RELIANCE.NS', 'TCS.NS', 'INFY.NS', 'HDFCBANK.NS',
        'ITC.NS', 'SBIN.NS', 'AXISBANK.NS', 'WIPRO.NS',
        'LT.NS', 'ICICIBANK.NS'
    ]

    for ticker in tickers:
        print(f"\n📊 Processing: {ticker}")
        df = yf.download(ticker, period='6mo', interval='1d', auto_adjust=True, progress=False)

        if df.empty or 'Close' not in df:
            print(f"⚠️ Skipped {ticker}: No data.")
            continue

        close_series = pd.Series(df['Close'].values.flatten(), index=df.index)

        # Indicators
        df['RSI'] = RSIIndicator(close=close_series).rsi()
        df['SMA20'] = SMAIndicator(close=close_series, window=20).sma_indicator()
        df['SMA50'] = SMAIndicator(close=close_series, window=50).sma_indicator()

        # Buy condition
        df['Buy'] = (
            (df['RSI'] < 40) &  # Relaxed from 30 for testing
            (df['SMA20'] > df['SMA50'])  # Trend confirmation
        )

        df.dropna(inplace=True)
        buy_signals = df[df['Buy'] == True]

        if not buy_signals.empty:
            print(f"✅ {len(buy_signals)} Buy Signal(s) found for {ticker}")
            for date, row in buy_signals.iterrows():
                close_price = float(row['Close'].iloc[0] if hasattr(row['Close'], 'iloc') else row['Close'])
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_to_sheet(
                    ticker=ticker,
                    date=str(date.date()),
                    price=round(close_price, 2),
                    signal='BUY',
                    timestamp=timestamp
                )
                send_telegram_alert(
                    f"*📈 BUY ALERT*\n\n*Ticker:* `{ticker}`\n*Date:* `{date.date()}`\n*Price:* ₹{close_price:.2f}"
                )
                print(f"🟢 Logged: {date.date()} - ₹{close_price:.2f}")
        else:
            print(f"❌ No Buy Signals found for {ticker} in last 6 months.")
