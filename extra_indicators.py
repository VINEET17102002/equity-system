def add_extra_indicators(df):
    ema12 = df["Close"].ewm(span=12, adjust=False).mean()
    ema26 = df["Close"].ewm(span=26, adjust=False).mean()

    df["MACD"] = ema12 - ema26
    df["Signal_Line"] = df["MACD"].ewm(span=9, adjust=False).mean()

    df["BB_Middle"] = df["Close"].rolling(window=20).mean()
    std_dev = df["Close"].rolling(window=20).std()

    df["BB_Upper"] = df["BB_Middle"] + (2 * std_dev)
    df["BB_Lower"] = df["BB_Middle"] - (2 * std_dev)

    return df