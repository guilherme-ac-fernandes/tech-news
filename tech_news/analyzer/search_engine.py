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
    tuple_news = []
    for new in search_news({"tags": {'$regex': tag, "$options": 'i'}}):
        tuple_news.append((new["title"], new["url"]))
    return tuple_news


# Requisito 9
def search_by_category(category):
    tuple_news = []
    news = search_news({"category": {'$regex': category, "$options": 'i'}})
    for new in news:
        tuple_news.append((new["title"], new["url"]))
    return tuple_news
