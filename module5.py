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

df["Signal"] = "HOLD"
df.loc[(df["MA_20"] > df["MA_50"]) & (df["RSI"] < 70), "Signal"] = "BUY"
df.loc[(df["MA_20"] < df["MA_50"]) & (df["RSI"] > 30), "Signal"] = "SELL"

df["Position"] = df["Signal"].map({
    "BUY": 1,
    "SELL": -1,
    "HOLD": 0
})

df["Strategy_Return"] = df["Daily_Return"] * df["Position"].shift(1)

df["Market_Return"] = df["Daily_Return"]

df["Cumulative_Strategy"] = (1 + df["Strategy_Return"]/100).cumprod()
df["Cumulative_Market"] = (1 + df["Market_Return"]/100).cumprod()

print("\nFinal Results:")
print("Strategy Return:", round(df["Cumulative_Strategy"].iloc[-1], 4))
print("Market Return:", round(df["Cumulative_Market"].iloc[-1], 4))

print("\nLast 10 rows:")
print(df[[
    "Close", "Signal", "Strategy_Return",
    "Cumulative_Strategy", "Cumulative_Market"
]].tail(10))