import pandas as pd
import yfinance as yf

def compare_stocks(stocks, period="1y"):

    compare_df = pd.DataFrame()

    for stock in stocks:

        data = yf.download(stock, period=period)

        if "Close" in data.columns:
            compare_df[stock] = data["Close"]

    return compare_df