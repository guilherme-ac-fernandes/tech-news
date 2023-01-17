from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    tuple_news = []
    for new in search_news({"title": {'$regex': title, "$options": 'i'}}):
        tuple_news.append((new["title"], new["url"]))
    return tuple_news


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
