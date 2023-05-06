# Use a imagem base do Python
FROM python:3.8-slim-buster

# Crie um diretório de trabalho
WORKDIR /app

# Copie os arquivos do projeto para o contêiner
COPY . .

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta 8501 para o streamlit
EXPOSE 8501

# Inicie o projeto com o streamlit
CMD ["streamlit", "run", "app.py"]
