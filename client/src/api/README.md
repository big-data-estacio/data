# API para cadastro e consulta de bebidas.

> Este é um projeto simples para fins educacionais que implementa um CRUD (Create, Read, Update, Delete) de bebidas utilizando Node.js, Express e Prisma ORM.

## Requisitos
----------

*   Node.js 14.x ou superior;
*   yarn ou npm;
*   PostgreSQL 12 ou superior.


## Tecnologias
-----------

*   Node.js
*   Express
*   Prisma
*   PostgreSQL


## Estrutura do projeto
--------------------

*   `client`: pasta com o código da API.
    *   `src`: pasta com o código da aplicação.
        *   `api`: pasta com as rotas da API.
        *   `controller`: pasta com os controllers da API.
        *   `data`: pasta com os arquivos CSV das bebidas.
        *   `db`: pasta com a configuração do banco de dados.
        *   `exportToCsv.js`: script para exportar os dados das bebidas para um arquivo CSV.
        *   `index.js`: arquivo principal da aplicação.
    *   `prisma`: pasta com as configurações do Prisma ORM.


## Instalação
----------

Para rodar a aplicação, é necessário ter o Node.js e o Yarn instalados. Em seguida, execute o seguinte comando na raiz do projeto para instalar as dependências:

`yarn install`

4.  Crie o banco de dados:
    
`yarn prisma migrate dev`


## Banco de dados
--------------

O banco de dados utilizado neste projeto é o SQLite. Para criar o banco e as tabelas, execute o seguinte comando:

`npx prisma migrate dev`


### Banco de dados

Este projeto utiliza o [Prisma ORM](https://www.prisma.io/) para acessar o banco de dados. Siga os passos abaixo para criar o banco de dados e as tabelas necessárias:

1.  Certifique-se de que o MySQL está instalado em sua máquina.
2.  Crie um banco de dados vazio com o nome "crud-bebidas".
3.  Configure as variáveis de ambiente do banco de dados no arquivo `.env`, conforme o exemplo em `.env.example`.
4.  Execute as migrações com o comando `npx prisma migrate dev`.
5.  Popule o banco de dados com o arquivo CSV fornecido em `client/src/data/bebidas.csv` usando o endpoint `POST /api/bebidas/populate`. Este endpoint irá inserir os dados do arquivo CSV no banco de dados.


## Execução
--------

1. Para executar a aplicação, execute o seguinte comando:

`yarn run dev`

A aplicação irá rodar na porta 3000 por padrão.

> Agora abre outra instância do terminal e execute o seguinte comando para iniciar o servidor:

Para importar as bebidas do arquivo bebidas.csv para o banco de dados, envie uma solicitação POST para a rota /api/bebidas/import. Isso pode ser feito usando uma ferramenta como o curl:

```bash
curl -X POST http://localhost:3000/api/bebidas/import
```

Isso importará as bebidas do arquivo bebidas.csv e as armazenará no banco de dados.

2. Acesse as rotas da API:
    
Você pode acessar as rotas da API através do [Insomnia](https://insomnia.rest/). O arquivo `insomnia.json` contém as rotas configuradas para a API.
As rotas podem ser testadas usando uma ferramenta de teste de API, como o [Insomnia](https://insomnia.rest/). Para importar as rotas no Insomnia, use o botão "Import" na barra lateral e selecione o arquivo `client/insomnia/bebidas.json`.

## API
---

Para acessar as bebidas armazenadas no banco de dados, você pode usar as seguintes rotas:

* **`GET /api/bebidas`**: Retorna todas as bebidas armazenadas no banco de dados.
* **`GET /api/bebidas/:id`**: Retorna uma bebida específica com o ID especificado.
* **`POST /api/bebidas`**: Cria uma nova bebida no banco de dados com os dados fornecidos no corpo da solicitação.
* **`PUT /api/bebidas/:id`**: Atualiza uma bebida existente com o ID especificado usando os dados fornecidos no corpo da solicitação.
* **`DELETE /api/bebidas/:id`**: Exclui uma bebida existente com o ID especificado.

Você pode testar essas rotas usando o curl, o Postman ou qualquer outra ferramenta que permita fazer solicitações HTTP.

A aplicação disponibiliza a seguinte API:

### `GET /api/bebidas`

Retorna todas as bebidas cadastradas.

#### Parâmetros

```
| Nome | Tipo | Descrição |
| --- | --- | --- |
| `nome` | string | **Obrigatório.** Nome da bebida. |
| `preco` | number | **Obrigatório.** Preço da bebida. |
| `quantidade` | number | **Obrigatório.** Quantidade de bebidas disponíveis. |
| `descricao` | string | Descrição da bebida. |
| `total_vendas` | number | Total de vendas da bebida. |
| `quantidade_vendas` | number | Quantidade de vendas da bebida. |
```

```json
[
  {
    "id": 1,
    "nome": "Coca Cola",
    "preco": 5.00,
    "quantidade": 10,
    "descricao": "Refrigerante de cola",
    "total_vendas": 100.00,
    "quantidade_vendas": 20
  },
  {
    "id": 2,
    "nome": "Fanta Laranja",
    "preco": 4.50,
    "quantidade": 5,
    "descricao": "Refrigerante de laranja",
    "total_vendas": 50.00,
    "quantidade_vendas": 10
  }
]
```

### `GET /api/bebidas/:id`

Retorna a bebida com o ID especificado.

#### Parâmetros

```
| Nome | Tipo | Descrição |
| --- | --- | --- |
| `id` | number | **Obrigatório.** ID da bebida. |
```

### `POST /api/bebidas`

Cria uma nova bebida com os dados passados no corpo da requisição.

Exemplo de corpo da requisição:

json

```json
{
  "nome": "Coca Cola",
  "preco": 5.0,
  "quantidade": 10,
  "descricao": "Refrigerante de cola",
  "total_vendas": 100.0,
  "quantidade_vendas": 20
}
```

### Parâmetros

```
| Nome | Tipo | Descrição |
| --- | --- | --- |
| `nome` | string | **Obrigatório.** Nome da bebida. |
| `preco` | number | **Obrigatório.** Preço da bebida. |
| `quantidade` | number | **Obrigatório.** Quantidade de bebidas disponíveis. |
| `descricao` | string | Descrição da bebida. |
| `total_vendas` | number | Total de vendas da bebida. |
| `quantidade_vendas` | number | Quantidade de vendas da bebida. |
```

### `PUT /api/bebidas/:id`

Atualiza os dados da bebida com o ID especificado com os dados passados no corpo da requisição.

Exemplo de corpo da requisição:

json

```json
{
  "nome": "Coca Cola",
  "preco": 5.0,
  "quantidade": 10,
  "descricao": "Refrigerante de cola",
  "total_vendas": 200.0,
  "quantidade_vendas": 30
}
```

### `DELETE /api/bebidas/:id`

Remove a bebida com o ID especificado.


## Rotas no Insomnia
-----------------

O arquivo `insomnia.json` contém uma coleção com as rotas da API prontas para serem importadas no Insomnia. Para importá-las, siga os seguintes passos:

1.  Abra o Insomnia;
2.  Clique em "Import/Export";
3.  Clique em "Import Data";
4.  Selecione o arquivo `insomnia.json`.


## Importação e Exportação para CSV
-------------------

Para exportar os dados das bebidas cadastradas para um arquivo CSV, execute o seguinte comando:

`node exportToCsv.js`