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


# Requisito 12
def analyzer_menu():
    """Seu código deve vir aqui"""
    options = "".join(array_options)
    option = input(options)
    return option


# analyzer_menu()
