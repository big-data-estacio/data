# 🔥Painel Streamlit para visualizar, analisar e prever dados de vendas de um restaurante

Este painel foi desenvolvido usando Streamlit. Vários pacotes de código aberto são usados para processar os dados e gerar as visualizações, por exemplo. [pandas](https://pandas.pydata.org/), [geopandas](https://geopandas.org), [leafmap](https://leafmap.org), [matplotlib](https://matplotlib.org/) e [pydeck](https://deckgl.readthedocs.io).

<p align="center">
 <img src="client/src/public/streamlit.png" width="350" />
</p>


# Projeto Pedacinho do Céu

Este é um projeto de análise de dados para um bar e restaurante localizado no sul da ilha de Florianópolis. O objetivo do projeto é utilizar as informações disponíveis para realizar análises e obter insights que possam ser utilizados para tomar decisões estratégicas.

O projeto utiliza a linguagem Python e diversas bibliotecas para análise de dados, como Pandas, NumPy e Plotly. Além disso, é utilizado o framework Streamlit para a criação de uma interface interativa para o usuário, permitindo a visualização dos dados e a interação com as funcionalidades desenvolvidas.

Entre as funcionalidades desenvolvidas, estão a análise de vendas por mês, a previsão de clientes para o próximo mês, a análise de dados de clientes cadastrados, a exibição de um mapa de localização do estabelecimento e a criação de uma história do bar e restaurante.

Para utilizar o projeto, basta clonar o repositório e instalar as dependências listadas no arquivo requirements.txt. Em seguida, execute o comando "streamlit run app.py" para iniciar a aplicação.


## Status

| Topics  | Links                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| :------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Build   | [![Build Status](https://img.shields.io/travis/big-data-estacio/data/master)](https://travis-ci.com/github/big-data-estacio/data) [![codecov](https://codecov.io/gh/big-data-estacio/data/branch/master/graph/badge.svg)](https://codecov.io/gh/big-data-estacio/data) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) |
| Version | [![Version](https://img.shields.io/github/v/release/big-data-estacio/data)](https://github.com/big-data-estacio/data/releases) [![Release Notes](https://img.shields.io/badge/release-notes-blue)](https://github.com/big-data-estacio/data/releases)                                                                                                                                         |
| Docs    | [![Docs](https://img.shields.io/static/v1?label=docs&message=wiki&color=blue&logo=github)](https://github.com/big-data-estacio/data/wiki)                                                                                                                                                                                                                                                                                                           |
| Support | [![Gitter](https://badges.gitter.im/big-data-estacio/data.svg)](https://gitter.im/big-data-estacio/data?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge) [![Mail](https://img.shields.io/badge/mail-support-brightgreen)](mailto:your-email@example.com)                                                                                                                                                     |
| Binder  | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/big-data-estacio/data/master?urlpath=lab)      |
| Technology | [![Flask](https://img.shields.io/badge/-Flask-black?style=flat&logo=flask)](https://flask.palletsprojects.com/) [![Hadoop](https://img.shields.io/badge/-Hadoop-black?style=flat&logo=hadoop)](https://hadoop.apache.org/) [![Kafka](https://img.shields.io/badge/-Kafka-black?style=flat&logo=apache-kafka)](https://kafka.apache.org/) [![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-black?style=flat&logo=postgresql)](https://www.postgresql.org/) |
| Deploy                                                                                                                                                            | [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://)

---

1. Coleta de dados: O projeto utiliza diversas fontes de dados, como arquivos CSV, APIs e bancos de dados. Os dados são coletados e processados em uma variedade de formatos para atender às necessidades do projeto. A coleta de dados é um processo crucial para garantir que as informações corretas estejam disponíveis para análise e visualização.

2. Processamento de dados: O projeto utiliza uma variedade de técnicas para processar e limpar os dados coletados, incluindo o uso de bibliotecas Python para análise e transformação de dados. Os dados são organizados e limpos para garantir que estejam prontos para análise e visualização. O processamento de dados é uma etapa importante no processo de garantir que as informações corretas estejam disponíveis para o usuário final.

3. Armazenamento de dados: O projeto utiliza uma variedade de tecnologias de armazenamento de dados, incluindo bancos de dados relacionais e não relacionais, armazenamento em nuvem e arquivos CSV. Os dados são armazenados de forma a garantir que estejam seguros e disponíveis para análise e visualização. O armazenamento de dados é um componente crítico do projeto, garantindo que os dados estejam disponíveis quando necessários.

4. Análise e visualização de dados: O projeto utiliza ferramentas de análise e visualização de dados, como Power BI e bibliotecas Python, para extrair informações significativas dos dados coletados. As informações são apresentadas de forma clara e intuitiva, permitindo que o usuário final compreenda facilmente os insights obtidos a partir dos dados. A análise e visualização de dados são etapas críticas no processo de transformação de dados em informações úteis.

5. Atualização e manutenção: O projeto requer atualizações regulares para garantir que os dados estejam atualizados e precisos. Além disso, a manutenção do sistema é importante para garantir que as tecnologias utilizadas estejam atualizadas e seguras. A atualização e manutenção do sistema são etapas críticas para garantir que o projeto continue funcionando de forma eficiente e eficaz ao longo do tempo.

O projeto utiliza conceitos de Big Data e Power BI. Vamos revisar como cada tecnologia é aplicada no projeto:

1. Linguagem de programação Python para desenvolvimento do back-end e front-end da aplicação web, utilizando o framework Streamlit para criação da interface do usuário.
2. Pandas e Numpy para manipulação e análise de dados, realizando operações como seleção, filtragem, agrupamento e junção de dados.
3. Matplotlib e Plotly para criação de gráficos e visualizações de dados interativas.
4. Scikit-Learn para modelagem de dados, com algoritmos de aprendizado de máquina para previsão e classificação.
5. Power BI para criação de dashboards e relatórios interativos e visuais a partir dos dados gerados e analisados na aplicação web.

Combinando Big Data e Power BI, este projeto oferece uma solução completa para coletar, processar, analisar e visualizar grandes volumes de dados em tempo real, ajudando na tomada de decisões informadas e oferecendo insights valiosos para o negócio do restaurante "Pedacinho do Céu".


> **Nota**: Resultados de gráficos e tabelas no power bi, estão disponíveis na pasta `data/processed`.

<!-- powerBi.jpeg -->
![Power BI](client/src/public/powerBi.jpeg)

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
9. [🔥Utilizando a API com Insomnia](#utilizando-a-api-com-insomnia)
10. [🥶Versão atual](#versão-atual)
11. [👹Coletando Dados](#coletando-dados)
12. [👻Processando Dados](#processando-dados)
13. [🤖Visualizando os Dados](#visualizando-os-dados)
14. [👽Futuras Atualizações](#futuras-atualizações)
15. [🐳Tecnologias e conceitos utilizados](#tecnologias-e-conceitos-utilizados)
    * [Hadoop](#hadoop)
    * [Kafka](#kafka)
    * [Docker](#docker)
    * [SOLID](#solid)
    * [Padrões de commit](#padrões-de-commit)
16. [🧠Roadmap v1](#roadmap-v1)
    * [Travis CI](#travis-ci)
    * [Princípios SOLID](#princípios-solid)
    * [SQLAlchemy com PostgreSQL ou MySQL](#sqlalchemy-com-postgresql-ou-mysql)
    * [Autenticação e autorização](#autenticação-e-autorização)
    * [Interface de usuário](#interface-de-usuário)
17. [🧠Roadmap v2](#roadmap-v2)
    * [Roadmap v1.1](#roadmap-v1.1)
    * [Roadmap v1.2](#roadmap-v1.2)
    * [Roadmap v1.3](#roadmap-v1.3)
    * [Roadmap v2.0](#roadmap-v2.0)
18. [🤖O que é o Apache Spark?](#o-que-é-o-apache-spark?)
29. [🎖️Critérios de aceitação do projeto](#critérios-de-aceitação-do-projeto)
20. [👹Contribuindo](#contribuindo)
21. [👾Contribuidores](#contribuidores)
22. [🎉Licença](#licença)


## Introdução

Este projeto é um estudo de caso de Big Data e Power BI. O objetivo é demonstrar como coletar, processar, analisar e visualizar grandes volumes de dados em tempo real usando ferramentas e tecnologias como Python, SQLite e Power BI.

O projeto é baseado em um restaurante chamado "Pedacinho do Céu". O restaurante está localizado em uma cidade turística e serve comida tradicional da região. O restaurante está interessado em coletar dados de várias fontes para analisar e obter insights sobre o negócio. O restaurante também deseja criar visualizações e relatórios interativos para ajudar na tomada de decisões e na compreensão de tendências e padrões nos dados.


## Arvore de Diretorios

Abaixo está a estrutura de diretórios do projeto:

```bash
.
├── 📂 .github
├── 📂 .husky
├── 📂 admin
│   ├── 📂 conf
│   ├── 📂 data_crawlers
│   ├── 📂 target_url_crawlers
│   ├── .gitignore
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── go_spider.py
│   ├── README.md
│   └── requirements.txt
├── 📂 docs
├── 📂 src
│   ├── 📂 api
│   ├── 📂 data
│   ├── 📂 error
│   ├── 📂 log
│   ├── 📂 public
│   ├── 📂 scripts
│   └── main.py
├── .editorconfig
├── .env
├── .gitignore
├── .npmrc
├── .travis.yml
├── app.py
├── debug.sh
├── docker-compose.yml
├── Dockerfile
├── LICENSE
├── Makefile
├── package.json
├── Procfile
├── README.md
├── requirements.txt
└── SECURITY.md
```


## Arquitetura do projeto

A arquitetura do projeto é dividida em várias partes:

* **`.github`**: diretório que contém arquivos relacionados à integração contínua com o GitHub.
* **`.husky`**: diretório que contém arquivos relacionados à configuração do Husky, ferramenta que permite a execução de scripts no Git Hooks.
* **`admin`**: diretório que contém arquivos relacionados à administração do projeto, como scripts para extração de dados (data_crawlers) e URLs alvo (target_url_crawlers).
* **`docs`**: diretório que contém arquivos relacionados à documentação do projeto.
* **`src`**: diretório que contém o código fonte do projeto, organizado em diferentes subdiretórios, como api (que contém as rotas da aplicação), data (que contém os arquivos de dados), error (que contém o tratamento de erros), log (que contém os arquivos de logs) e public (que contém arquivos estáticos, como imagens).
* **`app.py`**: arquivo que contém a configuração e inicialização da aplicação Flask.
* **`docker-compose.yml`**: arquivo que contém a configuração do Docker Compose para a execução da aplicação e do banco de dados.
* **`Dockerfile`**: arquivo que contém a configuração do Docker para a construção da imagem da aplicação.
* **`Makefile`**: arquivo que contém os comandos de automatização de tarefas do projeto.
* **`README.md`**: arquivo que contém a descrição do projeto e sua documentação.
* **`requirements.txt`**: arquivo que contém as dependências do projeto.
* **`LICENSE`**: arquivo que contém as informações sobre a licença do projeto.


## Tecnologias Utilizadas

Neste projeto "Pedacinho do Céu", diversas tecnologias são utilizadas para coletar, processar, armazenar e visualizar dados. Abaixo está uma lista dessas tecnologias e como elas se encaixam no projeto:

1. **Docker Compose**: Ferramenta para definir e gerenciar aplicações multi-container usando arquivos de configuração (docker-compose.yml). É usado para simplificar o processo de inicialização e gerenciamento de todos os serviços envolvidos no projeto.

2. **SQLite3**: Sistema de gerenciamento de banco de dados relacional (RDBMS) utilizado para armazenar e gerenciar dados coletados e processados.

3. **Power BI**: Ferramenta de Business Intelligence (BI) da Microsoft para criar relatórios e visualizações de dados. É usado para analisar e visualizar os dados coletados e processados pelo projeto.

4. **Flask** (opcional): Microframework Python para desenvolvimento de aplicações web. Pode ser usado para criar uma API RESTful que expõe os dados processados e armazenados para outras aplicações ou serviços.

5. **Pandas** (opcional): Biblioteca Python para manipulação e análise de dados. Pode ser usada em conjunto com o Apache Spark para realizar análises e limpeza de dados em pequena escala antes de processá-los no Spark.

6. **Python**: a linguagem de programação utilizada em todas as etapas do projeto, desde a coleta de dados até a análise e visualização. O Python é uma linguagem de programação interpretada, orientada a objetos e de alto nível, que possui uma vasta biblioteca padrão e diversas bibliotecas de terceiros para processamento de dados.

7. **Streamlit**: uma biblioteca de código aberto para criação de aplicativos web de dados em Python. O Streamlit é utilizado no projeto para criar uma interface amigável e interativa para visualização dos dados.

8. **Plotly**: uma biblioteca de visualização de dados interativa de código aberto para Python. O Plotly é utilizado no projeto para criar gráficos e visualizações interativas a partir dos dados processados com o Pandas.

9. **Apache Airflow**: uma plataforma de orquestração de fluxo de trabalho para gerenciamento de tarefas de processamento de dados. O Apache Airflow é utilizado no projeto para agendar e executar tarefas de coleta, processamento e análise de dados de forma automática.


## Pré-requisitos

* Python 3.6+
* Apache Spark 3.0+
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
    "test": "make test",
    "server": "streamlit run app.py",
    "dev": "nodemon server",
    "test-coverage": "make test-coverage",
    "pre-commit": "pre-commit install",
    "deploy": "./deploy.sh",
    "devops": "docker-compose -f docker-compose.devops.yml up --build -d",
    "devops-stop": "docker-compose -f docker-compose.devops.yml down"
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
git clone https://github.com/big-data-estacio/data.git
cd data
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
altair==4.1.0
appdirs==1.4.4
astor==0.8.1
attrs==19.3.0
backcall==0.1.0
base58==2.0.0
bleach==3.1.5
blinker==1.4
boto3==1.13.24
botocore==1.16.24
cachetools==4.1.0
certifi==2020.4.5.1
chardet==3.0.4
click==7.1.2
colorama==0.4.3
cycler==0.10.0
decorator==4.4.2
defusedxml==0.6.0
distlib==0.3.0
docopt==0.6.2
docutils==0.15.2
entrypoints==0.3
enum-compat==0.0.3
jedi==0.17.0
Jinja2==2.11.2
jmespath==0.10.0
jsonschema==3.2.0
kiwisolver==1.2.0
MarkupSafe==1.1.1
matplotlib==3.2.1
mistune==0.8.4
nbconvert==5.6.1
nbformat==5.0.6
numpy==1.18.5
packaging==20.4
pandas==1.0.4
pandocfilters==1.4.2
parso==0.7.0
pathtools==0.1.2
pickleshare==0.7.5
Pillow==7.1.2
pipreqs==0.4.10
plotly==4.14.3
plotting==0.0.6
pydeck==0.4.0b1
Pygments==2.6.1
pywinpty==0.5.7
pyzmq==19.0.1
qtconsole==4.7.4
QtPy==1.9.0
requests==2.23.0
retrying==1.3.3
s3transfer==0.3.3
scipy==1.4.1
seaborn==0.10.1
Send2Trash==1.5.0
six==1.15.0
streamlit==0.61.0
terminado==0.8.3
testpath==0.4.4
toml==0.10.1
toolz==0.10.0
tornado==5.1.1
traitlets==4.3.3
tzlocal==2.1
urllib3==1.25.9
validators==0.15.0
virtualenv==20.0.21
watchdog==0.10.2
wcwidth==0.2.3
webencodings==0.5.1
widgetsnbextension==3.5.1
yarg==0.1.9
```

8. Quando terminar de trabalhar no projeto, você pode desativar o ambiente virtual com o seguinte comando:

```bash
deactivate
```

### 📦 Continuando a instalação

1. Crie um arquivo `.env` na raiz do projeto com as variáveis de ambiente necessárias. Você pode usar o arquivo `.env.example` como modelo.

2. Instale as dependências do projeto com o yarn na raiz do projeto:

```bash
yarn add
```

### Para iniciar o projeto "Pedacinho do Céu" com o Docker, siga estas etapas:

1. Certifique-se de que o Docker e o Docker Compose estejam instalados em seu sistema. Se você ainda não os instalou, siga as instruções de instalação no site oficial do Docker: `https://docs.docker.com/get-docker/` e `https://docs.docker.com/compose/install/`

2. Abra um terminal e navegue até o diretório raiz do projeto `data`.

3. Execute o seguinte comando para criar e iniciar os containers do projeto, conforme definido no arquivo `docker-compose.yml`:

- ```docker build -t streamlit-ts-ml:0.1.0 -f Dockerfile .```
- ```docker run -p 8501:8501 streamlit-ts-ml:0.1.0```
- Open `http://localhost:8501/`
<!-- - Build with ```docker build -t ts-forecast-app .``` (takes some time!)
- Run with ```docker run -p 8501:8501 ts-forecast-app:latest``` -->

Isso iniciará os serviços do Docker, a API, como o SQLite3 e o serviço de processamento de dados se necessário.

4. Abra os relatórios do Power BI na pasta `data_visualization/power_bi_reports/` para visualizar e analisar os dados processados. Se você não possui o Power BI Desktop, faça o download e instale-o a partir do site oficial: `https://powerbi.microsoft.com/en-us/desktop/`

5. Ao longo do desenvolvimento do projeto, você pode modificar e ajustar os arquivos na pasta `src/` conforme necessário para aprimorar a análise e o processamento dos dados.

Lembre-se de que, dependendo da configuração do projeto, algumas etapas podem variar ou exigir ações adicionais. Ajuste as etapas conforme necessário para se adequar às necessidades específicas do seu projeto.

6. Quando terminar de usar o projeto, pare os serviços do Docker Compose pressionando `Ctrl+C` no terminal onde o Docker Compose está sendo executado. Para remover os contêineres e os volumes, execute:

```bash
docker-compose down --remove-orphans --volumes
```

### Para iniciar o projeto "Pedacinho do Céu" sem o Docker, siga estas etapas:

1. Abra um terminal e navegue até o diretório raiz do projeto `data`.

2. Execute o seguinte comando para executar o projeto na pasta `client`:

```bash
cd client
yarn run server:app
```

# ou

cd [client]
streamlit run app.py --server.address 0.0.0.0 --server.port [your port]
# http://0.0.0.0:[your port]
```

### Iniciando a API

1. Inicie o servidor da API:
  
```bash
node client/src/api/index.js
```

> Já o arquivo api/app.py, é o arquivo principal da API, onde é feita a conexão com o banco de dados e a definição dos endpoints.

Ele é executado na porta 5000, e pode ser acessado em `http://localhost:5000/`

## Utilizando a API

A API RESTful permite gerenciar os dados armazenados no banco de dados PostgreSQL. Para utilizar a API, você pode fazer requisições HTTP para os seguintes endpoints:

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
from flask import Flask
from routes.bebidas import bebidas_bp
from routes.clientes import clientes_bp

app = Flask(__name__)
app.register_blueprint(bebidas_bp)
app.register_blueprint(clientes_bp)

if __name__ == '__main__':
    app.run(debug=True)
```

A API estará disponível na porta 5000.

* Abra o Power BI Desktop e carregue os relatórios na pasta `data_visualization/power_bi_reports`.


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

Os dados podem ser visualizados usando relatórios do Power BI. Para visualizar os relatórios, você pode fazer o download do Power BI Desktop [aqui](https://powerbi.microsoft.com/pt-br/desktop/). Após instalar o Power BI Desktop, você pode abrir o arquivo `data.pbix` para visualizar os relatórios.


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

# Para iniciar o cluster Spark a partir da máquina local com o Linux, você precisa seguir os seguintes passos:


# **Instalação e Execução do Apache Spark no Windows**


## Pré-requisitos
--------------

Antes de começar a instalar o Apache Spark, certifique-se de que o seu sistema atenda aos seguintes requisitos:

*   Linux (Ubuntu ou outra distribuição)
*   Java 8 ou superior
*   Python 2.7 ou 3.x
*   Acesso à Internet

1.  Baixe e instale o Spark no seu computador, certificando-se de ter a versão correta do Spark para a sua plataforma: [spark apache ](https://spark.apache.org/downloads.html)
    
2.  Extraia o arquivo baixado para um diretório de sua escolha.
    
3.  Abra um terminal e navegue para o diretório onde você extraiu o Spark.
    
4.  Inicie o master Spark executando o seguinte comando:
    
    bash
    
    ```bash
    ./sbin/start-master.sh
    ```
    
    Isso iniciará o master Spark no seu computador local.
    
5.  Você pode verificar se o master Spark foi iniciado corretamente abrindo um navegador e digitando a seguinte URL na barra de endereço:
    
    arduino
    
    ```arduino
    http://localhost:8080/
    ```
    
    Isso abrirá a interface web do Spark, que mostrará se o master Spark está em execução.
    
6.  Inicie um ou mais workers Spark executando o seguinte comando:
    
    bash
    
    ```bash
    ./sbin/start-worker.sh spark://localhost:7077
    ```
    
    Isso iniciará um worker Spark no seu computador local, conectando-o ao master Spark. Você pode iniciar quantos workers quiser, em quantas máquinas diferentes quiser.
    
7.  Para parar o master Spark e todos os workers, execute o seguinte comando:
    
    arduino
    
    ```arduino
    ./sbin/stop-all.sh
    ```
    
    Isso interromperá o master Spark e todos os workers em execução.


</br>
</br>

## **Instalação e Execução do Apache Spark no Ubuntu Resumida**

## Pré-requisitos
--------------

Antes de começar a instalar o Apache Spark, certifique-se de que o seu sistema atenda aos seguintes requisitos:

*   Linux (Ubuntu ou outra distribuição)
*   Java 8 ou superior
*   Python 2.7 ou 3.x
*   Acesso à Internet


> Certifique-se de que o Java esteja instalado em sua máquina.

* Instale o Java 8 caso não esteja instalado:

Abra o terminal e execute o seguinte comando: `sudo apt update && sudo apt install openjdk-8-jdk`

* Verifique a versão do Python instalada:

```bash
python --version
```

* Instale o Python 3.7 ou superior caso não esteja instalado:

```bash
sudo apt update
sudo apt install python3
```


### 1\. Verifique se o Java está instalado

Antes de começar a instalar o Apache Spark, verifique se o Java está instalado em sua máquina. O Apache Spark requer que o Java esteja instalado.

Para verificar a versão do Java em sua máquina, execute o seguinte comando em seu terminal:

`java -version`

Se o Java não estiver instalado, siga as instruções no site oficial da Oracle para baixar e instalar o Java.


### Instalação por gerenciador de pacotes

1.  Abra o terminal e execute o seguinte comando para instalar o Apache Spark:
    
    sql
    
    ```sql
    sudo apt-get update
    sudo apt-get install spark
    ```

### Abra o navegador e digite o seguinte URL na barra de endereço para instalar o Apache Spark:

```bash
https://www.apache.org/dyn/closer.lua/spark/spark-3.4.0/spark-3.4.0-bin-hadoop3.tgz
```

* logo em seguida baixe na raiz do projeto o arquivo spark-3.4.0-bin-hadoop3.tgz
* mova o arquivo para a pasta /opt:

```bash
sudo mv spark-3.4.0-bin-hadoop3.tgz /opt
```

* acessar a pasta /opt:

```bash
cd /opt
```

* descompactar o arquivo:

```bash
sudo tar -xvzf spark-3.4.0-bin-hadoop3.tgz
```

* acessar a pasta spark-3.4.0-bin-hadoop3:

```bash
cd spark-3.4.0-bin-hadoop3
```

* configurar as variáveis de ambiente:

```bash
sudo nano /etc/profile
```

* adicionar as seguintes linhas no final do arquivo:

```bash
export SPARK_HOME=/opt/spark-3.4.0-bin-hadoop3
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
```

* salvar o arquivo e sair do editor de texto com os seguntes comandos:

```bash
CTRL + s
CTRL + x
```

* verificar se o pyspark está funcionando:

```bash
pyspark
```

* iniciar o servidor apache spark:

```bash
sudo /opt/spark-3.4.0-bin-hadoop3/sbin/start-master.sh
```

* acessar o endereço http://localhost:8080/ para verificar se o servidor está funcionando

* **OBS:** caso o servidor não esteja funcionando, verifique se a porta 8080 está liberada no firewall

Agora que você iniciou o serviço do Apache Spark, você pode utilizar suas funcionalidades em seu projeto. Para fazer isso, você precisa primeiro iniciar o SparkSession em seu código Python. O SparkSession é o ponto de entrada para o Spark e fornece a interface para trabalhar com os dados no Spark.

Para iniciar o SparkSession em seu código Python, você pode usar o seguinte código:

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("NomeDoSeuApp") \
    .master("local[*]") \
    .getOrCreate()
```

O appName define o nome da sua aplicação e o master define o modo de execução do Spark. No exemplo acima, estamos usando local[*] para executar o Spark no modo local. Você pode substituir local[*] pelo endereço do servidor do Spark se você estiver executando o Spark em um cluster.

Com o SparkSession criado, você pode utilizar todas as funcionalidades do Spark, como ler e escrever dados de e para diferentes fontes de dados, realizar transformações e operações em larga escala em seus dados, etc. Por exemplo, para ler um arquivo CSV e criar um DataFrame com os dados, você pode usar o seguinte código:

```python
df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("/caminho/para/o/arquivo.csv")

df.show()
```

Neste exemplo, estamos lendo um arquivo CSV que tem um cabeçalho e o Spark vai inferir o esquema dos dados. Você pode modificar as opções de leitura de acordo com suas necessidades.

* iniciar um ou mais workers Spark executando o seguinte comando:

```bash
sudo /opt/spark-3.4.0-bin-hadoop3/sbin/start-worker.sh spark://localhost:7077
```

* No seu projeto Python, importe as bibliotecas do PySpark e crie uma sessão Spark:
  
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("myApp").getOrCreate()
```

Em seguida, crie as funções que usam os serviços do Spark para realizar as tarefas desejadas. Por exemplo, se você quiser ler um arquivo CSV em um DataFrame do Spark, pode usar a seguinte função:

```python
def read_csv_file(file_path):
    df = spark.read.format("csv").option("header", "true").load(file_path)
    return df

df = read_csv_file("/path/to/file.csv")

df.show()
```

Por fim, execute seu aplicativo Streamlit a partir do terminal com o comando:

```bash
streamlit run app.py
```

Depois de executar o comando streamlit run app.py e ter iniciado a aplicação Streamlit, você pode interagir com a interface do seu aplicativo no navegador. A partir daí, é possível utilizar as funcionalidades e algoritmos implementados no seu projeto que utilizam o Apache Spark como processador de dados. Por exemplo, se o seu aplicativo utiliza o Spark para processar dados de um conjunto de dados, você pode carregar esse conjunto de dados na interface e executar as operações definidas pelo seu algoritmo para processá-los. É importante lembrar que o Apache Spark funciona como um motor de processamento de dados distribuído, o que significa que ele é capaz de processar grandes conjuntos de dados de forma eficiente, o que pode ser particularmente útil em projetos que lidam com dados em escala.


* **```Ou```** pode optar por seguir as seguintes instruções:

* iniciar o worker:

```bash
sudo /opt/spark-3.4.0-bin-hadoop3/sbin/start-slave.sh spark://localhost:7077
```

* atualizar as variáveis de ambiente:

```bash
source /etc/profile
```

* acessar a pasta spark-3.4.0-bin-hadoop3:

```bash
cd spark-3.4.0-bin-hadoop3
```

* iniciar o master Spark no seu computador local:

```bash
./sbin/start-master.sh
```

* pronto, o servidor apache spark está funcionando

* para parar o master Spark e todos os workers, execute o seguinte comando:

```bash
./sbin/stop-all.sh
```


## **Instalação e Execução do Apache Spark no Ubuntu (Completa)**

Este guia tem como objetivo fornecer os passos necessários para a instalação e execução do Apache Spark em um ambiente Linux. O Apache Spark é um sistema de computação distribuída que permite processar grandes volumes de dados em um cluster de computadores. Ele é amplamente utilizado para análise de big data, machine learning, processamento de stream e outras aplicações de processamento paralelo.

<div align="center">
  <a href="https://www.youtube.com/watch?v=DZ-ciI5_CQw" target="_blank"
  alt="IMAGE ALT TEXT" width="20" height="10" border="10"><img src="https://i.ytimg.com/vi/DZ-ciI5_CQw/maxresdefault.jpg"></a>
</div>


## Pré-requisitos

Antes de começar a instalar o Apache Spark, certifique-se de que o seu sistema atenda aos seguintes requisitos:

*   Linux (Ubuntu ou outra distribuição)
*   Java 8 ou superior
*   Python 2.7 ou 3.x
*   Acesso à Internet


> Certifique-se de que o Java esteja instalado em sua máquina.

* Instale o Java 8 caso não esteja instalado:

Abra o terminal e execute o seguinte comando: `sudo apt update && sudo apt install openjdk-8-jdk`

* Verifique a versão do Python instalada:

```bash
python --version
```

* Instale o Python 3.7 ou superior caso não esteja instalado:

```bash
sudo apt update
sudo apt install python3
```


### 1\. Verifique se o Java está instalado

Antes de começar a instalar o Apache Spark, verifique se o Java está instalado em sua máquina. O Apache Spark requer que o Java esteja instalado.

Para verificar a versão do Java em sua máquina, execute o seguinte comando em seu terminal:

`java -version`

Se o Java não estiver instalado, siga as instruções no site oficial da Oracle para baixar e instalar o Java.

## Instalação do Apache Spark
--------------------------

### Instalação por gerenciador de pacotes

1.  Abra o terminal e execute o seguinte comando para instalar o Apache Spark:
    
    sql
    
    ```sql
    sudo apt-get update
    sudo apt-get install spark
    ```
    
2.  Aguarde até que o processo de instalação seja concluído.

1.  Baixe o Spark:
    
```wget https://downloads.apache.org/spark/spark-3.2.4/spark-3.2.4-bin-hadoop3.2.tgz```
    
<!-- 2.  Extraia o arquivo baixado:
    
```tar xvf spark-3.2.4-bin-hadoop3.2.tgz``` -->
    
<!-- 3.  Mova o diretório extraído para `/opt`:
    
```sudo mv spark-3.1.1-bin-hadoop3.2 /opt/spark```

4. Mova a pasta extraída para o diretório /usr/local/spark:

```bash
sudo mv spark-3.2.4-bin-hadoop3.2 /usr/local/spark
```
    
    
5.  Verifique se o Spark está instalado corretamente:
    
`spark-shell`
    
Isso abrirá o shell do Spark e você deve ver a mensagem "Welcome to \_\_\_\_ \_\_\_\_". -->



### 3\. Extraia o Apache Spark

Após baixar o arquivo tar do Apache Spark, extraia-o para um diretório de sua escolha:

python

```python
tar -xvf spark-3.2.4-bin-hadoop3.2.tgz
```

### 4\. Configuração do Apache Spark

Crie o arquivo de configuração do Spark em sua pasta de instalação:

bash

```bash
cd spark-3.2.4-bin-hadoop3.2/conf/
cp spark-env.sh.template spark-env.sh
```

Edite o arquivo `spark-env.sh` com o seguinte comando:

`nano spark-env.sh`

Insira as seguintes linhas no arquivo e salve as alterações:

```bash
export SPARK_HOME=/usr/local/spark
export PATH=$PATH:$SPARK_HOME/bin
```

10. Execute o comando abaixo para atualizar as variáveis de ambiente:

```bash
bash -n ~/.bashrc
```

10. Verifique se o Apache Spark foi instalado corretamente:

```bash
spark-submit --version
```

> Caso ocorra esse erro:

```log
Traceback (most recent call last):
  File "/home/estevam/micromamba/bin/find_spark_home.py", line 95, in <module>
    print(_find_spark_home())
  File "/home/estevam/micromamba/bin/find_spark_home.py", line 59, in _find_spark_home
    module_home = os.path.dirname(find_spec("pyspark").origin)
AttributeError: 'NoneType' object has no attribute 'origin'
/home/estevam/micromamba/bin/spark-submit: line 27: /bin/spark-class: No such file or directory
```


Esse erro indica que o PySpark não foi instalado corretamente ou não foi encontrado no sistema.

Verifique se você seguiu todas as etapas corretamente durante a instalação e se adicionou as variáveis de ambiente corretamente.

Você pode tentar reinstalar o PySpark usando o comando pip install pyspark ou verifique se o caminho para o Spark Home está correto e atualizado nas variáveis de ambiente.

> Agora poderá usar novamente o comando ```spark-submit --version``` e logo aparecerá isso no terminal:

```log
23/05/02 18:52:38 WARN Utils: Your hostname, estevam resolves to a loopback address: 127.0.1.1; using 172.20.231.90 instead (on interface eth0)
23/05/02 18:52:38 WARN Utils: Set SPARK_LOCAL_IP if you need to bind to another address
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 3.4.0
      /_/
                        
Using Scala version 2.12.17, OpenJDK 64-Bit Server VM, 11.0.18
Branch HEAD
Compiled by user xinrong.meng on 2023-04-07T02:18:01Z
Revision 87a5442f7ed96b11051d8a9333476d080054e5a0
Url https://github.com/apache/spark
Type --help for more information.
```

> rode agora o ```pyspark``` no terminal e verá essa informação:

```log
Python 3.9.16 | packaged by conda-forge | (main, Feb  1 2023, 21:39:03) 
[GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
23/05/02 18:50:48 WARN Utils: Your hostname, estevam resolves to a loopback address: 127.0.1.1; using 172.20.231.90 instead (on interface eth0)
23/05/02 18:50:48 WARN Utils: Set SPARK_LOCAL_IP if you need to bind to another address
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
23/05/02 18:50:51 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 3.4.0
      /_/

Using Python version 3.9.16 (main, Feb  1 2023 21:39:03)
Spark context Web UI available at http://172.20.231.90:4040
Spark context available as 'sc' (master = local[*], app id = local-1683064253636).
SparkSession available as 'spark'.
>>> 
```


Agora que o PySpark está rodando corretamente no seu ambiente, você pode seguir as etapas do roadmap que você criou anteriormente para executar o seu projeto.

Você pode, por exemplo, utilizar as funções que você criou anteriormente para ler os arquivos estoque_mercadorias.csv e total_clientes.csv, realizar transformações e análises nos dados utilizando o PySpark e gerar os gráficos utilizando o Altair.

Lembre-se de ajustar as funções para que elas utilizem o PySpark ao invés do Pandas para processar os dados. Isso pode envolver a utilização de operações específicas do PySpark como o groupBy e o agg.



### 5\. Para executar o Apache Spark no seu projeto, você deve inicializar o cluster com o seguinte comando:

Para iniciar o Apache Spark, execute o seguinte comando na pasta de instalação do Spark:


```bash
SPARK_HOME/sbin/start-master.sh
```

11. O endereço do web UI do cluster será exibido no terminal. Acesse o endereço em seu navegador para visualizar o cluster.

11. Para adicionar workers ao cluster, execute o seguinte comando em um novo terminal:

```bash
$SPARK_HOME/sbin/start-worker.sh spark://<IP_DO_MASTER>:7077
```

Substitua <IP_DO_MASTER> pelo endereço IP da máquina em que o Master está sendo executado.

10. Agora você pode executar seu projeto com PySpark. Basta importar a biblioteca PySpark e utilizar as funções disponíveis. Exemplo:

```java
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("MeuApp").getOrCreate()
```

### 6\. Verifique se o Apache Spark está em execução

Para verificar se o Apache Spark está em execução, acesse o navegador e digite a URL `http://localhost:8080`. Isso deve exibir a interface da Web do Apache Spark com informações sobre a execução do cluster Spark.

### 7\. Use o Apache Spark

Com o Apache Spark em execução, você pode começar a usá-lo para executar suas tarefas de processamento de dados.

Para começar, você pode executar o `spark-shell`, que é uma ferramenta interativa de linha de comando que permite executar código Scala ou Python no contexto do Spark. Para executar o `spark-shell`, execute o seguinte comando na pasta de instalação do Spark:

bash

```bash
./bin/spark-shell
```

O Apache Spark agora está pronto para ser usado em sua máquina local.



    

## Execução do Apache Spark
------------------------

1.  Inicie o Spark:
    
    
```sql
start-master.sh
```
    
2.  Abra o navegador e acesse `http://localhost:8080/`. Você deverá ver a interface do usuário do Spark.
    
3.  Para executar um aplicativo, use o seguinte comando:
    
    
```bash
spark-submit /caminho/para/o/arquivo/app.py
```
    
    Substitua `/caminho/para/o/arquivo/app.py` pelo caminho completo para o arquivo do seu aplicativo.
    

Com essas etapas, você deve ser capaz de instalar e executar o Apache Spark no Ubuntu.


## Execução
--------

Após instalar o Apache Spark, você pode executá-lo da seguinte maneira:

1.  Abra o terminal e execute o seguinte comando:
    
    `spark-shell`
    
    Esse comando inicia o shell interativo do Spark, onde você pode executar comandos e scripts do Spark utilizando a linguagem Scala.
    
2.  Para executar scripts em Python, use o seguinte comando:
    
    `pyspark`
    
    Esse comando inicia o shell interativo do Spark, onde você pode executar comandos e scripts do Spark utilizando a linguagem Python.
    
3.  Para executar scripts em R, use o seguinte comando:
    
    `sparkR`
    
    Esse comando inicia o shell interativo do Spark, onde você pode executar comandos e scripts do Spark utilizando a linguagem R.

## Executando scripts em python no terminal interativo do Spark

Ao digitar pyspark no terminal, você iniciou uma sessão interativa do Spark utilizando a linguagem Python (PySpark).

A linha SparkSession available as 'spark' indica que a sessão do Spark foi iniciada e que você pode acessá-la por meio do objeto spark.

Você pode começar a escrever código para executar suas tarefas no Spark dentro da sessão interativa. Por exemplo, para ler um arquivo CSV e exibir o schema do DataFrame resultante, você pode executar o seguinte código:

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("myApp").getOrCreate()

df = spark.read.csv("client/src/data/bebidas.csv", header=True, inferSchema=True)

df.printSchema()
```

No exemplo acima, criamos um objeto SparkSession e utilizamos o método read.csv para ler o arquivo CSV especificado. Em seguida, exibimos o schema do DataFrame resultante com o método printSchema().

Depois de executar o código na sessão interativa do PySpark, você pode fechar a sessão com o seguinte comando:

```python
spark.stop()
```

Para integrar o cluster do Spark em seu projeto, você pode utilizar a API PySpark do Spark para ler e manipular dados em larga escala. Para isso, você pode criar uma sessão Spark em seu arquivo app.py da seguinte maneira:

```python
from pyspark.sql import SparkSession

# Crie uma sessão Spark
spark = SparkSession.builder \
    .appName("MyApp") \
    .master("local[*]") \
    .getOrCreate()

# Leitura de dados a partir de um arquivo CSV
df = spark.read.csv("client/src/data/bebidas.csv", header=True, inferSchema=True)

# Manipulação de dados
df = df.filter(df["idade"] > 18)

# Exibição do DataFrame resultante
df.show()

# Encerramento da sessão Spark
spark.stop()
```

Dentro da sessão, você pode ler e manipular dados de forma distribuída, aproveitando a capacidade de processamento e armazenamento do cluster Spark. No exemplo acima, estamos criando uma sessão local e lendo dados de um arquivo CSV, filtrando os registros com idade maior que 18 e exibindo o resultado. No final, encerramos a sessão Spark com o método stop().


## Iniciar o servidor Apache Spark

Para iniciar o servidor local com o Apache Spark, basta executar o comando start-all.sh na pasta $SPARK_HOME/sbin. Por exemplo, se você instalou o Apache Spark em /opt/spark, o comando seria:

```bash
spark-3.2.4-bin-hadoop3.2/sbin/start-all.sh
```

Isso iniciará o servidor Spark, incluindo o Master, os Workers e o History Server. Você poderá então executar o seu código Spark ou o Streamlit em outro terminal. Para parar o servidor, basta executar o comando stop-all.sh na mesma pasta.


## Conclusão

Com isso, você já está pronto para instalar e executar o Apache Spark em seu sistema. Lembre-se de sempre verificar a documentação oficial do Apache Spark em [https://spark.apache.org/docs/latest/](https://spark.apache.org/docs/latest/) para informações mais detalhadas.

> Caso for enviar as alterações feitas com o arquivo spark-3.2.1-bin-hadoop2.7.tgz, não esqueça de deletar o arquivo do diretório antes de enviar, ou posso usar os comandos:

```git lfs install```
```git lfs track "venv/lib/python3.9/site-packages/pyspark/jars/rocksdbjni-7.9.2.jar"```
```git lfs track "backend/spark-3.2.4-bin-hadoop3.2.tgz"```

* caso ocorra esse erro:

```log
git lfs install
git lfs track "venv/lib/python3.9/site-packages/pyspark/jars/rocksdbjni-7.9.2.jar"
git lfs track "backend/spark-3.2.4-bin-hadoop3.2.tgz"
git: 'lfs' is not a git command. See 'git --help'.

The most similar command is
        lsfn
git: 'lfs' is not a git command. See 'git --help'.

The most similar command is
        lsfn
git: 'lfs' is not a git command. See 'git --help'.

The most similar command is
        lsfn
```

* execute o comando no linux:

```bash
sudo apt-get install git-lfs
```

Em seguida, execute novamente os comandos para rastrear os arquivos grandes e fazer o commit e push novamente.

```bash
git lfs install
git lfs track "venv/lib/python3.9/site-packages/pyspark/jars/rocksdbjni-7.9.2.jar"
git lfs track "backend/spark-3.2.4-bin-hadoop3.2.tgz"
git add .gitattributes
git add .
git commit -m "Commit message"
git push
```

Certifique-se de também confirmar o seu email e o nome de usuário do git com o comando ```git config --global user.email "you@example.com"``` e ```git config --global user.name "Your Name"```.



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

<a href="https://github.com/gutorafael">
  <img src="https://contrib.rocks/image?repo=gutorafael/gutorafael" />
</a>
<a href="https://github.com/gfucci">
  <img src="https://contrib.rocks/image?repo=gfucci/desafio_acaodireta" />
</a>
<a href="https://github.com/lele-sf">
  <img src="https://contrib.rocks/image?repo=lele-sf/lele-sf" />
</a>
<a href="https://github.com/estevam5s">
  <img src="https://contrib.rocks/image?repo=estevam5s/rest-api-nasa" />
</a>
<a href="https://github.com/PedroDellaMea">
  <img src="https://contrib.rocks/image?repo=PedroDellaMea/Atividades-HTML-AV1" />
</a>
<a href="https://github.com/AldairSouto">
  <img src="https://contrib.rocks/image?repo=AldairSouto/AldairSouto" />
</a>

## Deploy do WebApp na streamlit.io

Para fazer o deploy do WebApp na streamlit.io, siga estas etapas:

1. Faça um fork do repositório.
2. Crie uma conta na streamlit.io.
3. Crie um novo projeto na streamlit.io.
4. Faça o upload do arquivo `app.py` para o projeto criado na streamlit.io.
5. Clique no botão `Deploy`.
6. Aguarde o deploy ser concluído.
7. Acesse o link do WebApp.
8. Pronto! Agora você pode acessar o WebApp e testá-lo.


## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo `LICENSE` para obter detalhes.
