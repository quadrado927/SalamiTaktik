import pandas as pd
path = "/Users/sylwia/PycharmProjects/SalamiTaktik/src/imports/apple_news_articles.csv"

df = pd.read_csv(path)

df = df[df["content"] != "[Removed]"]
df = df.str.lower()
