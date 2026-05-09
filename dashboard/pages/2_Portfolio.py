import streamlit as st
import yfinance as yf
import pandas as pd
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
)

st.set_page_config(layout="wide")

st.title("📈 Portfolio Comparison")

stocks = st.multiselect(
    "Select Stocks",
    ["AAPL", "TSLA", "MSFT", "NVDA"],
    default=["AAPL", "TSLA"]
)

df = pd.DataFrame()

for s in stocks:

    data = yf.download(s, period="1y")

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    df[s] = data["Close"]

st.line_chart(df)