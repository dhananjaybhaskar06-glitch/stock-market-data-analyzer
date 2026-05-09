def analyze_stock(df):

    df["Daily Return"] = df["Close"].pct_change()

    volatility = df["Daily Return"].std()

    highest = df["High"].max()
    lowest = df["Low"].min()

    avg_return = df["Daily Return"].mean()

    return {
        "volatility": volatility,
        "highest": highest,
        "lowest": lowest,
        "average_return": avg_return
    }