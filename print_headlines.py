from scrape_bbc import fetch_news_bbc
from scrape_cnn import fetch_news_cnn
from scrape_foxnews import fetch_fox_news
from scrape_nytimes import fetch_news_nytimes
from scrape_ars import fetch_ars_headlines
from scrape_cbs import fetch_news_cbs
from prettytable import PrettyTable, ALL


def print_headlines_table(*sources):
    table = PrettyTable()
    table._max_width = {"BBC": 40, "CNN": 40,
                        "FOX": 40, "NYT": 40, "ArsTechnica": 40, "CBS": 40}

    if 'BBC' in sources:
        bbc_headlines = fetch_news_bbc()
        table.add_column("BBC", bbc_headlines)
        while len(bbc_headlines) < 10:
            bbc_headlines.append("")
        while len(bbc_headlines) > 10:
            bbc_headlines.pop()
    if 'CBS' in sources:
        cbs_headlines = fetch_news_cbs()
        table.add_column("CBS", cbs_headlines)
        while len(cbs_headlines) < 10:
            cbs_headlines.append("")
        while len(cbs_headlines) > 10:
            cbs_headlines.pop()
    if 'CNN' in sources:
        cnn_headlines = fetch_news_cnn()
        while len(cnn_headlines) < 10:
            cnn_headlines.append("")
        while len(cnn_headlines) > 10:
            cnn_headlines.pop()
        table.add_column("CNN", cnn_headlines)
    if 'FOX' in sources:
        fox_headlines = fetch_fox_news()
        table.add_column("FOX", fox_headlines)
        while len(fox_headlines) < 10:
            fox_headlines.append("")
        while len(fox_headlines) > 10:
            fox_headlines.pop()
    if 'NYT' in sources:
        nytimes_headlines = fetch_news_nytimes()
        table.add_column("NYT", nytimes_headlines)
        while len(nytimes_headlines) < 10:
            nytimes_headlines.append("")
        while len(nytimes_headlines) > 10:
            nytimes_headlines.pop()
    if 'ArsTechnica' in sources:
        ars_headlines = fetch_ars_headlines()
        table.add_column("ArsTechnica", ars_headlines)
        while len(ars_headlines) < 10:
            ars_headlines.append("")
        while len(ars_headlines) > 10:
            ars_headlines.pop()

    table.hrules = ALL
    print(table)
