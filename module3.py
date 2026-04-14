import yfinance as yf
import pandas as pd

ticker = "INFY.NS"
df = yf.download(ticker, period="6mo")
df.columns = df.columns.get_level_values(0)
df.columns.name = None
df.index = pd.to_datetime(df.index)
df = df.sort_index()
df = df.dropna()

df["Daily_Return"] = df["Close"].pct_change() * 100

df["MA_20"] = df["Close"].rolling(window=20).mean()
df["MA_50"] = df["Close"].rolling(window=50).mean()

delta = df["Close"].diff()
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)
avg_gain = gain.rolling(window=14).mean()
avg_loss = loss.rolling(window=14).mean()
rs = avg_gain / avg_loss
df["RSI"] = 100 - (100 / (1 + rs))

print(df[["Close", "MA_20", "MA_50", "RSI"]].tail(10).round(2))