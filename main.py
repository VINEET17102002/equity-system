import pandas as pd

from fetch_data import fetch_data
from clean_data import clean_data
from indicators import add_indicators
from extra_indicators import add_extra_indicators
from signals import generate_signals
from backtest import backtest


user_input = input("Enter stock symbols (comma-separated, e.g. INFY,TCS,RELIANCE): ")

symbols = [stock.strip().upper() for stock in user_input.split(",")]
tickers = [symbol + ".NS" for symbol in symbols]


results = []

for ticker in tickers:
    print(f"\nProcessing {ticker}...")

    try:
        df = fetch_data(ticker)
        if df.empty:
            print(f"{ticker} has no data, skipping...")
            continue

        df = clean_data(df)
        df = add_indicators(df)
        df = add_extra_indicators(df)
        df = generate_signals(df)
        df = backtest(df)

        latest_signal = df["Signal"].iloc[-1]
        final_return = df["Cumulative_Strategy"].iloc[-1]

        results.append({
            "Ticker": ticker,
            "Signal": latest_signal,
            "Return": round(final_return, 2),
            "RSI": round(df["RSI"].iloc[-1], 2),
            "MA_20": round(df["MA_20"].iloc[-1], 2),
            "MA_50": round(df["MA_50"].iloc[-1], 2)
        })

    except Exception as e:
        print(f"Error processing {ticker}: {e}")


df_results = pd.DataFrame(results)

if not df_results.empty:
    df_results = df_results.sort_values(by="Return", ascending=False)

    print("\nAll Results:")
    print(df_results)

    buy_stocks = df_results[df_results["Signal"] == "BUY"]

    print("\nTop BUY Stocks:")
    print(buy_stocks.head(3))

    df_results.to_csv("final_results.csv", index=False)

else:
    print("No valid results generated.")