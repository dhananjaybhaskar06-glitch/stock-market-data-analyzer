from src.fetch_data import fetch_stock_data
from src.indicators import *
from src.analysis import analyze_stock
from src.visualization import *
from src.report_generator import generate_pdf_report

ticker = input("Enter stock ticker: ")

start = input("Start date (YYYY-MM-DD): ")

end = input("End date (YYYY-MM-DD): ")

print("Fetching stock data...")

df = fetch_stock_data(ticker, start, end)

df.dropna(inplace=True)

df = add_moving_averages(df)

df = calculate_rsi(df)

df = add_bollinger_bands(df)

analysis = analyze_stock(df)

print("\nAnalysis Summary")

print(analysis)

closing_chart(df, ticker)

moving_average_chart(df, ticker)

candlestick_chart(df, ticker)

returns_distribution(df, ticker)

generate_pdf_report(ticker, analysis)

print("\nPDF report generated successfully!")