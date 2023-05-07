# Use a imagem base do Python
FROM python:3.8-slim-buster

# Instale o pacote mysql-client
RUN apt-get update && apt-get install -y default-mysql-client

# Crie um diretório de trabalho
WORKDIR /app

# Copie os arquivos do projeto para o contêiner
COPY . .

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Configure o MySQL dentro do contêiner
RUN apt-get update && \
    apt-get install -y default-mysql-server && \
    service mysql start && \
    mysql -u root -e "CREATE DATABASE big_data_app" && \
    mysql -u root -e "CREATE USER 'user'@'localhost' IDENTIFIED BY 'user'" && \
    mysql -u root -e "GRANT ALL PRIVILEGES ON big_data_app.* TO 'user'@'localhost'"

# Exponha a porta 8501 para o streamlit
EXPOSE 8501

# Inicie o projeto com o streamlit
CMD ["streamlit", "run", "app.py"]
