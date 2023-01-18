from tech_news.database import find_news
from collections import Counter
# Utilização do modulo operator para ordenação de dicionários
# proveniente do Stack OverFlow
# source: https://stackoverflow.com/questions/72899/how-do-i-
# sort-a-list-of-dictionaries-by-a-value-of-the-dictionary
from operator import itemgetter


# Requisito 10
def top_5_news():
    news = find_news()
    alphabetic_news = sorted(news, key=itemgetter('title'))
    popular_news = sorted(
        alphabetic_news,
        key=itemgetter('comments_count'),
        reverse=True,
    )
    return [(new["title"], new["url"]) for new in popular_news][:5]


# Requisito 11
def top_5_categories():
    news = find_news()
    categories = [new["category"] for new in news]
    categories_count = Counter(sorted(categories)).most_common()
    categories_top_five = [category[0] for category in categories_count]
    return categories_top_five[:5]
