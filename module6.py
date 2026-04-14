import yfinance as yf
import pandas as pd

ticker = "INFY.NS"
df = yf.download(ticker, period="6mo")

df.columns = df.columns.get_level_values(0)
df.columns.name = None

df.index = pd.to_datetime(df.index)
df = df.sort_index()
df = df.dropna()

ema12 = df["Close"].ewm(span=12, adjust=False).mean()
ema26 = df["Close"].ewm(span=26, adjust=False).mean()

df["MACD"] = ema12 - ema26
df["Signal_Line"] = df["MACD"].ewm(span=9, adjust=False).mean()

df["BB_Middle"] = df["Close"].rolling(window=20).mean()
std_dev = df["Close"].rolling(window=20).std()

df["BB_Upper"] = df["BB_Middle"] + (2 * std_dev)
df["BB_Lower"] = df["BB_Middle"] - (2 * std_dev)

print("\nIndicators:")
print(df[[
    "Close", "MACD", "Signal_Line",
    "BB_Upper", "BB_Lower"
]].tail(10).round(2))