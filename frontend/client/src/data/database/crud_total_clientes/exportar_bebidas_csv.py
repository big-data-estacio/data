import sqlite3
import csv

# Abre uma conexão com o banco de dados
conn = sqlite3.connect('exemplo.db')

# Executa uma query para pegar todos os dados da tabela bebidas
cursor = conn.cursor()
cursor.execute("SELECT * FROM bebidas")
dados = cursor.fetchall()

# Escreve os dados em um arquivo CSV
with open('../bebidas.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID', 'NOME', 'PRECO'])
    writer.writerows(dados)

# Fecha a conexão com o banco de dados
conn.close()
