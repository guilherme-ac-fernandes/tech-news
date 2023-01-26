# Projeto Tech News 👨🏻‍💻🗞

Consiste em uma aplicação para realização de consultas de notícias sobre tecnologia presentes no [blog da Trybe](https://blog.betrybe.com/), para realização da raspagem dos dados e armazenar em um banco de dados.

* Construído utilizando Python e MongoDB

<br />

<details>
  <summary><strong>Descrição das funções criadas:</strong></summary><br />

| Função | Descrição | Localização |
|---|---|---|
| `fetch` | Responsável por realizar a requisição do conteúdo `HTML` | `tech_news/scraper.py` |
| `scrape_updates` | Responsável por coletar todos os links das páginas de notícias | `tech_news/scraper.py` |
| `scrape_next_page_link` | Responsável por coletar o link da próxima página de notícias | `tech_news/scraper.py` |  
| `scrape_news` | Responsável por coletar as informações de uma notícia | `tech_news/scraper.py` |  
| `get_tech_news` | Responsável por combinar as funções acima para realizar a raspagem de dados e armazenadamento das informações no banco de dados | `tech_news/scraper.py` |  
| `search_by_title` | A partir dos dados presentes no banco, retorna a busca por título | `tech_news/analyzer/search_engine.py` |
| `search_by_date` | A partir dos dados presentes no banco, retorna a busca por data | `tech_news/analyzer/search_engine.py` |  
| `search_by_tag` | A partir dos dados presentes no banco, retorna a busca pela tag informada | `tech_news/analyzer/search_engine.py` | 
| `search_by_category` | A partir dos dados presentes no banco, retorna a busca pela categoria informada | `tech_news/analyzer/search_engine.py` |
| `top_5_news` | A partir dos dados presentes no banco, retorna as cinco notícias mais populares | `tech_news/analyzer/ratings.py` |
| `top_5_categories` | A partir dos dados presentes no banco, retorna as cinco categorias com mais ocorrências | `tech_news/analyzer/ratings.py` |
| `analyzer_menu` | A partir das funções criadas, retorna as informações mediante a solicitação pela linha de comando | `tech_news/menu.py` |
</details>


### Estrutura do Projeto

```
.
├── tech_news
│   ├── analyzer
│   │   ├── 🔹ratings.py
│   │   └── 🔹search_engine.py
│   ├── 🔸database.py
│   └── 🔹menu.py
│   └── 🔹scraper.py
├── tests
│   └── 🔸__init__.py
├── 🔸dev-requirements.txt
├── 🔸docker-compose.yml
├── 🔸Dockerfile
├── 🔸pyproject.toml
├── 🔸README.md
├── 🔸requirements.txt
├── 🔸setup.cfg
└── 🔸setup.py

Legenda:
🔸 Arquivos desenvolvidos pela Trybe (não foram alterados).
🔹 Arquivos a serem alterados para realizar os requisitos.

```


### Instruções

- Para rodar a aplicação localmente, realize o clone do projeto e utilize os comandos a seguir:

```
Para criação do ambiente e instalação das dependências:
<-- na raiz do projeto -->
python3 -m venv .venv // para criar o ambiente virtual
source .venv/bin/activate // para ativar o ambiente virtual
python3 -m pip install -r dev-requirements.txt // instalação das dependências

Para criação de um container do Docker contendo MongoDB, caso necessário:
<-- na raiz do projeto -->
docker-compose up -d
ou
docker run --name mongodb -d -p 27017:27017 mongo

Para para o container criado:
<-- na raiz do projeto -->
docker-compose down
ou
docker stop mongodb

Para rodar a linha de comando da aplicação:
<-- na raiz do projeto -->
tech-news-analyzer // mostrará as opções no terminal
```

### Demonstração

> Comando: `tech-news-analyzer`

```
Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por tag;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.
```
