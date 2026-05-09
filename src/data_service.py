import yfinance as yf
import pandas as pd

def get_stock_data(ticker, period="1y"):

    data = yf.download(ticker, period=period)

    # Fix multi-index issue safely
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data.dropna(inplace=True)

    return data