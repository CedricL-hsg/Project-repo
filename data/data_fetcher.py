import yfinance as yf

def get_price_data(ticker, period="5y", interval="1d"):
    stock = yf.Ticker(ticker)
    return stock.history(period=period, interval=interval)