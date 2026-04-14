import yfinance as yf

def fetch_data(ticker):
    df = yf.download(ticker, period="6mo")
    return df