import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from deta import Deta


DETA_KEY = "e0u31gqkqju_2Ps7fJD5a1kAKF2Rr4Y31ASSdvUUeX8Y"
deta = Deta(DETA_KEY)

def cadastrar_venda():
  db_deta_previsaoVendas = deta.Base("previsaoVendas")

  st.title("Previsão de Vendas")

  # Input para a data da venda
  data = st.date_input("Data da venda")

  # Input para o total de vendas
  total_vendas = st.number_input("Total de vendas")

  # Botão para cadastrar a venda
  if st.button("Cadastrar Venda"):
    # Adiciona a venda no banco de dados
    db_deta_previsaoVendas.put({"key": str(data), "Data": data.isoformat(), "Total Vendas": total_vendas})
    st.success("Venda cadastrada com sucesso!")

  # Obtém todas as vendas do banco de dados
  todas_vendas = list(db_deta_previsaoVendas.fetch().items)

  if todas_vendas:
    # Cria um DataFrame a partir dos dados
    dados = pd.DataFrame(todas_vendas)

    # Converte a coluna 'Data' para datetime
    dados["Data"] = pd.to_datetime(dados["Data"])

    # Gráfico de linha
    fig, ax = plt.subplots()
    ax.plot(dados["Data"], dados["Total Vendas"])
    ax.set_xlabel("Data")
    ax.set_ylabel("Total de Vendas")
    ax.set_title("Previsão de Vendas")
    st.pyplot(fig)