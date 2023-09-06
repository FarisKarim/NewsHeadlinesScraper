import requests
from bs4 import BeautifulSoup

def fetch_news_bbc():
    URL = 'https://www.bbc.com/news'
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    containers = soup.find_all('div', class_='gs-c-promo-body', limit=10) 

    news_data = []
    seen_headlines = set()

    for container in containers:
        headline_elem = container.find('h3', class_='gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text')
        description_elem = container.find('p', class_='gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary')
        
        if headline_elem and description_elem:
            headline_text = headline_elem.text.strip()
            description_text = description_elem.text.strip()

            # Check if we haven't seen this headline yet and we haven't reached 5 items
            if headline_text not in seen_headlines and len(news_data) < 5:
                seen_headlines.add(headline_text)
                news_data.append({
                    'headline': headline_text,
                    'description': description_text
                })

    return news_data

news = fetch_news_bbc()
for item in news:
    print(item['headline'])
    print(item['description'])
    print("---")
