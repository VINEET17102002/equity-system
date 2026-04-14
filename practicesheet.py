# import pandas as pd

# data = {
#     "Name": ["Infosys", "TCS", "Wipro"],
#     "Price": [1470, 3800, 420],
#     "Volume": [5000000, 3000000, 8000000]
# }

# df = pd.DataFrame(data)
# print(df)
# print("\nVolume Column:")
# print(df["Volume"])

# print(df.index)
# print(df.iloc[0])    
# print(df.loc[0])


import pandas as pd

stocks = pd.read_csv("stocks.csv")
tickers = stocks["SYMBOL"].apply(lambda x: x + ".NS")
tickers1 = tickers.head(5)

print(tickers1)