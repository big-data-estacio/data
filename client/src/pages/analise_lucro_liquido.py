import pandas as pd
import streamlit as st
from deta import Deta


DETA_KEY = "e0u31gqkqju_2Ps7fJD5a1kAKF2Rr4Y31ASSdvUUeX8Y"
deta = Deta(DETA_KEY)


db_deta_lucroliquido = deta.Base("lucroliquido")

class DadosRestaurante:
  def __init__(self):
    self.data = pd.DataFrame()

  def load_data_from_deta(self):
    items = db_deta_lucroliquido.fetch().items
    self.data = pd.DataFrame(items)

  def show_table(self):
    st.write(self.data)

  def add_data_to_deta(self, data_dict):
    db_deta_lucroliquido.put(data_dict)

  def is_deta_empty(self):
    items = db_deta_lucroliquido.fetch().items
    return len(items) == 0

class AnaliseLucroLiquido:
  def __init__(self, dados: DadosRestaurante):
    self.dados = dados

    def calcular_lucro_liquido(self):
      custos_fixos = self.dados.data["Custos fixos"].sum()
      custos_variaveis = self.dados.data["Custos variáveis"].sum()
      receita_total = self.dados.data["Receita total"].sum()

      lucro_liquido = receita_total - custos_fixos - custos_variaveis

      return lucro_liquido

def analise_lucro_liquido(dados: DadosRestaurante):
  st.subheader("Análise de Lucro Líquido")

  # Exibir dados em uma tabela
  dados.show_table()

  # Calcular lucro líquido
  analise = AnaliseLucroLiquido(dados)
  lucro_liquido = analise.calcular_lucro_liquido()

  st.write(f"Lucro líquido: R$ {lucro_liquido:.2f}")

  # Verificar se o banco de dados está vazio
  if dados.is_deta_empty():
    # Se estiver vazio, adicionar os dados
    dados.add_data_to_deta({"lucro_liquido": 5000, "data": "2023-05-11"})
    st.info("Dados adicionados ao banco de dados Deta com sucesso!")
  else:
    # Se não estiver vazio, apenas informar o lucro líquido
    st.info("Lucro líquido salvo no banco Deta com sucesso!")

dados = DadosRestaurante()
dados.load_data_from_deta()
analise_lucro_liquido(dados)