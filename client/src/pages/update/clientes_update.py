import streamlit as st
import pandas as pd


class Clientes:
  def __init__(self, db_clientes):
    self.db_clientes = db_clientes
    self.load_data()
  
  def load_data(self):
    fetch_response = self.db_clientes.fetch()
    self.data = pd.DataFrame([item for item in fetch_response.items])

  def show_table(self):
    st.write(self.data)
  
  def update_by_id(self, id):
    item_key = str(id)
    update_data = {}
    for col in self.data.columns:
        if col != 'key':
            new_val = st.text_input(f"Novo valor para {col.capitalize()} (deixe em branco para não alterar):", value="")
            if new_val != "":
                update_data[col] = new_val
    return update_data