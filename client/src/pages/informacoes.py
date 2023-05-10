import logging
import streamlit as st


class ExibidorInformacoesRestaurante:
    
  def __init__(self, horarios):
      self.horarios = horarios
  
  def exibir_informacoes(self):
      st.markdown("## Horário de Funcionamento")
      for dia, horario in self.horarios.items():
          st.markdown(f"{dia.capitalize()}: {horario}")
