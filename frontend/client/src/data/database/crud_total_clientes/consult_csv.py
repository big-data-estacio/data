import pandas as pd


# consult = str(input('Digite o nome da tabela que deseja consultar: '))
# df_consult = pd.read_csv(consult + '.csv')
# print(df_consult.head())

# Lendo o arquivo bebidas.csv
df_bebidas = pd.read_csv('../bebidas.csv')

# Exibindo as primeiras linhas do arquivo
print(df_bebidas.head())

# Fazendo uma consulta aos dados do arquivo
bebidas_caro = df_bebidas[df_bebidas['PRECO'] > 2]
print(bebidas_caro)


