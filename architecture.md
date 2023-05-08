# Arquitetura do Projeto e Estrutura de Pastas

Este documento descreve a arquitetura geral e a estrutura de pastas do projeto "Restaurante Pedacinho do Céu".

## Arquitetura do Projeto

O projeto utiliza a linguagem Python com o framework Flask para criar uma API RESTful. A arquitetura do projeto é baseada nos seguintes componentes principais:

- API RESTful (pasta `api`)
- Processamento e análise de dados (pasta `src`)
- Armazenamento e gerenciamento de dados (pasta `data`)
- Visualização de dados com Power BI (pasta `notebooks`)

### API RESTful

A API RESTful é implementada usando o framework Flask e segue os princípios de arquitetura SOLID. A pasta `api` contém os seguintes subdiretórios:

- `controller`: Responsável por gerenciar as requisições HTTP e as respostas da API.
- `routes`: Define as rotas da API e mapeia as requisições HTTP para os métodos dos controllers.
- `service`: Contém a lógica de negócios e a interação com o banco de dados.
- `tests`: Contém os testes unitários e de integração para a API.

### Processamento e Análise de Dados

O processamento e a análise de dados são realizados usando a biblioteca Pandas. A pasta `src` contém os seguintes subdiretórios:

- `analysis`: Contém os scripts de análise de dados.
- `config`: Contém os arquivos de configuração do projeto.
- `database`: Contém os arquivos relacionados ao banco de dados.
- `utils`: Contém funções auxiliares e utilitários.

### Armazenamento e Gerenciamento de Dados

O armazenamento e o gerenciamento de dados são realizados usando o SQLite como banco de dados. A pasta `data` contém os seguintes subdiretórios:

- `raw`: Armazena os dados brutos coletados.
- `processed`: Armazena os dados processados e analisados.

### Visualização de Dados com Power BI

A visualização de dados é realizada usando o Power BI. A pasta `notebooks` contém os arquivos de relatórios do Power BI.

## Estrutura de Pastas

A estrutura de pastas do projeto é a seguinte:

```bash
.
├─ api/
│ ├─ controller/
│ ├─ routes/
│ ├─ service/
│ └─ tests/
├─ data/
│ ├─ raw/
│ └─ processed/
├─ docs/
├─ notebooks/
├─ src/
│ ├─ analysis/
│ ├─ config/
│ ├─ database/
│ └─ utils/
└─ .github/
```

Esta estrutura de pastas facilita a organização e a manutenção do projeto, permitindo uma separação clara entre os diferentes componentes e responsabilidades.

Este arquivo descreve a arquitetura e a estrutura de pastas do projeto, facilitando a compreensão e a colaboração dos desenvolvedores.
