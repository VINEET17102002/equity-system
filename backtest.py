def backtest(df):
    df["Strategy_Return"] = df["Daily_Return"] * df["Position"].shift(1)

    df["Cumulative_Strategy"] = (1 + df["Strategy_Return"] / 100).cumprod()

    return df