import streamlit as st
from src.data_service import get_stock_data
from src.ai_service import generate_signal
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
)

st.set_page_config(layout="wide")

st.title("🤖 AI Trading Signal")

ticker = st.text_input("Stock", "TSLA")

data = get_stock_data(ticker)

signal = generate_signal(data)

st.subheader("AI Decision")

st.success(signal)