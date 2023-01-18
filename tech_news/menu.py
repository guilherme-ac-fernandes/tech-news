from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import search_by_category
from tech_news.analyzer.search_engine import search_by_date
from tech_news.analyzer.search_engine import search_by_tag
from tech_news.analyzer.search_engine import search_by_title
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.ratings import top_5_news
import sys


string_options = [
    'Selecione uma das opções a seguir:\n',
    ' 0 - Popular o banco com notícias;\n',
    ' 1 - Buscar notícias por título;\n',
    ' 2 - Buscar notícias por data;\n',
    ' 3 - Buscar notícias por tag;\n',
    ' 4 - Buscar notícias por categoria;\n',
    ' 5 - Listar top 5 notícias;\n',
    ' 6 - Listar top 5 categorias;\n',
    ' 7 - Sair.',
]


def _get_tech_news(amount):
    if not amount.isdigit():
        raise ValueError()
    return get_tech_news(amount)


def _search_by_title(title):
    return search_by_title(title)


def _search_by_date(title):
    return search_by_date(title)


def _search_by_tag(title):
    return search_by_tag(title)


def _search_by_category(title):
    return search_by_category(title)


def _top_5_news():
    return top_5_news()


def _top_5_categories():
    return top_5_categories()


functions_options = {
    "0": {
        "callback": _get_tech_news,
        "question": "Digite quantas notícias serão buscadas:"
    },
    "1": {
        "callback": _search_by_title,
        "question": "Digite o título:"
    },
    "2": {
        "callback": _search_by_date,
        "question": "Digite a data no formato aaaa-mm-dd:"
    },
    "3": {
        "callback": _search_by_tag,
        "question": "Digite a tag:"
    },
    "4": {
        "callback": _search_by_category,
        "question": "Digite a categoria:"
    },
    "5": {
        "callback": _top_5_news,
    },
    "6": {
        "callback": _top_5_categories,
    },
}


# Requisito 12
def analyzer_menu():
    menu_options = "".join(string_options)
    option = input(menu_options)

    if not option.isdigit() or int(option) not in range(8):
        print(ValueError('Opção inválida'), file=sys.stderr)
        return

    if int(option) == 7:
        print("Encerrando script\n")
        return

    function = functions_options[option]
    response = ''

    if "question" in function:
        response_input = input(function["question"])
        response = function["callback"](response_input)

    if "question" not in function:
        response = function["callback"]()

    print(response, end="")
    return response
