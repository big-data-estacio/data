FROM python:3.7-slim-buster

# Instala o sudo
RUN apt-get update && apt-get install -y sudo

# Define a diretório de trabalho
WORKDIR /app

# Copia os arquivos necessários para o diretório de trabalho
COPY requirements.txt ./
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Define a variável de ambiente
ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

# Define a porta que a aplicação estará escutando
EXPOSE 8501

# Executa a aplicação
CMD [ "streamlit", "run", "app.py" ]
