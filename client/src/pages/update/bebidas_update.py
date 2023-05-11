import streamlit as st
import pandas as pd


class Bebidas:
  def __init__(self, db_bebidas):
    self.db_bebidas = db_bebidas
    self.load_data()
  
  def load_data(self):
    fetch_response = self.db_bebidas.fetch()
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