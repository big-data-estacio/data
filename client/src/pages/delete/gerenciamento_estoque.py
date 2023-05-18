import logging
import pandas as pd
import streamlit as st
from deta import Deta


DETA_KEY = "e0u31gqkqju_2Ps7fJD5a1kAKF2Rr4Y31ASSdvUUeX8Y"
deta = Deta(DETA_KEY)


def gerenciar_estoque():
  logging.info('O cliente acessou o estoque')
  # Conectar ao banco de dados
  db_deta_estoque = deta.Base('estoque')

  def show_table():
    # Fetch data from the "estoque" database and convert it to a DataFrame
    fetch_response = db_deta_estoque.fetch()
    data = [item for item in fetch_response.items]
    df_estoque = pd.DataFrame(data)

    # Display the DataFrame
    st.write(df_estoque)

  def delete_by_id(id):
    db_deta_estoque.delete(str(id))  # Convert the ID to string here
    st.success("Dados deletados com sucesso!")

  # Display data in a table
  show_table()
  id_to_delete = st.number_input("Digite o ID do registro que deseja deletar:", min_value=1)
  if st.button("Deletar"):
    delete_by_id(id_to_delete)
  if st.button("Deseja ver os dados atualizados?"):
    show_table()
