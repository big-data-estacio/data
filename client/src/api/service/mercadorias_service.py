import pandas as pd

class MercadoriasService:
    def __init__(self, mercadorias_file_path):
        self.mercadorias = pd.read_csv(mercadorias_file_path)

    def listar_mercadorias(self):
        return self.mercadorias.to_dict('records')

    def buscar_mercadoria_por_id(self, id):
        mercadoria = self.mercadorias.loc[self.mercadorias['ID'] == id].to_dict('records')
        if not mercadoria:
            return None
        return mercadoria[0]
