import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')

# Inserindo dados na tabela bebidas
conn.execute("INSERT INTO bebidas (ID, NOME, PRECO) VALUES (1, 'Coca-Cola', 4.50)")
conn.execute("INSERT INTO bebidas (ID, NOME, PRECO) VALUES (2, 'Guaraná', 3.50)")
conn.execute("INSERT INTO bebidas (ID, NOME, PRECO) VALUES (3, 'Suco de Laranja', 5.00)")

# Fechando a conexão com o banco de dados
conn.close()
