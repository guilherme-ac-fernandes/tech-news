from tech_news.database import find_news
from collections import Counter
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
    return popular_news[:5]


# Requisito 11
def top_5_categories():
    news = find_news()
    categories = [new["category"] for new in news]
    categories_count = Counter(sorted(categories)).most_common()
    categories_top_five = [category[0] for category in categories_count]
    return categories_top_five[:5]


print(top_5_news())
