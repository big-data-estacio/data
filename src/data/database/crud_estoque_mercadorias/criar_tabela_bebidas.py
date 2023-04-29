import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')

# Criando a tabela bebidas
conn.execute('''
    CREATE TABLE bebidas
    (ID INT PRIMARY KEY NOT NULL,
    NOME TEXT NOT NULL,
    PRECO REAL NOT NULL);
''')

# Fechando a conexão com o banco de dados
conn.close()
