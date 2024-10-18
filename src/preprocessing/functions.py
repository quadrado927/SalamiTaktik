def calculate_sma(data, window):
    return data['Close'].rolling(window=window).mean()
def calculate_ema(data, window):
    return data['Close'].ewm(span=window, adjust=False).mean()
def calculate_rsi(data, period=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    RS = gain / loss
    RSI = 100 - (100 / (1 + RS))
    return RSI