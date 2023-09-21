from print_headlines import print_headlines_table


def main():
    print('Welcome to the Headlines Scraper!\n')
    
    news_type = input("Do you want tech news or general news? (Enter 'tech' or 'general'): ").lower()
    
    if news_type == 'tech':
        print("\nSelect the tech news source you want:")
        print("ArsTechnica (enter 'at' for short)\n")
        
        choices = [choice.lower() for choice in input().split()]
        selected = set()
        if 'arstechnica' in choices or 'at' in choices:
            selected.add('ArsTechnica')
        if not selected:
            print('No valid sources selected.')
            return
        print_headlines_table(*selected)
    
    elif news_type == 'general':
        print("\nSelect the news sources you want, or All (Enter choices separated by spaces): ")
        print("BBC")
        print("CNN")
        print("FOX")
        print("NYT")
        print("CBS")
        print("All\n")

        choices = [choice.lower() for choice in input().split()]
        selected = set()

        if 'all' in choices:
            selected.update(['BBC', 'CNN', 'FOX', 'NYT', 'CBS'])
        if 'bbc' in choices:
            selected.add('BBC')
        if 'cnn' in choices:
            selected.add('CNN')
        if 'fox' in choices:
            selected.add('FOX')
        if 'nyt' in choices:
            selected.add('NYT')
        if 'cbs' in choices:
            selected.add('CBS')
        if not selected:
            print('No valid sources selected.')
            return

        print_headlines_table(*selected)

    else:
        print("Invalid choice. Please choose 'tech' or 'general'.")
        return


if __name__ == "__main__":
    main()
