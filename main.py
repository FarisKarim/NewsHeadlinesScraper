from print_headlines import print_headlines_table

def main():
    print('Welcome to the Headlines Scraper!\n')
    print("Select the news sources you want, or All (Enter choices separated by spaces): \n")
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