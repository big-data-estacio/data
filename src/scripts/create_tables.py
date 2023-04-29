import psycopg2
import csv

# Função para criar a tabela clientes
def create_table_clientes(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(50) NOT NULL,
            cpf VARCHAR(14) NOT NULL,
            email VARCHAR(50) NOT NULL,
            telefone VARCHAR(15) NOT NULL
        );
    """)

# Função para criar a tabela bebidas
def create_table_bebidas(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS bebidas (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(50) NOT NULL,
            descricao VARCHAR(100),
            valor DECIMAL(10,2) NOT NULL,
            quantidade INTEGER NOT NULL
        );
    """)

# Função para criar a tabela pratos
def create_table_pratos(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS pratos (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(50) NOT NULL,
            descricao VARCHAR(100),
            valor DECIMAL(10,2) NOT NULL,
            quantidade INTEGER NOT NULL
        );
    """)

# Função para criar a tabela estoque
def create_table_estoque(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS estoque (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(50) NOT NULL,
            quantidade INTEGER NOT NULL
        );
    """)

# Função para inserir dados na tabela clientes
def insert_data_clientes(cur):
    with open('clientes.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # Pula o cabeçalho do CSV
        for row in reader:
            cur.execute("""
                INSERT INTO clientes (nome, cpf, email, telefone)
                VALUES (%s, %s, %s, %s);
            """, (row[0], row[1], row[2], row[3]))

# Função para inserir dados na tabela bebidas
def insert_data_bebidas(cur):
    with open('bebidas.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # Pula o cabeçalho do CSV
        for row in reader:
            cur.execute("""
                INSERT INTO bebidas (nome, descricao, valor, quantidade)
                VALUES (%s, %s, %s, %s);
            """, (row[0], row[1], row[2], row[3]))

# Função para inserir dados na tabela pratos
def insert_data_pratos(cur):
    with open('pratos.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # Pula o cabeçalho do CSV
        for row in reader:
            cur.execute("""
                INSERT INTO pratos (nome, descricao, valor, quantidade)
                VALUES (%s, %s, %s, %s);
            """, (row[0], row[1], row[2], row[3]))

# Inserir dados na tabela "estoque"
def insert_data_estoque(cur):
    with open('estoque.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # Pula o cabeçalho do CSV
        for row in reader:
            cur.execute("""
                INSERT INTO estoque (produto, quantidade)
                VALUES (%s, %s)
            """, row)

# Inserir dados na tabela "clientes"
def insert_data_clientes(cur):
    with open('clientes.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # Pula o cabeçalho do CSV
        for row in reader:
            cur.execute("""
                INSERT INTO clientes (nome, telefone, email)
                VALUES (%s, %s, %s)
            """, row)

# Inserir dados na tabela "pratos"
def insert_data_pratos(cur):
    with open('pratos.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # Pula o cabeçalho do CSV
        for row in reader:
            cur.execute("""
                INSERT INTO pratos (nome, descricao, preco)
                VALUES (%s, %s, %s)
            """, row)

# Inserir dados na tabela "bebidas"
def insert_data_bebidas(cur):
    with open('bebidas.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # Pula o cabeçalho do CSV
        for row in reader:
            cur.execute("""
                INSERT INTO bebidas (nome, descricao, preco)
                VALUES (%s, %s, %s)
            """, row)

if __name__ == "__main__":
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="restaurante",
        user="postgres",
        password="postgres"
    )

    cur = conn.cursor()

    # Criar tabelas
    create_tables(cur)

    # Inserir dados nas tabelas
    insert_data_estoque(cur)
    insert_data_clientes(cur)
    insert_data_pratos(cur)
    insert_data_bebidas(cur)

    # Commitar as alterações e fechar a conexão
    conn.commit()
    cur.close()
    conn.close()
