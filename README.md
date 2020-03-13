# Serasa Consumidor - Teste para Web Scrapping
[![Python](https://img.shields.io/badge/python-3.7-blue.svg)]()
[![Scrapy](https://img.shields.io/badge/scrapy-2.0-red.svg)]()
[![Scrapy](https://img.shields.io/badge/mongoDB-green.svg)]()

- Escolha uma empresa do seu dia a dia (internet, telefone, energia...) que possua um sistema web com **autenticação**
- Acesse o sistema (não é necessario ter recapcha) via crawler
- Busque todas as faturas disponiveis e salve em uma base local
- Agende uma nova busca baseada em alguma regra (proxima fatura, proximo vencimento...) para uma nova sincronização

### Requisitos mínimos para o teste

- Uma API para cadastro de novos acessos (usuario e senha)
- Uma API para forçar uma nova varredura de faturas (sync)
- Uma API para retornar as faturas que foram encontradas
- Persistência dos acessos dos usuarios **criptografados**
- Persistência das faturas com status, valor, data de vencimento e data de pagamento
- Documentação de setup e do funcionamento do sistema
- Um crawler para extrair faturas de uma determinada empresa
- Um processo que rode de tempos em tempos realizando um novo sync dos dados

### Critérios de avaliação

- Arquitetura do crawler e facilidade de integrar com outras empresas (abstração)
- Utilização de containers Docker
- API seguindo os padrões REST
- Código testável e demonstrar isso escrevendo testes
- Melhores práticas para segurança de APIs e dados
- Diretizes de estilo de código
- Banco de dados escolhido
- Você **NÃO** precisa desenvolver um "frontend" (telas) para esse teste

# Resolução do Exercício

## Introdução

Primeiramente gostaria de avisar que não pude fazer com uma empresa  
que emita boletos, porém vou aplicar os mesmos conceitos para um outro exemplo.
Eu vou utilizar o site: [http://quotes.toscrape.com/](http://quotes.toscrape.com/), que é um site
desenvolvido pela própria ScrapingHub para esse tipo de teste.


## Código

1. Run the server-side Flask app in one terminal window:

    ```sh
    $ cd api
    $ python3.7 -m venv env
    $ source env/bin/activate
    (env)$ pip install -r requirements.txt
    (env)$ python3 run.py
    ```

    Navigate to [http://localhost:5000/api/v1/docs](http://localhost:5000/api/v1/docs)


2. Você também pode iniciar o crawler sem iniciar a API. Navegue até a raiz do projeto:

    ```sh
    $ scrapy crawl quotes
    ```

## Docker
### Build

```
docker build -t flask-app .
```

### Start a New Container

```
docker run -d \
--name flask-app \
-p 5000:5000 \
-e MONGO_URI="<mongodb://<your_mongo_host>:27017/<your_database>" \
flask-app
```

## Swagger

After the application goes up, open your browser on `localhost:5000/api/v1/docs` to see the self-documented interactive API:

![](/screenshot.png)


## Project Structure1

The project structure is based on the official [Scaling your project](https://flask-restplus.readthedocs.io/en/stable/scaling.html#multiple-apis-with-reusable-namespaces) doc with some adaptations (e.g `v1` folder to agroup versioned resources).


```
.

```

### Folders

* `app` - All the RESTful API implementation is here.
* `app/helpers` - Useful function/class helpers for all modules.
* `app/v1` - Resource agroupment for all `v1` [Namespaces](https://flask-restplus.readthedocs.io/en/stable/scaling.html#multiple-namespaces).
* `app/v1/resources` - All `v1` resources are implemented here.
* `tests/unit` - Unit tests modules executed on the CI/CD pipeline.
* `tests/integration` - Integration tests modules executed using a fake database on the CI/CD pipeline.
* `tests/fake_data` - Fake data files ("fixtures").

### Files

* `app/__init__.py` - The Flask Application factory (`create_app()`) and it's configuration are done here. Your [Blueprints](https://flask-restplus.readthedocs.io/en/stable/scaling.html#use-with-blueprints) are registered here.
* `app/v1/__init__.py` - The Flask RESTPlus API is created here with the versioned Blueprint (e.g `v1`). Your [Namespaces](https://flask-restplus.readthedocs.io/en/stable/scaling.html#multiple-namespaces) are registered here.
* `config.py` - Config file for envs, global config vars and so on.
* `Dockerfile` - Dockerfile used to build a Docker image (using [Docker Multistage Build](https://docs.docker.com/develop/develop-images/multistage-build/))
* `LICENSE` - MIT License, i.e. you are free to do whatever is needed with the given code with no limits.
* `tox.ini` - Config file for tests using [Tox](https://tox.readthedocs.io/en/latest/index.html).
* `.dockerignore` - Lists files and directories which should be ignored while Docker build process.
* `.gitignore` - Lists files and directories which should not be added to git repository.
* `requirements.txt` - All project dependencies.
* `run.py` - The Application entrypoint.
* `conftest.py` - Common pytest [fixtures](https://docs.pytest.org/en/latest/fixture.html).

