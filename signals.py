def generate_signals(df):
    df["Signal"] = "HOLD"

    # Basic logic (can improve later)
    df.loc[(df["MA_20"] > df["MA_50"]) & (df["RSI"] < 70), "Signal"] = "BUY"
    df.loc[(df["MA_20"] < df["MA_50"]) & (df["RSI"] > 30), "Signal"] = "SELL"

    df["Position"] = df["Signal"].map({
        "BUY": 1,
        "SELL": -1,
        "HOLD": 0
    })

    return df