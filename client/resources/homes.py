import hashlib
import smtplib
import yagmail
import requests
import csv
import os
import logging
from faker import Faker
import altair as alt
import pydeck as pdk
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from dotenv import load_dotenv
from PIL import Image
import matplotlib.pyplot as plt
import datetime

def home():
  st.markdown("### HOME")
  st.markdown("###### ESTA É A PÁGINA INICIAL DO PROJETO")
  st.markdown("###### AQUI VOCÊ PODE SELECIONAR AS PÁGINAS QUE DESEJA VISUALIZAR")
  st.markdown("###### ABAIXO VOCÊ PODE VER O MAPA, OS GRÁFICOS E OS DADOS BRUTOS")
  st.markdown("###### VOCÊ PODE SELECIONAR O QUE DESEJA VER NO MENU DA ESQUERDA")

  # Gráfico de vendas mensais
  st.markdown("#### Gráfico de Vendas Mensais")
  data_vendas = pd.DataFrame({
      'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
      'Vendas': [5000, 7000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000]
  })
  fig = px.line(data_vendas, x='Mês', y='Vendas')
  st.plotly_chart(fig)

  # Fotos dos Pratos
  st.markdown("## Fotos dos Pratos")
  # Cria duas colunas de largura igual
  col1, col2 = st.columns(2)

  # Adiciona conteúdo na primeira coluna
  with col1:
      st.header("Primeira Coluna")
      st.write("Conteúdo da primeira coluna")

  # Adiciona conteúdo na segunda coluna
  with col2:
      st.header("Segunda Coluna")
      st.write("Conteúdo da segunda coluna")

  # Avaliação dos Clientes
  st.markdown("## Avaliação dos Clientes")
  st.write("Média de avaliação: 4.5")
  st.write("Comentários:")
  st.write("- Comida deliciosa!")
  st.write("- Ótimo atendimento!")
  st.write("- Preços justos!")