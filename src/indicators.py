import pandas as pd

# -----------------------------
# Moving Averages
# -----------------------------

def add_moving_averages(df):

    df["MA20"] = df["Close"].rolling(window=20).mean()

    df["MA50"] = df["Close"].rolling(window=50).mean()

    return df

# -----------------------------
# RSI Indicator
# -----------------------------

def calculate_rsi(df, period=14):

    delta = df["Close"].diff()

    gain = delta.where(delta > 0, 0)

    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=period).mean()

    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss

    df["RSI"] = 100 - (100 / (1 + rs))

    return df

# -----------------------------
# Bollinger Bands
# -----------------------------

def add_bollinger_bands(df):

    rolling_mean = df["Close"].rolling(window=20).mean()

    rolling_std = df["Close"].rolling(window=20).std()

    df["MiddleBand"] = rolling_mean

    df["UpperBand"] = rolling_mean + (rolling_std * 2)

    df["LowerBand"] = rolling_mean - (rolling_std * 2)

    return df