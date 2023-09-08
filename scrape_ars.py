import requests
from bs4 import BeautifulSoup

def fetch_ars_headlines():
    URL = 'https://arstechnica.com/gadgets/'
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    h2_tags = soup.find_all('h2', limit=10) 
    headlines_text = [h2.a.text.strip() for h2 in h2_tags if h2.a]

    return headlines_text

# for text in headlines_text:
#     print(text)
#     print("---")
