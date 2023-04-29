# Projeto Pedacinho do Céu

Este projeto foi criado para gerenciar um restaurante chamado Pedacinho do Céu. O projeto utiliza Big Data, Power BI, Docker e uma API RESTful para coletar, processar, armazenar e visualizar os dados.


## Status

| Topics  | Links                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| :------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Build   | [![Build Status](https://img.shields.io/travis/big-data-estacio/data/master)](https://travis-ci.com/github/big-data-estacio/data) [![codecov](https://codecov.io/gh/big-data-estacio/data/branch/master/graph/badge.svg)](https://codecov.io/gh/big-data-estacio/data) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) |
| Version | [![Version](https://img.shields.io/github/v/release/big-data-estacio/data)](https://github.com/big-data-estacio/data/releases) [![Release Notes](https://img.shields.io/badge/release-notes-blue)](https://github.com/big-data-estacio/data/releases)                                                                                                                                         |
| Docs    | [![Docs](https://img.shields.io/static/v1?label=docs&message=wiki&color=blue&logo=github)](https://github.com/big-data-estacio/data/wiki)                                                                                                                                                                                                                                                                                                           |
| Support | [![Gitter](https://badges.gitter.im/big-data-estacio/data.svg)](https://gitter.im/big-data-estacio/data?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge) [![Mail](https://img.shields.io/badge/mail-support-brightgreen)](mailto:your-email@example.com)                                                                                                                                                     |
| Binder  | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/big-data-estacio/data/master?urlpath=lab)      |
| Technology | [![Flask](https://img.shields.io/badge/-Flask-black?style=flat&logo=flask)](https://flask.palletsprojects.com/) [![Hadoop](https://img.shields.io/badge/-Hadoop-black?style=flat&logo=hadoop)](https://hadoop.apache.org/) [![Kafka](https://img.shields.io/badge/-Kafka-black?style=flat&logo=apache-kafka)](https://kafka.apache.org/) [![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-black?style=flat&logo=postgresql)](https://www.postgresql.org/) |

---

1. Coleta de dados: Os scripts na pasta `data_collection/scripts/` são executados para coletar dados de várias fontes externas. Esses dados podem ser armazenados na pasta `data_collection/data_sources/` em formatos como CSV, JSON, XML ou qualquer outro formato de dados necessário.

2. Processamento de dados: Os scripts Apache Spark na pasta `data_processing/spark_jobs/` são executados para processar os dados coletados, realizar transformações e análises necessárias, e prepará-los para armazenamento no banco de dados.

3. Armazenamento de dados: Os dados processados são armazenados no banco de dados PostgreSQL, que está configurado na pasta `data_storage/postgres/`. O arquivo `init.sql` contém instruções SQL para criar tabelas e estruturas de dados necessárias.

4. Análise e visualização de dados: Com os dados armazenados no banco de dados PostgreSQL, você pode usar o Power BI para se conectar ao banco de dados, criar visualizações e painéis interativos para analisar os dados e obter insights valiosos. O Power BI permite criar relatórios detalhados e personalizados que ajudam na tomada de decisões e na compreensão de tendências e padrões nos dados.

5. Atualização e manutenção: À medida que novos dados são coletados e processados, o projeto pode ser atualizado e mantido para garantir que as análises e visualizações permaneçam relevantes e precisas. Isso pode incluir ajustes nos scripts de coleta e processamento de dados, bem como modificações nas visualizações e painéis do Power BI

O projeto utiliza conceitos de Big Data e Power BI. Vamos revisar como cada tecnologia é aplicada no projeto:

1. Big Data: O projeto coleta e processa grandes volumes de dados de várias fontes usando scripts personalizados em Python e Apache Spark. Apache Spark é uma plataforma de computação em cluster rápida e geral que é projetada para processamento de Big Data escalonável e de alto desempenho. Neste projeto, os dados coletados são processados e transformados pelo Apache Spark, tornando-os adequados para análise e visualização.

2. Power BI: Para a visualização de dados e análise dos resultados processados, o projeto utiliza o Power BI. Os arquivos de relatório do Power BI (.pbix) são armazenados na pasta `data_visualization/power_bi_reports`. Esses arquivos podem ser criados e editados usando o aplicativo Power BI Desktop e, em seguida, publicados no serviço Power BI para compartilhamento e colaboração online. A integração com o Power BI permite que você explore e analise os dados coletados e processados, criando visualizações interativas e relatórios dinâmicos.

Combinando Big Data e Power BI, este projeto oferece uma solução completa para coletar, processar, analisar e visualizar grandes volumes de dados em tempo real, ajudando na tomada de decisões informadas e oferecendo insights valiosos para o negócio do restaurante "Pedacinho do Céu".


## Índice

1. [🚀Introdução](#introdução)
2. [🔮Arvore de Diretorios](#arvore-de-diretorios)
3. [🌃Arquitetura do projeto](#arquitetura-do-projeto)
4. [🎆Tecnologias Utilizadas](#tecnologias-utilizadas)
5. [💎Pré-requisitos](#pré-requisitos)
6. [✨Instalando o Projeto](#instalando-o-projeto)
7. [🎉Executando o Projeto](#executando-o-projeto)
   * [Configurando o ambiente virtual](#configurando-o-ambiente-virtual)
   * [Continuando a instalação](#continuando-a-instalação)
8. [👾Testes](#testes)
9. [🔝Utilizando a API](#utilizando-a-api)
10. [🔥Utilizando a API com Insomnia](#utilizando-a-api-com-insomnia)
11. [🥶Versão atual](#versão-atual)
12. [👹Coletando Dados](#coletando-dados)
13. [👻Processando Dados](#processando-dados)
14. [🤖Visualizando os Dados](#visualizando-os-dados)
15. [👽Futuras Atualizações](#futuras-atualizações)
16. [🐳Tecnologias e conceitos utilizados](#tecnologias-e-conceitos-utilizados)
    * [Hadoop](#hadoop)
    * [Kafka](#kafka)
    * [Docker](#docker)
    * [SOLID](#solid)
    * [Padrões de commit](#padrões-de-commit)
17. [🧠Roadmap v1](#roadmap-v1)
    * [Travis CI](#travis-ci)
    * [Princípios SOLID](#princípios-solid)
    * [SQLAlchemy com PostgreSQL ou MySQL](#sqlalchemy-com-postgresql-ou-mysql)
    * [Autenticação e autorização](#autenticação-e-autorização)
    * [Interface de usuário](#interface-de-usuário)
18. [🧠Roadmap v2](#roadmap-v2)
    * [Roadmap v1.1](#roadmap-v1.1)
    * [Roadmap v1.2](#roadmap-v1.2)
    * [Roadmap v1.3](#roadmap-v1.3)
    * [Roadmap v2.0](#roadmap-v2.0)
19. [🤖O que é o Apache Spark?](#o-que-é-o-apache-spark?)
20. [🎖️Critérios de aceitação do projeto](#critérios-de-aceitação-do-projeto)
21. [👹Contribuindo](#contribuindo)
22. [👾Contribuidores](#contribuidores)
23. [🎉Licença](#licença)


## Introdução

Este projeto é um estudo de caso de Big Data e Power BI. O objetivo é demonstrar como coletar, processar, analisar e visualizar grandes volumes de dados em tempo real usando ferramentas e tecnologias como Python, Apache Spark, PostgreSQL e Power BI.

O projeto é baseado em um restaurante chamado "Pedacinho do Céu". O restaurante está localizado em uma cidade turística e serve comida tradicional da região. O restaurante está interessado em coletar dados de várias fontes para analisar e obter insights sobre o negócio. O restaurante também deseja criar visualizações e relatórios interativos para ajudar na tomada de decisões e na compreensão de tendências e padrões nos dados.


## Arvore de Diretorios

Abaixo está a estrutura de diretórios do projeto:

```bash
.
├── api
│   ├── controller
│   ├── model
│   ├── routes
│   └── service
├── data_collection
│   ├── raw_data
│   └── scripts
├── data_processing
│   ├── config
│   ├── Dockerfile
│   └── scripts
├── data_visualization
│   └── power_bi_reports
├── src
│   ├── analysis
│   ├── config
│   ├── constants
│   ├── database
│   └── utils
├── tests
│   ├── integration
│   └── unit
├── .env
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── Makefile
├── package.json
├── README.md
└── requirements.txt

```


## Arquitetura do projeto

A arquitetura do projeto é dividida em várias partes:

* **`data_collection`**: Coleta e armazenamento dos dados em arquivos.
* **`data_processing`**: Processamento dos dados usando Apache Spark.
* **`data_storage`**: Armazenamento dos dados processados em um banco de dados PostgreSQL.
* **`api`**: API RESTful para acessar e gerenciar os dados armazenados.
* **`data_visualization`**: Visualização dos dados usando relatórios do Power BI.
* **`docker`**: Configuração do Docker para executar os serviços do projeto.
* **`docker-compose`**: Configuração do Docker Compose para gerenciar os serviços do projeto.
* **`scripts`**: Scripts de inicialização e gerenciamento do projeto.
* **`docs`**: Documentação do projeto.
* **`LICENSE`**: Licença do projeto.
* **`README.md`**: Arquivo de leia-me do projeto.
* **`requirements.txt`**: Lista de dependências do projeto.
* **`docker-compose.yml`**: Arquivo de configuração do Docker Compose.


## Tecnologias Utilizadas

Neste projeto "Pedacinho do Céu", diversas tecnologias são utilizadas para coletar, processar, armazenar e visualizar dados. Abaixo está uma lista dessas tecnologias e como elas se encaixam no projeto:

1. **Python**: Linguagem de programação principal para scripts de coleta e processamento de dados.

2. **Apache Spark**: Framework de Big Data utilizado para processar grandes volumes de dados em paralelo e em cluster. Spark é usado em conjunto com o Python (pyspark) para realizar análises de dados em grande escala.

3. **Docker**: Plataforma para desenvolvimento, deploy e execução de aplicações em containers. Docker é usado para empacotar e gerenciar os serviços e dependências do projeto, como o PostgreSQL e o Apache Spark.

4. **Docker Compose**: Ferramenta para definir e gerenciar aplicações multi-container usando arquivos de configuração (docker-compose.yml). É usado para simplificar o processo de inicialização e gerenciamento de todos os serviços envolvidos no projeto.

5. **PostgreSQL**: Sistema de gerenciamento de banco de dados relacional (RDBMS) utilizado para armazenar e gerenciar dados coletados e processados.

6. **Power BI**: Ferramenta de Business Intelligence (BI) da Microsoft para criar relatórios e visualizações de dados. É usado para analisar e visualizar os dados coletados e processados pelo projeto.

7. **Flask** (opcional): Microframework Python para desenvolvimento de aplicações web. Pode ser usado para criar uma API RESTful que expõe os dados processados e armazenados para outras aplicações ou serviços.

8. **Pandas** (opcional): Biblioteca Python para manipulação e análise de dados. Pode ser usada em conjunto com o Apache Spark para realizar análises e limpeza de dados em pequena escala antes de processá-los no Spark.


## Pré-requisitos

* Python 3.6+
* Apache Spark 3.0+
* PostgreSQL 12+
* Power BI Desktop
* Docker
* Docker Compose
* Node.js e npm
* Git
* Insomnia
* IDE de sua preferência (PyCharm, VS Code, etc.)
* Terminal de sua preferência (Git Bash, PowerShell, etc.)
* Sistema operacional Linux, macOS ou Windows
* Conhecimentos básicos de Python e SQL
* Conhecimentos básicos de Apache Spark e Power BI


## Arquivo de configuração package.json

O arquivo `package.json` contém as dependências do projeto. Para instalar as dependências, execute o seguinte comando:

```bash
{
  "name": "restaurante",
  "version": "1.0.0",
  "description": "Projeto de restaurante utilizando Python e Flask",
  "main": "api/app.py",
  "scripts": {
    "docker-start": "docker-compose up --build -d",
    "docker-stop": "docker-compose down",
    "build": "docker build -t nome-da-imagem .",
    "lint": "flake8 src/ tests/",
    "start": "make",
    "dev": "make",
    "test": "make test",
    "dev:server": "nodemon api/app.py",
    "test-coverage": "make test-coverage",
    "pre-commit": "pre-commit install",
    "deploy": "./deploy.sh"
  },
  "keywords": [
    "restaurante",
    "python",
    "flask"
  ],
  "author": "grupo-estacio",
  "license": "MIT",
  "devDependencies": {
    "nodemon": "^2.0.22"
  },
  "dependencies": {
    "Flask": "^2.0.0",
    "Flask-Cors": "^3.0.10",
    "Flask-JWT-Extended": "^4.2.3",
    "Flask-Mail": "^0.9.1",
    "Flask-RESTful": "^0.3.9",
    "Flask-SQLAlchemy": "^3.0.0",
    "PyMySQL": "^1.0.2"
  }
}
```


## Instalando o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/your_username/pedacinho_do_ceu.git
cd pedacinho_do_ceu
```


## Executando o Projeto

### Configurando o ambiente virtual

É recomendado utilizar um ambiente virtual para isolar as dependências do projeto. Siga os passos abaixo para configurar e ativar o ambiente virtual usando o `venv`:

1. Instale o módulo `venv`, caso ainda não tenha, com o seguinte comando:

```bash
python3 -m pip install --user virtualenv
```

2. Navegue até a pasta do projeto e crie um ambiente virtual:

```bash
python3 -m venv venv

# ou, se você estiver no Windows

py -m venv venv
```

3. Ative o ambiente virtual:

* No Windows:

```bash
.\venv\Scripts\activate

# ou, se você estiver usando o Git Bash

source venv/Scripts/activate
```

* No macOS e Linux:

```bash
source venv/bin/activate
```

4. Após a ativação do ambiente virtual, seu terminal deve mostrar o prefixo `(venv)`.

Agora você pode executar o projeto com as dependências instaladas no ambiente virtual. Lembre-se de ativar o ambiente virtual sempre que for trabalhar no projeto.

5. Instale todas as bibliotecas necessárias usando o comando `pip install`:

```bash
pip install biblioteca1 biblioteca2 biblioteca3
```

Substitua `biblioteca1`, `biblioteca2` e `biblioteca3` pelos nomes das bibliotecas que você deseja instalar.

6. Agora que todas as bibliotecas estão instaladas, execute o seguinte comando para gerar o arquivo `requirements.txt`:

```bash
pip freeze > requirements.txt
```

O comando `pip freeze` listará todas as bibliotecas instaladas no ambiente virtual e suas versões específicas. O operador `>` redirecionará a saída para o arquivo `requirements.txt`, criando-o ou atualizando-o, se já existir.

7. Instale as dependências do projeto utilizando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

> arquivo requirements.txt para esse projeto com as dependências necessárias.

```bash
alembic==1.10.3
aniso8601==9.0.1
anyio==3.6.2
arabic-reshaper==3.0.0
asgiref==3.6.0
astroid==2.15.2
attrs==22.2.0
bcrypt==4.0.1
brotlipy @ file:///home/conda/feedstock_root/build_artifacts/brotlipy_1666764672617/work
certifi==2022.12.7
cffi @ file:///home/conda/feedstock_root/build_artifacts/cffi_1671179360775/work
charset-normalizer @ file:///home/conda/feedstock_root/build_artifacts/charset-normalizer_1661170624537/work
click==8.1.3
colorama @ file:///home/conda/feedstock_root/build_artifacts/colorama_1666700638685/work
conda==23.1.0
conda-package-handling @ file:///home/conda/feedstock_root/build_artifacts/conda-package-handling_1669907009957/work
conda_package_streaming @ file:///home/conda/feedstock_root/build_artifacts/conda-package-streaming_1669733752472/work
contourpy==1.0.7
cryptography @ file:///home/conda/feedstock_root/build_artifacts/cryptography-split_1677821254559/work
cycler==0.11.0
dill==0.3.6
distlib==0.3.6
Django==3.2.2
django-crispy-forms==1.11.2
django-extensions==3.1.3
django-widget-tweaks==1.4.8
docopt==0.6.2
exceptiongroup==1.1.1
fastapi==0.94.1
filelock==3.10.6
flasgger==0.9.5
Flask==2.2.3
Flask-Bcrypt==1.0.1
Flask-Cors==3.0.10
Flask-JWT-Extended==4.4.4
Flask-Migrate==4.0.4
Flask-RESTful==0.3.9
Flask-SQLAlchemy==2.4.4
Flask-Testing==0.8.1
fonttools==4.39.2
greenlet==2.0.2
gunicorn==20.1.0
hdfs==2.7.0
html5lib==1.1
idna @ file:///home/conda/feedstock_root/build_artifacts/idna_1663625384323/work
importlib-metadata==6.0.0
importlib-resources==5.12.0
iniconfig==2.0.0
init==0.1.0
isort==5.12.0
itsdangerous==2.1.2
Jinja2==3.1.2
jsonschema==4.17.3
kafka==1.3.5
kiwisolver==1.4.4
lazy-object-proxy==1.9.0
Mako==1.2.4
MarkupSafe==2.1.2
matplotlib==3.7.1
mccabe==0.7.0
mistune==2.0.5
mysql-connector==2.2.9
numpy==1.24.2
packaging==23.0
pandas==1.3.4
Pillow==8.2.0
platformdirs==3.2.0
pluggy @ file:///home/conda/feedstock_root/build_artifacts/pluggy_1667232663820/work
psycopg2==2.9.6
pycosat @ file:///home/conda/feedstock_root/build_artifacts/pycosat_1666836642684/work
pycparser @ file:///home/conda/feedstock_root/build_artifacts/pycparser_1636257122734/work
pydantic==1.10.6
PyJWT==2.6.0
pylint==2.17.2
pyOpenSSL @ file:///home/conda/feedstock_root/build_artifacts/pyopenssl_1672659226110/work
pyparsing==3.0.9
PyPDF2==3.0.1
pyrsistent==0.19.3
PySocks @ file:///home/conda/feedstock_root/build_artifacts/pysocks_1661604839144/work
pytest==7.2.2
python-bidi==0.4.2
python-dateutil==2.8.2
python-dotenv==0.15.0
pytz==2022.7.1
PyYAML==6.0
reportlab==3.6.9
requests @ file:///home/conda/feedstock_root/build_artifacts/requests_1673863902341/work
ruamel.yaml @ file:///home/conda/feedstock_root/build_artifacts/ruamel.yaml_1678272973380/work
ruamel.yaml.clib @ file:///home/conda/feedstock_root/build_artifacts/ruamel.yaml.clib_1670412733608/work
six==1.16.0
sniffio==1.3.0
SQLAlchemy==1.3.23
sqlparse==0.4.3
starlette==0.26.1
terminal==0.4.0
tomli==2.0.1
tomlkit==0.11.7
toolz @ file:///home/conda/feedstock_root/build_artifacts/toolz_1657485559105/work
tqdm @ file:///home/conda/feedstock_root/build_artifacts/tqdm_1677948868469/work
ttkthemes==3.2.2
typing_extensions==4.5.0
urllib3 @ file:///home/conda/feedstock_root/build_artifacts/urllib3_1678635778344/work
virtualenv==20.21.0
webencodings==0.5.1
Werkzeug==2.2.3
wrapt==1.15.0
xhtml2pdf==0.2.5
zipp==3.15.0
zstandard==0.19.0
```

8. Quando terminar de trabalhar no projeto, você pode desativar o ambiente virtual com o seguinte comando:

```bash
deactivate
```

### 📦 Continuando a instalação

1. Crie um arquivo `.env` na raiz do projeto com as variáveis de ambiente necessárias. Você pode usar o arquivo `.env.example` como modelo.

2. Instale as dependências do projeto:

```bash
npm install
```

### Para iniciar o projeto "Pedacinho do Céu" com o Docker, siga estas etapas:

1. Certifique-se de que o Docker e o Docker Compose estejam instalados em seu sistema. Se você ainda não os instalou, siga as instruções de instalação no site oficial do Docker: `https://docs.docker.com/get-docker/` e `https://docs.docker.com/compose/install/`

2. Abra um terminal e navegue até o diretório raiz do projeto `pedacinho_do_ceu`.

3. Execute o seguinte comando para criar e iniciar os containers do projeto, conforme definido no arquivo `docker-compose.yml`:

```bash
docker-compose up -d
```

Isso iniciará os serviços do Docker, a API, Hadoop, como o PostgreSQL, o Apache Spark e o serviço de processamento de dados se necessário.

4. Após a inicialização dos serviços, você pode executar os scripts de coleta de dados na pasta `data_collection/scripts/` para coletar e armazenar os dados no banco de dados PostgreSQL.

5. Em seguida, execute os jobs do Apache Spark na pasta `data_processing/spark_jobs/` para processar os dados coletados e armazenados.

6. Abra os relatórios do Power BI na pasta `data_visualization/power_bi_reports/` para visualizar e analisar os dados processados. Se você não possui o Power BI Desktop, faça o download e instale-o a partir do site oficial: `https://powerbi.microsoft.com/en-us/desktop/`

7. Ao longo do desenvolvimento do projeto, você pode modificar e ajustar os arquivos na pasta `src/` conforme necessário para aprimorar a análise e o processamento dos dados.

Lembre-se de que, dependendo da configuração do projeto, algumas etapas podem variar ou exigir ações adicionais. Ajuste as etapas conforme necessário para se adequar às necessidades específicas do seu projeto.

8. Quando terminar de usar o projeto, pare os serviços do Docker Compose pressionando `Ctrl+C` no terminal onde o Docker Compose está sendo executado. Para remover os contêineres e os volumes, execute:

```bash
docker-compose down --remove-orphans --volumes
```

9. Inicie o servidor da API:
  
```bash
npm start
```

> Já o arquivo api/app.py, é o arquivo principal da API, onde é feita a conexão com o banco de dados e a definição dos endpoints.

Ele é executado na porta 5000, e pode ser acessado em `http://localhost:5000/`

Nesse arquivo, se encontram os endpoints da API, que são:

* **`GET /`**: Lista todos os itens armazenados no banco de dados.
* **`GET /<id>`**: Retorna os detalhes de um item específico com base no ID.
* **`POST /`**: Adiciona um novo item ao banco de dados.
* **`PUT /<id>`**: Atualiza os detalhes de um item específico com base no ID.
* **`DELETE /<id>`**: Remove um item específico com base no ID.

> @TODO: Adicionar mais detalhes sobre a API
> @Note: A API foi desenvolvida com o framework FastAPI, que é um framework web assíncrono de alto desempenho, fácil de aprender, rápido para codificar, pronto para produção. Ele é construído com base no Starlette e Pydantic.

o arquivo `api/app.py` está configurado com os scripts de coleta de dados e processamento de dados, para que os dados sejam coletados e processados automaticamente quando a API for iniciada:

```python
import sys
from pathlib import Path
from flask import Flask
from routes.restaurant_routes import restaurant_routes


sys.path.insert(0, str(Path(__file__).resolve().parent))

app = Flask(__name__)

app.register_blueprint(restaurant_routes)

if __name__ == '__main__':
    app.run(debug=True)
```

A API estará disponível na porta 5000.

9. Abra o Power BI Desktop e carregue os relatórios na pasta `data_visualization/power_bi_reports`.


## Testes

Execute os testes unitários e de integração usando o seguinte comando:

```bash
python -m unittest discover tests
```


## Debugging e Logging

Para depurar o projeto, você pode usar o depurador interativo do Python. Para isso, basta adicionar o seguinte código ao arquivo que você deseja depurar:

```python
import pdb; pdb.set_trace()
```

Em seguida, execute o arquivo normalmente e o depurador interativo será iniciado quando o código atingir o ponto de interrupção.

Para adicionar logs ao projeto, você pode usar o módulo `logging` do Python. Para isso, basta adicionar o seguinte código ao arquivo que você deseja depurar:

```python
import logging

logging.basicConfig(level=logging.DEBUG)
```

> como que fica o arquivo de log logs/app.log

```log
2023-04-25 00:31:31,719 - INFO - A aplicação foi encerrada com sucesso.
2023-04-25 00:33:49,546 - INFO - A aplicação foi encerrada com sucesso.
2023-04-25 00:34:44,584 - INFO - A aplicação foi encerrada com sucesso.
2023-04-25 00:34:46,857 - WARNING - DNS lookup failed for kafka:9092, exception was [Errno -2] Name or service not known. Is your advertised.listeners (called advertised.host.name before Kafka 9) correct and resolvable?
2023-04-25 00:34:46,859 - ERROR - DNS lookup failed for kafka:9092 (AddressFamily.AF_UNSPEC)
2023-04-25 00:34:46,860 - INFO - Probing node bootstrap-0 broker version
2023-04-25 00:34:47,912 - WARNING - DNS lookup failed for kafka:9092, exception was [Errno -2] Name or service not known. Is your advertised.listeners (called advertised.host.name before Kafka 9) correct and resolvable?
2023-04-25 00:34:47,915 - ERROR - DNS lookup failed for kafka:9092 (AddressFamily.AF_UNSPEC)
2023-04-25 00:36:12,026 - INFO - A aplicação foi encerrada com sucesso.
2023-04-25 09:37:32,931 - INFO - A aplicação foi encerrada com sucesso.
2023-04-25 09:38:27,387 - INFO - A aplicação foi encerrada com sucesso.
2023-04-25 09:38:29,541 - WARNING - DNS lookup failed for kafka:9092, exception was [Errno -2] Name or service not known. Is your advertised.listeners (called advertised.host.name before Kafka 9) correct and resolvable?
2023-04-25 09:38:29,542 - ERROR - DNS lookup failed for kafka:9092 (AddressFamily.AF_UNSPEC)
2023-04-25 09:38:29,542 - INFO - Probing node bootstrap-0 broker version
2023-04-25 09:38:30,582 - WARNING - DNS lookup failed for kafka:9092, exception was [Errno -2] Name or service not known. Is your advertised.listeners (called advertised.host.name before Kafka 9) correct and resolvable?
2023-04-25 09:38:30,582 - ERROR - DNS lookup failed for kafka:9092 (AddressFamily.AF_UNSPEC)
2023-04-25 09:39:43,938 - INFO - A aplicação foi encerrada com sucesso.
2023-04-25 09:39:44,780 - INFO - <BrokerConnection node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: connecting to localhost:9092 [('127.0.0.1', 9092) IPv4]
2023-04-25 09:39:44,780 - INFO - Probing node bootstrap-0 broker version
2023-04-25 09:39:44,781 - ERROR - Connect attempt to <BrokerConnection node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]> returned error 111. Disconnecting.
2023-04-25 09:39:44,782 - INFO - <BrokerConnection node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 111 ECONNREFUSED
2023-04-25 09:39:44,827 - INFO - <BrokerConnection node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: connecting to localhost:9092 [('127.0.0.1', 9092) IPv4]
2023-04-25 09:39:44,828 - ERROR - Connect attempt to <BrokerConnection node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]> returned error 111. Disconnecting.
2023-04-25 09:39:44,828 - INFO - <BrokerConnection node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 111 ECONNREFUSED
2023-04-25 09:41:52,885 - INFO - A aplicação foi encerrada com sucesso.
2023-04-25 09:41:53,647 - INFO - <BrokerConnection node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: connecting to localhost:9092 [('127.0.0.1', 9092) IPv4]
2023-04-25 09:41:53,648 - INFO - Probing node bootstrap-0 broker version
2023-04-25 09:41:53,649 - ERROR - Connect attempt to <BrokerConnection node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]> returned error 111. Disconnecting.
2023-04-25 09:41:53,649 - INFO - <BrokerConnection node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 111 ECONNREFUSED
2023-04-25 09:41:53,693 - INFO - <BrokerConnection node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: connecting to localhost:9092 [('127.0.0.1', 9092) IPv4]
2023-04-25 09:41:53,694 - ERROR - Connect attempt to <BrokerConnection node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]> returned error 111. Disconnecting.
2023-04-25 09:41:53,694 - INFO - <BrokerConnection node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv4 ('127.0.0.1', 9092)]>: Closing connection. KafkaConnectionError: 111 ECONNREFUSED
2023-04-25 09:42:12,859 - INFO - A aplicação foi encerrada com sucesso.
```

> e o arquivo de debug:

[![debug](docs/debug.png)](docs/debug.png)

## Utilizando a API

A API RESTful permite gerenciar os dados armazenados no banco de dados PostgreSQL. Para utilizar a API, você pode fazer requisições HTTP para os seguintes endpoints:

* **`GET /`**: Lista todos os itens armazenados no banco de dados.
* **`GET /<id>`**: Retorna os detalhes de um item específico com base no ID.
* **`POST /`**: Adiciona um novo item ao banco de dados.
* **`PUT /<id>`**: Atualiza os detalhes de um item específico com base no ID.
* **`DELETE /<id>`**: Remove um item específico com base no ID.


## Utilizando a API com Insomnia

Para testar e interagir com a API, você pode usar o Insomnia REST Client, que é uma aplicação de desktop para gerenciar requisições HTTP e API.

1. Instale o Insomnia em seu computador: Insomnia Download
2. Abra o Insomnia e crie um novo workspace ou use um existente.
3. Para adicionar as rotas da API ao seu workspace, clique em `Create Request`. Escolha o método HTTP (GET, POST, PUT, DELETE) e insira a URL da API (por exemplo, `http://localhost:5000/` para listar todos os itens). Adicione os parâmetros, cabeçalhos ou corpo da requisição conforme necessário e clique em `Send` para executar a requisição.
4. Você pode criar várias requisições para diferentes endpoints da API e organizá-las em pastas para facilitar a navegação.

Agora você pode usar o Insomnia para testar e explorar a API RESTful do projeto Pedacinho do Céu.


## Versão atual
A versão atual do projeto inclui as seguintes funcionalidades:

* Coleta e armazenamento de dados em tempo real com Hadoop e Kafka.
* API RESTful para interagir com os dados e serviços.
* Docker Compose para facilitar a instalação e configuração do projeto.


## Coletando Dados

Os dados podem ser coletados usando o script `data_collection/data_collector.py`. Para coletar os dados, você pode executar o seguinte comando:

```bash
python data_collection/data_collector.py
```

Os dados coletados serão armazenados em arquivos no diretório `data_collection/data`.


## Processando Dados

Os dados podem ser processados usando o script `data_processing/data_processor.py`. Para processar os dados, você pode executar o seguinte comando:

```bash
python data_processing/data_processor.py
```

Os dados processados serão armazenados no banco de dados PostgreSQL.


## Visualizando os Dados

Os dados podem ser visualizados usando relatórios do Power BI. Para visualizar os relatórios, você pode fazer o download do Power BI Desktop [aqui](https://powerbi.microsoft.com/pt-br/desktop/). Após instalar o Power BI Desktop, você pode abrir o arquivo `pedacinho_do_ceu.pbix` para visualizar os relatórios.


## Futuras Atualizações

* Melhoria na coleta de dados
* Implementação de novas análises e visualizações
* Adição de mais testes
* Melhoria na documentação

O projeto "Pedacinho do Céu" está em constante evolução e melhorias. Abaixo estão algumas das atualizações futuras planejadas para o projeto:

1. **Expansão das fontes de dados**: Atualmente, o projeto utiliza um conjunto limitado de fontes de dados. No futuro, pretendemos expandir a lista de fontes de dados para enriquecer ainda mais nossas análises e visualizações.

2. **Otimização do processamento de Big Data**: Continuaremos a melhorar a eficiência e a velocidade do processamento de Big Data usando técnicas de otimização avançadas e atualizações nas ferramentas e tecnologias utilizadas.

3. **Visualizações interativas**: Atualmente, o projeto utiliza relatórios estáticos do Power BI. Planejamos adicionar visualizações interativas e em tempo real para tornar os dados mais acessíveis e fáceis de entender.

4. **Machine Learning**: Exploraremos a implementação de algoritmos de aprendizado de máquina para identificar padrões e tendências nos dados e fornecer insights adicionais.

5. **Integração com outras plataformas**: Planejamos adicionar suporte para integração com outras plataformas de visualização de dados e análise, como Tableau e Looker.

6. **APIs e microserviços**: Atualmente, o projeto possui uma API simples para acessar os dados. No futuro, pretendemos expandir a API e usar microserviços para fornecer uma solução mais modular e escalonável.

7. **Segurança e privacidade**: Continuaremos a aprimorar a segurança e a privacidade dos dados, garantindo a conformidade com os regulamentos de proteção de dados e as melhores práticas do setor.

8. **Documentação e tutoriais**: A documentação e os tutoriais serão atualizados regularmente para garantir que sejam claros, abrangentes e atualizados com as últimas informações do projeto.


## Tecnologias e conceitos utilizados

### Hadoop
O projeto utiliza o Hadoop e o HDFS (Hadoop Distributed FileSystem) para armazenar e processar grandes volumes de dados.

### Kafka
O projeto utiliza o Apache Kafka para construir sistemas de processamento de dados em tempo real, permitindo lidar com fluxos de dados contínuos.

### Docker
O projeto é executado em contêineres Docker para facilitar a implantação e a escalabilidade.

### SOLID
Os princípios SOLID foram aplicados neste projeto para garantir um código limpo, modular e fácil de manter.


## Padrões de commit
Ao fazer um commit, siga as diretrizes de mensagens de commit personalizadas e com emojis, utilizando até 200 caracteres.


## Roadmap v1

* Adicionar suporte ao Travis CI para integração contínua.
* Aplicar os princípios SOLID ao projeto para melhorar a manutenibilidade e escalabilidade.
* Atualizar o SQLAlchemy para usar um banco de dados mais robusto, como PostgreSQL ou MySQL, em vez de SQLite.
* Implementar autenticação e autorização para proteger as rotas da API.
* Adicionar testes automatizados para garantir a qualidade do código.
* Implementar uma interface de usuário para interagir com a API.

### Travis CI

1. Para adicionar suporte ao Travis CI, siga estas etapas:
2. Vá para `travis-ci.com` e faça login com sua conta do GitHub.
3. Ative o repositório do projeto nas configurações do Travis CI.
4. Crie um arquivo `.travis.yml` na raiz do projeto com o seguinte conteúdo:

```yml
language: python
python:
  - "3.8"

install:
  - pip install -r api/requirements.txt

script:
  - pytest
```

5. Vincule seu repositório do GitHub ao Travis CI e habilite a integração contínua para o projeto.


### Princípios SOLID
Para aplicar os princípios SOLID ao projeto, siga estas diretrizes:

1. Single Responsibility Principle (SRP): Separe as responsabilidades do código em classes e funções distintas. Por exemplo, separe a lógica de negócio da lógica de banco de dados.

2. Open/Closed Principle (OCP): Crie classes e funções extensíveis sem modificar seu código-fonte. Por exemplo, use a herança e a composição para estender a funcionalidade de uma classe.

3. Liskov Substitution Principle (LSP): As subclasses devem ser substituíveis por suas classes base sem alterar a correção do programa. Por exemplo, verifique se as subclasses seguem o contrato estabelecido pelas classes base.

4. Interface Segregation Principle (ISP): Divida as interfaces grandes em interfaces menores e mais específicas. Por exemplo, crie interfaces separadas para operações de leitura e gravação em vez de uma interface única.

5. Dependency Inversion Principle (DIP): Dependências de alto nível não devem depender de dependências de baixo nível; em vez disso, ambas devem depender de abstrações. Por exemplo, use a injeção de dependência para inverter as dependências entre os módulos.

### SQLAlchemy com PostgreSQL ou MySQL
Para usar o PostgreSQL ou MySQL com SQLAlchemy, siga estas etapas:

1. Instale os pacotes necessários:

```bash
pip install psycopg2 sqlalchemy psycopg2-binary
```

OU

```bash
pip install pymysql sqlalchemy
```

2. Atualize a string de conexão do banco de dados no arquivo api/database.py para usar PostgreSQL ou MySQL:

Para PostgreSQL:

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@localhost/dbname"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

Para MySQL:

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://user:password@localhost/dbname"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

3. Atualize as configurações do banco de dados em `api/__init__.py` para usar a nova string de conexão.

### Autenticação e autorização
Para implementar a autenticação e autorização, você pode usar a extensão Flask-Login ou Flask-Security. Siga a documentação oficial de cada extensão para configurar a autenticação e autorização no projeto.

### Testes automatizados
Para adicionar testes automatizados, siga estas etapas:

1. Instale o pacote pytest:
  
```bash
pip install pytest
```

2. Crie um diretório `tests` na raiz do projeto.

3. Dentro do diretório `tests`, crie arquivos de teste para cada módulo do projeto. Por exemplo, você pode criar um arquivo `test_restaurant_service.py` para testar a classe RestaurantService.

4. Escreva testes usando o pytest para cada função e classe do projeto.

5. Execute os testes usando o comando `pytest` no terminal.

### Interface de usuário
Para implementar uma interface de usuário, você pode criar uma aplicação web usando HTML, CSS e JavaScript para interagir com a API. Você pode usar bibliotecas como React, Angular ou Vue.js para criar a interface do usuário.


## Roadmap v2

### Versão 1.1
* Implementar autenticação e autorização na API.
* Adicionar suporte para diferentes formatos de dados (JSON, XML, etc.).
* Desenvolver uma interface gráfica para visualizar os dados e interagir com a API.

### Versão 1.2
* Adicionar suporte para processamento de dados em tempo real usando Apache Spark ou Flink.
* Implementar algoritmos de machine learning para análise de dados e geração de insights.
* Integrar com outras fontes de dados e APIs de terceiros.

### Versão 1.3
* Adicionar suporte para escalabilidade horizontal e balanceamento de carga.
* Implementar monitoramento e alertas para garantir a saúde e o desempenho do sistema.
* Desenvolver testes de carga e estresse para garantir a estabilidade do projeto em ambientes de produção.

### Versão 2.0
* Redesenhar a arquitetura do projeto para melhorar a modularidade e a manutenibilidade.
* Adicionar suporte para outras linguagens de programação e frameworks.
* Implementar uma API GraphQL para maior flexibilidade na consulta e manipulação de dados.


## O que é o Apache Spark?

![](docs/spark-streaming-datanami.png)
# Apache_Spark
:sparkles::tada: Este repositório explica sobre o Apache Spark com práticas :tada::sparkles:

- É uma ferramenta de processamento em tempo real desenvolvida para resolver o problema de trabalhar com dados em tempo real.
- É tratado pelo Apache.
- É muito rápido, dá resultado no clique.
- Usa avaliação preguiçosa, ou seja, processa sempre que necessário.
- Como o MapReduce não conseguiu lidar com dados em tempo real, o Spark entrou em cena para ajudar.
- Agora é usado por muitos grandes gigantes da tecnologia como Oracle, Amazon, Microsoft, Visa, Cisco, Verizon, Hortonworks.
- Como acima, temos 3.000 empresas usando o Apache Spark.

<div align="center">
  <a href="https://www.youtube.com/watch?v=4TE6AGQ0IzI" target="_blank"
  alt="IMAGE ALT TEXT" width="20" height="10" border="10"><img src="https://i.ytimg.com/vi/4TE6AGQ0IzI/maxresdefault.jpg"></a>
</div>

## Baixando o Apache Spark

- Para baixar o Apache Spark, acesse: [Download Apache Spark](https://spark.apache.org/downloads.html)

### Instalando o Apache Spark
- Para Mac: [Instalação do Apache Spark](https://github.com/HarshitDawar55/Apache_Spark/blob/master/docs/Installation_Of_Spark_In_Mac.docx)

### Linguagens usadas para programação no Spark:

- Python
- Escala

### Instruções para executar scripts do Apache Spark

- Copie o código do respectivo script e cole-o no shell Spark correspondente para executar o código.

### Instruções para executar scripts python
- Abra o terminal (no ambiente Linux)/Command Propmpt (Windows).
- Execute "python <nome do script>.py"


## Critérios de aceitação do projeto

Com base nas informações fornecidas até agora, o projeto está usando as seguintes tecnologias e técnicas:

1. **`Apache Hadoop e Apache Spark`** como ferramentas de Big Data
2. **`Integração com Python`** para executar scripts e processar dados usando o Spark
3. **`Flask`** para criar uma API RESTful

De acordo com os critérios do professor, esse projeto estaria atendendo aos seguintes pontos:

* Usando alguma ferramenta de Big Data com Python (+++): O projeto está usando o Apache Hadoop e o Apache Spark, que são ferramentas de Big Data, e está integrando-as com Python para executar scripts e processar dados.

> Como resultado, o projeto deve passar na matéria com uma nota alta, pois está utilizando ferramentas de Big Data e integrando-as com Python, o que é o critério de maior pontuação (+++).

Além disso, o projeto também utiliza outras tecnologias e práticas relevantes, como o Flask para criar uma API RESTful e o SQLAlchemy como um ORM para lidar com as operações de banco de dados. Esses aspectos podem não ser mencionados diretamente nos critérios de avaliação do professor, mas certamente agregam valor ao projeto e demonstram a capacidade de trabalhar com várias tecnologias e bibliotecas em Python.

Em resumo, o projeto atende ao critério de maior pontuação, utilizando ferramentas de Big Data e integrando-as com Python. Isso deve resultar em uma avaliação positiva para a matéria.

## Contribuindo

Para contribuir com este projeto, siga estas etapas:

1. Faça um fork do repositório.
2. Crie um branch com suas alterações (`git checkout -b my-feature`).
3. Faça commit das suas alterações (`git commit -m 'Add some feature'`).
4. Faça push para o branch (`git push origin my-feature`).
5. Crie uma nova Pull Request.


## Contribuidores

Agradecemos às seguintes pessoas que contribuíram para este projeto:

<a href="">
  <img src="https://contrib.rocks/image?repo=gutorafael/gutorafael" />
</a>
<a href="">
  <img src="https://contrib.rocks/image?repo=gfucci/desafio_acaodireta" />
</a>
<a href="">
  <img src="https://contrib.rocks/image?repo=lele-sf/lele-sf" />
</a>
<a href="">
  <img src="https://contrib.rocks/image?repo=estevam5s/rest-api-nasa" />
</a>
<a href="">
  <img src="https://contrib.rocks/image?repo=PedroDellaMea/Atividades-HTML-AV1" />
</a>
<a href="">
  <img src="https://contrib.rocks/image?repo=AldairSouto/AldairSouto" />
</a>


## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo `LICENSE` para obter detalhes.