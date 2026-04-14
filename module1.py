import yfinance as yf
import pandas as pd

ticker = "INFY.NS"
df = yf.download(ticker, period="6mo")

df.columns = df.columns.get_level_values(0)

print("Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nData types:")
print(df.dtypes)
print("\nMissing values:")
print(df.isnull().sum())