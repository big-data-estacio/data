import pandas as pd
from flask import jsonify

mercadorias_df = pd.read_csv('mercadorias.csv')

def get_mercadorias():
    mercadorias = mercadorias_df.to_dict('records')
    return jsonify(mercadorias)
