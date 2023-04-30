from flask import Blueprint, jsonify
import pandas as pd

clientes_bp = Blueprint('clientes', __name__)

@clientes_bp.route('/clientes', methods=['GET'])
def listar_clientes():
    clientes_df = pd.read_csv('../data/clientes.csv')
    clientes_json = clientes_df.to_dict(orient='records')
    return jsonify(clientes_json)
