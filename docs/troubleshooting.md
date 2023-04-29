# Solução de problemas (Troubleshooting)

Este documento fornece algumas soluções para problemas comuns que podem ocorrer ao configurar e executar o projeto "Restaurante Pedacinho do Céu".

## Problemas comuns

### 1. Erro ao instalar as dependências do projeto

Se você encontrar problemas ao instalar as dependências do projeto usando o comando `pip install -r requirements.txt`, verifique se você está usando a versão correta do Python (3.7+). Você também pode tentar criar e ativar um ambiente virtual antes de instalar as dependências.

### 2. Erro ao executar o projeto com o Docker

Se você encontrar problemas ao executar o projeto usando o Docker, verifique se o Docker está instalado corretamente em seu computador. Se o problema persistir, tente reconstruir a imagem do Docker usando o comando `docker build -t restaurante-pedacinho-do-ceu .` e execute o contêiner novamente com o comando `docker run -p 5000:5000 restaurante-pedacinho-do-ceu`.

### 3. Erro ao executar os testes

Se você encontrar problemas ao executar os testes com o comando `pytest api/tests`, verifique se você instalou as dependências de teste usando o comando `pip install -r requirements-test.txt`. Se o problema persistir, verifique se os arquivos de teste estão no diretório correto (`api/tests`).

## Suporte

Se você encontrar um problema que não está listado aqui ou precisa de mais ajuda para resolver um problema, sinta-se à vontade para abrir uma issue no GitHub ou entrar em contato com os colaboradores do projeto.
