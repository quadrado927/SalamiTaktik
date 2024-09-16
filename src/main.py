import yfinance as yf
import pandas as pd

symbols = ["AAPL", "LDO.MI", "NVDA", "RHM.DE", "RTX", "AMZN", "BA", "UBSG.SW", "UCG.MI",
            "TSLA", "LISN.SW", "NESN.SW", "ZURN.SW", "NOVN", "META", "NFLX", "LMT", "NOC",
              "GD", "AIR", "TII", "XOM", "SHEL", "CVX", "BP", "EC", "EQNRO", "ENI", "PSX",
                "WMT", "COST", "TGT", "HD", "CR", "CSV", "CA", "EBAY", "UHRN", "MSFT", "GOOGL",
                  "IBM", "INTC", "CSCO", "ORCL", "ADBE", "CRM", "SSU", "LOGN.SW", "ABBN.SW", "BKNG",
                    "LVS", "DAL", "ABNB", "AAL", "LHA", "RYAAY", "GS", "UPS", "DHL", "GE", "BLK", "VTI",
                      "MS", "HLT", "SHOP", "SBUX", "BAER.SW", "SIN.SW", "ROCH.SW"]



stocks = {sym: yf.Ticker(sym) for sym in symbols}

stocks["AAPL"]

data = stocks["AAPL"].history(period="1mo")



print(data)
print(type(data))