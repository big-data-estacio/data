import pandas as pd
from flask import jsonify

bebidas_df = pd.read_csv('bebidas.csv')

def get_bebidas():
    bebidas = bebidas_df.to_dict('records')
    return jsonify(bebidas)
