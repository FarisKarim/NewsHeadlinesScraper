import requests
from bs4 import BeautifulSoup

def fetch_fox_news():
    URL = 'https://www.foxnews.com/'
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    headlines_elements = soup.find_all('h3', class_='title')
    headlines_links = [h.find('a') for h in headlines_elements if h.find('a')]

    headlines_text = [link.text.strip() for link in headlines_links][:10]

    return headlines_text

# news = fetch_fox_news()
# for headline in news:
#     print(headline)
#     print("---")
