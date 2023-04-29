import pandas as pd

class BebidasService:
    def __init__(self, bebidas_file_path):
        self.bebidas = pd.read_csv(bebidas_file_path)

    def listar_bebidas(self):
        return self.bebidas.to_dict('records')

    def buscar_bebida_por_id(self, id):
        bebida = self.bebidas.loc[self.bebidas['ID'] == id].to_dict('records')
        if not bebida:
            return None
        return bebida[0]
