from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    news = find_news()
    categories = [new["category"] for new in news]
    categories_count = Counter(sorted(categories)).most_common()
    categories_top_five = [category[0] for category in categories_count]
    return categories_top_five[:5]
