# Use a imagem base do Python
FROM python:3.8-slim-buster

# Instale as dependências do sistema necessárias para o psycopg2
RUN apt-get update && apt-get install -y postgresql-client

# Crie um diretório de trabalho
WORKDIR /app

# Copie os arquivos do projeto para o contêiner
COPY . .

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Crie um usuário e um banco de dados no PostgreSQL dentro do contêiner
RUN su - postgres -c "psql -c \"CREATE USER <nome_do_usuario> WITH PASSWORD '<senha_do_usuario>'\"" && \
    su - postgres -c "createdb -O <nome_do_usuario> <nome_do_banco_de_dados>"

# Exponha a porta 8501 para o streamlit
EXPOSE 8501

# Inicie o projeto com o streamlit
CMD ["streamlit", "run", "app.py"]
