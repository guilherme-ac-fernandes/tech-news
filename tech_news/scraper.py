import requests
from time import sleep


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
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
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
