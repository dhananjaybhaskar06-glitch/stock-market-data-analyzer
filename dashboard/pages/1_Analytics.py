import streamlit as st
import plotly.graph_objects as go
from src.data_service import get_stock_data
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
)

st.set_page_config(layout="wide")

st.title("📊 Stock Analytics")

ticker = st.text_input("Enter Stock", "TSLA")

data = get_stock_data(ticker)

data["MA20"] = data["Close"].rolling(20).mean()
data["MA50"] = data["Close"].rolling(50).mean()

fig = go.Figure()

fig.add_trace(go.Candlestick(
    x=data.index,
    open=data["Open"],
    high=data["High"],
    low=data["Low"],
    close=data["Close"],
    name="Price"
))

fig.add_trace(go.Scatter(x=data.index, y=data["MA20"], name="MA20"))
fig.add_trace(go.Scatter(x=data.index, y=data["MA50"], name="MA50"))

fig.update_layout(template="plotly_dark", height=600)

st.plotly_chart(fig, use_container_width=True)