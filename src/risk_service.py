import numpy as np

def calculate_risk(data):

    returns = data["Close"].pct_change().dropna()

    volatility = returns.std()

    sharpe = (returns.mean() / volatility) if volatility != 0 else 0

    cumulative = (1 + returns).cumprod()

    peak = cumulative.cummax()

    drawdown = (cumulative - peak) / peak

    return {
        "volatility": volatility,
        "sharpe": sharpe,
        "drawdown": drawdown.min()
    }