import pandas as pd
from flask import jsonify

clientes_df = pd.read_csv('clientes.csv')

def get_clientes():
    clientes = clientes_df.to_dict('records')
    return jsonify(clientes)
