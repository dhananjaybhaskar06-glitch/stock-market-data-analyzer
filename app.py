import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.set_page_config(page_title="Stock Analyzer", layout="wide")

st.title("📈 Advanced Stock Market Analyzer")

ticker = st.text_input("Enter Ticker", "AAPL")

data = yf.download(ticker, period="1y")

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=data.index,
    y=data["Close"],
    mode='lines',
    name='Close Price'
))

st.plotly_chart(fig, use_container_width=True)

st.write(data.tail())