import yfinance as yf
import pandas as pd

symbols = ["AAPL", "LDO.MI", "NVDA", "RHM.DE", "RTX", "AMZN", "BA", "UBSG.SW", "UCG.MI",
            "TSLA", "LISN.SW", "NESN.SW", "ZURN.SW", "NOVN.SW", "META", "NFLX", "LMT", "NOC",
              "GD", "AIR", "XOM", "SHEL", "CVX", "BP", "EC", "EQNR", "E", "PSX",
                "WMT", "COST", "TGT", "HD", "CR", "CSV", "CA", "EBAY", "UHRN.SW", "MSFT", "GOOGL",
                  "IBM", "INTC", "CSCO", "ORCL", "ADBE", "CRM", "SSU.JO", "LOGN.SW", "ABBN.SW", "BKNG",
                    "LVS", "DAL", "ABNB", "AAL", "LHA.DE", "RYAAY", "GS", "UPS", "GE", "BLK", "VTI",
                      "MS", "HLT", "SHOP", "SBUX", "BAER.SW", "SIE.DU", "ROG.SW", "TII.F"]



#stocks = {sym: yf.Ticker(sym) for sym in symbols}

#stocks["AAPL"]

#data = stocks["AAPL"].history(period="1mo")



#print(data)
#print(type(data))

data = []


for symbol in symbols:
  ticker = yf.Ticker(symbol)
  hist = ticker.history(period="1y", interval="1wk")

  for date, row in hist.iterrows():
    data.append({
      'Date': date,
      'Open': row['Open'],
      'Symbol': symbol
    })


df = pd.DataFrame(data)


df.head()

