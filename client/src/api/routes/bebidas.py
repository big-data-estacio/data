from flask import Blueprint, jsonify
import pandas as pd

bebidas_bp = Blueprint('bebidas', __name__)

@bebidas_bp.route('/bebidas', methods=['GET'])
def listar_bebidas():
    bebidas_df = pd.read_csv('../data/bebidas.csv')
    bebidas_json = bebidas_df.to_dict(orient='records')
    return jsonify(bebidas_json)
