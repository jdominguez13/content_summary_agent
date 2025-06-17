import requests
import os
from datetime import datetime, timedelta

NEWS_API_KEY = os.getenv('NEWS_API_KEY')

print("Loaded NEWS_API_KEY:", NEWS_API_KEY)

TOPIC = 'AI productivity OR AI revenue OR AI innovation OR artificial intelligence productivity OR artificial intelligence revenue OR artificial intelligence innovation'

NEWS_API_URL = 'https://newsapi.org/v2/everything'


def fetch_articles(days=1, max_results=10):
    from_date = (datetime.utcnow() - timedelta(days=days)).strftime('%Y-%m-%d')
    params = {
        'q': TOPIC,
        'from': from_date,
        'sortBy': 'popularity',
        'language': 'en',
        'apiKey': NEWS_API_KEY,
        'pageSize': max_results
    }
    response = requests.get(NEWS_API_URL, params=params)
    response.raise_for_status()
    articles = response.json().get('articles', [])
    return [
        {
            'title': a['title'],
            'url': a['url'],
            'publishedAt': a['publishedAt'],
            'content': a.get('content', ''),
            'description': a.get('description', '')
        }
        for a in articles
    ]

if __name__ == '__main__':
    for article in fetch_articles():
        print(article['title'], article['url']) 