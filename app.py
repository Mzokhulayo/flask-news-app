
from flask import Flask, render_template
import requests

app = Flask(__name__)

NEWS_API_KEY = 'your_news_api_key'  # Use your API key from a news API provider like NewsAPI.org

def get_johannesburg_news():
    url = f"https://newsapi.org/v2/everything?q=Johannesburg&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    news = response.json().get('articles', [])
    return news

@app.route('/')
def home():
    news_articles = get_johannesburg_news()
    return render_template('index.html', news=news_articles)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
