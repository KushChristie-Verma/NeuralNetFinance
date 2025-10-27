import yfinance as yf
import pandas as pd

def load_raw_data(name='SPY'):
    raw_data = yf.download(
    tickers = name,
    start="2021-01-01", # From what point do we want to start getting stock data
    end="2025-01-1", # From what point do we want to stop getting stock data
    interval = "1d", # The sample rate of the data one stock data every day
    ignore_tz=True,
    auto_adjust=True, # Adjust all fields by splits and dividends
    )

    raw_data = raw_data[['Open', 'High', 'Low', 'Close', 'Volume']]
    return raw_data.dropna()



if __name__ == "__main__":
    print(load_raw_data().head())




