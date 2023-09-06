import requests
from bs4 import BeautifulSoup


def fetch_news_cnn():
    URL = 'https://www.cnn.com/'
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    title_section = soup.find('h2', class_='container__title-text container_list-headlines__title-text', string="More top stories")
    
    for sibling in title_section.find_next_siblings(limit=5):
        print(sibling)
        print("-----")
    
    headlines_div = title_section.find_next('div', class_='container_list-headlines__cards-wrapper')
    
    if not headlines_div:
        print("Headlines container not found.")
        return
    
    headlines = headlines_div.find_all('span', attrs={"data-editable": "headline"})
    headlines_text = [headline.text for headline in headlines]

    return headlines_text

news = fetch_news_cnn()
if news:
    for headline in news:
        print(headline)
        print("---")
