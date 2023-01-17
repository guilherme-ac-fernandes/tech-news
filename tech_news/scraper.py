import requests
from time import sleep
from parsel import Selector


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
    except (requests.HTTPError, requests.ReadTimeout):
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
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


# html_trybe = fetch('https://blog.betrybe.com/')
# print(scrape_updates(html_trybe))
