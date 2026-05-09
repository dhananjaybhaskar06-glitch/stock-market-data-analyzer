import numpy as np

def calculate_sharpe_ratio(returns, risk_free_rate=0.01):

    excess_returns = returns.mean() - risk_free_rate

    sharpe = excess_returns / returns.std()

    return sharpe

def calculate_max_drawdown(returns):

    cumulative = (1 + returns).cumprod()

    peak = cumulative.cummax()

    drawdown = (cumulative - peak) / peak

    return drawdown.min()