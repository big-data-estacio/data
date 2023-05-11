import pandas as pd
import streamlit as st

def mapaVisual():
  st.markdown("### MAPA")
  st.markdown("###### AQUI VOCÊ PODE VER O MAPA DE FLORIANÓPOLIS COM TODOS OS RESTAURANTES")
  st.markdown("### Mapa")
  st.markdown("Este mapa mostra a localização do restaurante Pedacinho do Céu.")
  # Definindo as informações de latitude e longitude manualmente
  locations = [
    [-27.7817, -48.5092]
  ]

  # Criando um dataframe com as informações de latitude e longitude
  df_locations = pd.DataFrame(
    locations,
    columns=['latitude', 'longitude']
  )

  # Exibindo o mapa com as informações de latitude e longitude
  st.map(df_locations)

  st.markdown("Estamos localizados na Rua Joaquim Neves, 152, no Praia do Sul da Ilha. Venha nos visitar e experimentar nossos deliciosos pratos!")
