FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y sqlite3 libsqlite3-dev && \
    pip install sqlite-utils

RUN useradd -m -U -u 1000 dockeruser

WORKDIR /app

COPY criar_banco.py .

RUN chown -R dockeruser:dockeruser /app

USER dockeruser

CMD ["python", "criar_banco.py"]

EXPOSE 5000
