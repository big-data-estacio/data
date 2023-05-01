FROM python:3.9-slim-buster

WORKDIR /app

# Instala as dependências do PySpark
RUN apt-get update && apt-get install -y openjdk-11-jre-headless && \
    pip3 install pyspark==2.4.8

# Instala o streamlit e adiciona seu diretório ao PATH do sistema
RUN pip3 install streamlit && \
    echo 'export PATH="/root/.local/bin:$PATH"' >> /root/.bashrc

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "client/app.py", "--server.port", "8501"]
