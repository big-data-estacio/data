import pandas as pd
import streamlit as st
from deta import Deta


DETA_KEY = "e0u31gqkqju_2Ps7fJD5a1kAKF2Rr4Y31ASSdvUUeX8Y"
deta = Deta(DETA_KEY)


db_deta_lucroliquido = deta.Base("lucroliquido")

def calculate_net_profit():
  # Buscando todos os dados do banco Deta
  items = db_deta_lucroliquido.fetch().items
  
  # Se houver itens, calcular o lucro líquido e exibi-lo
  if items:
    # Criando um DataFrame com os dados
    data = pd.DataFrame([item for item in items])
    
    # Calculando o lucro líquido
    lucro_liquido = data['lucro_liquido'].sum()
    
    # Criando um DataFrame para exibir o lucro líquido
    df_lucro_liquido = pd.DataFrame({'Lucro Líquido': [lucro_liquido]})
    
    # Exibindo o DataFrame
    st.dataframe(df_lucro_liquido)