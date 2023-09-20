import requests
from bs4 import BeautifulSoup

def fetch_news_cbs():
    URL = "https://www.cbsnews.com/"
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    hl_tags = soup.find_all('h4', class_='item__hed', limit=10)
    headlines_text = [hl.text.strip() for hl in hl_tags]
    return headlines_text

headlines = fetch_news_cbs()

# for text in headlines:
#     print(text)
#     print("---")
