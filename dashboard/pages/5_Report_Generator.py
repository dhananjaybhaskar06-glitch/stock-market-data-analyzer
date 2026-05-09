import streamlit as st
from src.data_service import get_stock_data
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
)

st.set_page_config(layout="wide")

st.title("📄 Report Generator")

ticker = st.text_input("Stock", "TSLA")

data = get_stock_data(ticker)

st.dataframe(data.tail())

csv = data.to_csv().encode("utf-8")

st.download_button(
    "Download CSV Report",
    csv,
    f"{ticker}_report.csv",
    "text/csv"
)