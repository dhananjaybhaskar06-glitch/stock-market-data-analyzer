import streamlit as st
from src.data_service import get_stock_data
from src.risk_service import calculate_risk
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
)

st.set_page_config(layout="wide")

st.title("⚠ Risk Analysis")

ticker = st.text_input("Stock", "TSLA")

data = get_stock_data(ticker)

risk = calculate_risk(data)

col1, col2, col3 = st.columns(3)

col1.metric("Volatility", f"{risk['volatility']:.4f}")
col2.metric("Sharpe Ratio", f"{risk['sharpe']:.2f}")
col3.metric("Max Drawdown", f"{risk['drawdown']:.2f}")