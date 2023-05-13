# Define a imagem base
FROM postgres:13

# Copia o arquivo de inicialização do banco de dados
COPY init.sql /docker-entrypoint-initdb.d/

# Define a variável de ambiente para o usuário padrão
ENV POSTGRES_USER postgres

# Define a variável de ambiente para a senha do usuário padrão
ENV POSTGRES_PASSWORD postgres

# Define a variável de ambiente para o nome do banco de dados
ENV POSTGRES_DB mydb

# Define a porta que será exposta
EXPOSE 5432
