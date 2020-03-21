# Serasa Consumidor - Teste para Web Scrapping
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
[![Python](https://img.shields.io/badge/python-3.7-blue.svg)]()
[![Scrapy](https://img.shields.io/badge/scrapy-2.0-red.svg)]()
[![Scrapy](https://img.shields.io/badge/mongoDB-green.svg)]()

## Introdução

Primeiramente gostaria de avisar que não pude fazer com uma empresa que  
emita boletos, porém vou aplicar os mesmos conceitos para um outro exemplo.
Eu vou utilizar o site: [http://quotes.toscrape.com/](http://quotes.toscrape.com/), que é um site
desenvolvido pela própria ScrapingHub para esse tipo de teste.


## Código

1. Inicie a API em Flask pelo terminal:

    ```sh
    $ cd api
    $ python3.7 -m venv env
    $ source env/bin/activate
    (env)$ pip install -r requirements.txt
    (env)$ python3 run.py
    ```

    Accesse o endereço [http://localhost:5000/api/v1/docs](http://localhost:5000/api/v1/docs)



2. Você também pode iniciar o crawler sem iniciar a API. Navegue até a raiz do projeto e abra o terminal:

    ```sh
    $ scrapy crawl quotes
    ```

3. Ou iniciar utilizando Docker:

    ```
    $ docker build -t crawler-app .
    $ docker run -d \
    --name crawler-app \
    -p 5000:5000 \
    -e MONGO_URI="<mongodb://<your_mongo_host>:27017/<your_database>" \
    crawler-app 
    ```

## Swagger

Após a aplicação iniciar, abra seu navegador em `localhost:5000/api/v1/docs`  
 para ver a autodocumentação da API:

![](/screenshot.png)


### Pastas
* `quotes/app` - Toda a implementação do Crawler está aqui.
* `api/app` - Toda a implementação do RESTful API está aqui.
* `api/app/v1` - Agrupamento de recursos para todos os `v1` [Namespaces](https://flask-restplus.readthedocs.io/en/stable/scaling.html#multiple-namespaces).


## Testes

Existem dois tipos de testes na aplicação. O primeiro são os
[Spiders Contracts](https://docs.scrapy.org/en/latest/topics/contracts.html). Acesse a pasta raiz do projeto
pelo terminal:
    ```
    $ scrapy check
    ```

O segundo é o teste da própria API.

    ```
    $ cd api
    $ pytest 
    ```
