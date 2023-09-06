from scrape_bbc import fetch_news_bbc
from scrape_cnn import fetch_news_cnn
from scrape_foxnews import fetch_fox_news
from scrape_nytimes import fetch_news_nytimes
from prettytable import PrettyTable, ALL

def print_headlines_table(*sources):
    table = PrettyTable()
    table._max_width = {"BBC": 40, "CNN": 40, "FOX": 40, "NYT": 40}

    if 'BBC' in sources:
        bbc_headlines = fetch_news_bbc()
        table.add_column("BBC", bbc_headlines)
    if 'CNN' in sources:
        cnn_headlines = fetch_news_cnn()
        table.add_column("CNN", cnn_headlines)
    if 'FOX' in sources:
        fox_headlines = fetch_fox_news()
        table.add_column("FOX", fox_headlines)
    if 'NYT' in sources:
        nytimes_headlines = fetch_news_nytimes()
        table.add_column("NYT", nytimes_headlines)

    table.hrules = ALL
    print(table)

def main():
    print("Select the news sources you want, or All (Enter choices separated by spaces):")
    print("BBC")
    print("CNN")
    print("FOX")
    print("NYT")
    print("All")

    choices = [choice.lower() for choice in input().split()]
    selected = set()

    if 'all' in choices:
        selected.update(['BBC', 'CNN', 'FOX', 'NYT'])
    if 'bbc' in choices:
        selected.add('BBC')
    if 'cnn' in choices:
        selected.add('CNN')
    if 'fox' in choices:
        selected.add('FOX')
    if 'nyt' in choices:
        selected.add('NYT')
    
    if not selected:
        print('No valid sources selected.')
    print_headlines_table(*selected)


if __name__ == "__main__":
    main()