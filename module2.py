import yfinance as yf
import pandas as pd

ticker = "INFY.NS"
df = yf.download(ticker, period="6mo")
df.columns = df.columns.get_level_values(0)

df.index = pd.to_datetime(df.index)

df = df.sort_index()

df = df.dropna()

df.columns.name = None

df["Daily_Return"] = df["Close"].pct_change() * 100

print("Shape after cleaning:", df.shape)
print("\nSample with Daily Return:")
print(df[["Close", "Daily_Return"]].head(10))
print("\nBasic stats:")
print(df["Daily_Return"].describe().round(2))