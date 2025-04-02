def calculate_max_drawdown(prices):
    """
    Berechnet den maximalen Drawdown einer Preisreihe.
    """
    peak = prices.cummax()
    drawdown = (prices - peak) / peak
    max_drawdown = drawdown.min()
    return max_drawdown