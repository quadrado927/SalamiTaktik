import yfinance as yf
import pandas as pd
#Only Apple for now
ticker = yf.Ticker("AAPL")

data = ticker.history(period="10y", interval="1d")

df = pd.DataFrame(data)

print(df.head())
print(df.columns.tolist())
df.to_csv("historical_data_apple_test.csv", index=True)