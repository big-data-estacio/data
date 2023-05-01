FROM python:3.9-slim-buster

WORKDIR /app

# Instalação das dependências
RUN pip3 install streamlit \
                pyspark==2.4.8 \
                pandas \
                matplotlib \
                seaborn \
                scikit-learn

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.port", "8501"]
