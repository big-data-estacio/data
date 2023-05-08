import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')

# Atualizando os dados da tabela bebidas
conn.execute("UPDATE bebidas SET PRECO = 4.00 WHERE ID = 2")

# Fechando a conexão com o banco de dados
conn.close()
