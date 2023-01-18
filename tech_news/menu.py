from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import search_by_category
from tech_news.analyzer.search_engine import search_by_date
from tech_news.analyzer.search_engine import search_by_tag
from tech_news.analyzer.search_engine import search_by_title
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.ratings import top_5_news
import sys


def find_get_tech_news(amount):
    return get_tech_news(amount)


def find_title(title):
    return search_by_title(title)


def find_date(title):
    return search_by_date(title)


def find_tag(title):
    return search_by_tag(title)


def find_category(title):
    return search_by_category(title)


def find_top_5_news():
    return top_5_news()


def find_top_5_categories():
    return top_5_categories()


array_options = [
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

callback_option = {
    "0": {
        "def": find_get_tech_news,
        "inputString": "Digite quantas notícias serão buscadas:"
    },
    "1": {
        "def": find_title,
        "inputString": "Digite o título:"
    },
    "2": {
        "def": find_date,
        "inputString": "Digite a data no formato aaaa-mm-dd:"
    },
    "3": {
        "def": find_tag,
        "inputString": "Digite a tag:"
    },
    "4": {
        "def": find_category,
        "inputString": "Digite a categoria:"
    },
    "5": {
        "def": find_top_5_news,
    },
    "6": {
        "def": find_top_5_categories,
    },
}


# Requisito 12
def analyzer_menu():
    menu_options = "".join(array_options)
    choose_option = input(menu_options)

    if not choose_option.isdigit() or int(choose_option) not in range(8):
        print(ValueError('Opção inválida'), file=sys.stderr)
        return

    if int(choose_option) == 7:
        print("Encerrando script\n")
        return

    # response = ''
    callback = callback_option[choose_option]

    if "inputString" in callback:
        response_input = input(callback["inputString"])
        response = callback["def"](response_input)
        print(response, end="")
    else:
        response = callback["def"]()
        print(response, end="")

    # print(response, end="")
    # return response

# def analyzer_menu():
#     options = "".join(array_options)
#     option = input(options)

#     if option == '0':
#         news_amount = input("Digite quantas notícias serão buscadas:")
#         return get_tech_news(news_amount)

#     elif option == '1':
#         news_title = input("Digite o título:")
#         return search_by_title(news_title)

#     elif option == '2':
#         news_date = input("Digite a data no formato aaaa-mm-dd:")
#         return search_by_date(news_date)

#     elif option == '3':
#         news_tag = input("Digite a tag:")
#         return search_by_tag(news_tag)

#     elif option == '4':
#         news_category = input("Digite a categoria:")
#         return search_by_category(news_category)

#     elif option == '5':
#         return top_5_news(news_amount)

#     elif option == '6':
#         return top_5_categories(news_amount)

#     elif option == '7':
#         return
#     else:
#         print(ValueError('Opção inválida'), file=sys.stderr)

#     # print(response, end="")

# print(analyzer_menu())
