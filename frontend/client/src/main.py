from database.crud import create_data, read_data, update_data, delete_data
import pandas as pd

# Cria um novo registro no banco de dados
new_data = {"name": "Restaurante XYZ", "address": "Rua A, 123", "rating": 4.5}
create_data(new_data)

# Lê os dados do banco de dados em um dataframe
data = pd.DataFrame(read_data())

# Atualiza um registro existente no banco de dados
update_data(1, {"name": "Restaurante ABC", "address": "Rua B, 456", "rating": 4.0})

# Deleta um registro existente no banco de dados
delete_data(2)

# Exporta os dados do dataframe para um arquivo .csv
data.to_csv("data.csv", index=False)
