def generate_signal(data):

    close = data["Close"]

    ma20 = close.rolling(20).mean().iloc[-1]
    ma50 = close.rolling(50).mean().iloc[-1]
    latest = close.iloc[-1]

    if latest > ma20 > ma50:
        return "📈 BUY (Strong Uptrend)"
    elif latest < ma20 < ma50:
        return "📉 SELL (Downtrend)"
    else:
        return "⚖ HOLD (Sideways Market)"