import requests
import pandas as pd
from src.imports.api_key import api_key


url = 'https://newsapi.org/v2/everything'

params = {
    'q': 'apple',
    'from': '2024-10-01',
    'sortBy': 'relevancy',
    'language': 'en',
    'apiKey': api_key
}

response = requests.get(url, params=params)
data = response.json()

if response.status_code == 200:
    articles = data.get('articles', [])

    # Prepare data for DataFrame
    articles_list = []
    for article in articles:
        articles_list.append({
            'title': article.get('title'),
            'description': article.get('description'),
            'url': article.get('url'),
            'publishedAt': article.get('publishedAt'),
            'content': article.get('content')
        })

    articles_df = pd.DataFrame(articles_list)

    articles_df.to_csv('apple_news_articles.csv', index=False)
