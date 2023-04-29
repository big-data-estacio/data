import os
import csv

# define as tabelas e colunas
tables = {
    "estoque_mercadorias": ["id", "nome", "quantidade"],
    "total_clientes": ["id", "nome", "quantidade"],
    "pratos": ["id", "nome", "preco"],
    "bebidas": ["id", "nome", "preco"]
}

# define o diretório onde os arquivos serão salvos
dir_path = "../data"

# verifica se o diretório existe, caso contrário, cria o diretório
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

# itera sobre as tabelas e cria um arquivo .csv para cada uma delas
for table, columns in tables.items():
    file_path = os.path.join(dir_path, f"{table}.csv")
    
    # verifica se o arquivo já existe, caso contrário, cria o arquivo com as colunas
    if not os.path.exists(file_path):
        with open(file_path, mode="w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(columns)
    
    # adiciona alguns dados de exemplo aos arquivos
    with open(file_path, mode="a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        for i in range(1, 6):
            writer.writerow([i, f"{table} {i}", i * 10])
