from tech_news.database import create_news
from parsel import Selector
from time import sleep
import requests


# Remoção de tags HTML presentes na string sem a utilização da
# biblioteca Beautiful Soup através de um função proveniente da
# página Medium (autor: Jorge Galvis)
# source: https://medium.com/@jorlugaqui/how-to-strip-html-tags
# -from-a-string-in-python-7cb81a2bbf44
def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


# Requisito 1
def fetch(url):
    try:
        sleep(1)
        response = requests.get(
            url,
            timeout=3,
            headers={"user-agent": "Fake user-agent"},
        )
        response.raise_for_status()
    except (requests.ReadTimeout, requests.HTTPError):
        return None
    else:
        return response.text


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    links = selector.css(".cs-overlay-link::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page = selector.css(".next::attr(href)").get()
    return next_page


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)

    title = selector.css("h1.entry-title::text").get()
    summary = remove_html_tags(selector.css(".entry-content p").get())

    if not title or not summary:
        return None

    url = selector.css("link[rel='canonical']::attr(href)").get()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".author a::text").get()
    comments_count = len(selector.css("comment-list li").getall()) or 0
    tags = selector.css(".post-tags li a::text").getall()
    category = selector.css(".meta-category .label::text").get()

    return {
        "url": url,
        "title": title.strip(),
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary.strip(),
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    URL = 'https://blog.betrybe.com/'

    news_links = []
    news_info = []

    while len(news_links) <= amount:
        html_content = fetch(URL)
        news_links.extend(scrape_updates(html_content))
        URL = scrape_next_page_link(html_content)

    for link in news_links[:amount]:
        page_content = fetch(link)
        news_info.append(scrape_news(page_content))

    create_news(news_info)
    return news_info
