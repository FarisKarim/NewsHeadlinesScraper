import requests
from bs4 import BeautifulSoup

def fetch_news_nytimes():
    URL = 'https://www.nytimes.com/'
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    headlines = soup.find_all('h3', class_='indicate-hover')
    headlines_text = [headline.text for headline in headlines[:10]]

    return headlines_text
news = fetch_news_nytimes()
for item in news:
    print(item)
    print("---")