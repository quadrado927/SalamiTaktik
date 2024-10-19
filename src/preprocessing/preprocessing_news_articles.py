import pandas as pd
path = #TO DO

df = pd.read_csv(path)

df = df[df["content"] != "[Removed]"]
df = df.str.lower()
