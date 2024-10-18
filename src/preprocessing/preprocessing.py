import os
import pandas as pd
from src.preprocessing.functions import *




#importieren
current_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current_dir, '..', 'imports', 'historical_data_apple_test.csv')
df = pd.read_csv(path)
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date')
print(df.columns.tolist())

#Modifizieren df
df['SMA_10'] = calculate_sma(df, 10)
df['SMA_50'] = calculate_sma(df, 50)
df['EMA_10'] = calculate_ema(df, 10)
df['EMA_50'] = calculate_ema(df, 50)
df['RSI_14'] = calculate_rsi(df, 14)

df=df.dropna()
#splitten
split_index = int(0.8 * len(df))
train_df = df[:split_index]   # First 80% (older data)
test_df = df[split_index:]    # Last 20% (latest data)





