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
        while len(bbc_headlines) < 10:
            bbc_headlines.append("")
    if 'CNN' in sources:
        cnn_headlines = fetch_news_cnn()
        while len(cnn_headlines) < 10:
            cnn_headlines.append("")
        table.add_column("CNN", cnn_headlines)
    if 'FOX' in sources:
        fox_headlines = fetch_fox_news()
        table.add_column("FOX", fox_headlines)
        while len(fox_headlines) < 10:
            fox_headlines.append("")
    if 'NYT' in sources:
        nytimes_headlines = fetch_news_nytimes()
        table.add_column("NYT", nytimes_headlines)
        while len(nytimes_headlines) < 10:
            nytimes_headlines.append("")

    table.hrules = ALL
    print(table)
