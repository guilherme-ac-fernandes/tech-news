from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    tuple_news = []
    for new in search_news({"title": {'$regex': title, "$options": 'i'}}):
        tuple_news.append((new["title"], new["url"]))
    return tuple_news


# Requisito 7
def search_by_date(date):
    try:
        date_format = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        tuple_news = []
        query = {"timestamp": {"timestamp": {"$eq": date_format}}}
        for new in search_news(query):
            tuple_news.append((new["title"], new["url"]))
        return tuple_news
    except ValueError:
        raise ValueError("Data inválida")


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
