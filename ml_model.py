import yfinance as yf
import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import MACD
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

# Ensure models/ folder exists
os.makedirs("models", exist_ok=True)

def run_ml_model():
    ticker = 'TCS.NS'
    df = yf.download(ticker, period='6mo', interval='1d')

    # ✅ FIX: Ensure Close is a 1D series
    close_series = pd.Series(df['Close'].values.flatten(), index=df.index)

    # Indicators
    df['RSI'] = RSIIndicator(close=close_series).rsi()
    macd = MACD(close=close_series)
    df['MACD'] = macd.macd()
    df['Volume'] = df['Volume']

    # Label: 1 if price goes up tomorrow, else 0
    df['Target'] = (close_series.shift(-1) > close_series).astype(int)
    df.dropna(inplace=True)

    # Features and labels
    X = df[['RSI', 'MACD', 'Volume']]
    y = df['Target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    accuracy = accuracy_score(y_test, model.predict(X_test))

    print(f"🤖 ML Prediction Accuracy: {accuracy * 100:.2f}%")

    # Save model
    joblib.dump(model, "models/decision_tree_model.pkl")
    print("💾 Model saved to models/decision_tree_model.pkl")
