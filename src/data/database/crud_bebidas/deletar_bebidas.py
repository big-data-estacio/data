import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')

# Deletando os dados da tabela bebidas
conn.execute("DELETE FROM bebidas WHERE ID = 1")

# Fechando a conexão com o banco de dados
conn.close()
