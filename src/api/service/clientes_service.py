import pandas as pd

class ClientesService:
    def __init__(self, clientes_file_path):
        self.clientes = pd.read_csv(clientes_file_path)

    def listar_clientes(self):
        return self.clientes.to_dict('records')

    def buscar_cliente_por_id(self, id):
        cliente = self.clientes.loc[self.clientes['ID'] == id].to_dict('records')
        if not cliente:
            return None
        return cliente[0]
