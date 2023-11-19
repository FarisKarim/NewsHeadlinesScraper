import requests
from bs4 import BeautifulSoup


def fetch_news_cnn():
    URL = 'https://www.cnn.com/'
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    headlines = soup.find_all(lambda tag: 'class' in tag.attrs and 'headline' in ''.join(
        tag['class']) and ((tag.get('data-editable') == 'headline') or (tag.get('data.editable' == 'title'))))

    headlines_text = [headline.text for headline in headlines if len(headline.text.split()) > 4][:15]

    return headlines_text

# news = fetch_news_cnn()
# if news:
#     for headline in news:
#         print(headline)
#         print("---")
