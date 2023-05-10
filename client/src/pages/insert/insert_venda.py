from datetime import datetime
import hashlib
# import json
import smtplib
import csv
import os
import logging
import altair as alt
import pydeck as pdk
import pandas as pd
import numpy as np
# import base64
import plotly.express as px
import plotly.graph_objects as go
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import streamlit as st
import time
import plotly.graph_objects as go
from PIL import Image
import hydralit_components as hc
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from deta import Deta


DETA_KEY = "e0u31gqkqju_2Ps7fJD5a1kAKF2Rr4Y31ASSdvUUeX8Y"
deta = Deta(DETA_KEY)
db = deta.Base("data")
# TODO - Conecte-se às bases de dados
db_deta_categoriavendas = deta.Base("categoriavendas")


# TODO Inserir dados no banco venda
def inserir_venda(id, categoria, vendas, preco_medio):
  # Insert data into the "venda" database
  db_deta_categoriavendas.put({
      "ID": id,
      "Categoria": categoria,
      "Vendas": vendas,
      "PrecoMedio": preco_medio
  })

  st.success('Venda cadastrada com sucesso!')
  
  show_chart = st.radio('Deseja visualizar o gráfico de bolhas para as vendas?', ('Sim', 'Não'))

  if show_chart == 'Sim':
    st.markdown("### Comparação de Categoria de Vendas")
    st.markdown("Neste gráfico, cada bolha representa uma categoria de vendas e o tamanho da bolha representa o Preço Médio.")
    st.markdown("##### CLASSIFICAÇÃO DE DADOS DE VENDAS ★★★★★")

    # Fetch data from the "venda" database and convert it to a DataFrame
    fetch_response = db_deta_categoriavendas.fetch()
    data = [item for item in fetch_response.items]
    df_vendas = pd.DataFrame(data)

    # Create a bubble chart with category on x-axis, sales on y-axis, and color representing the average price
    chart = alt.Chart(df_vendas).mark_circle(size=100).encode(
        x='Categoria',
        y='Vendas',
        color='PrecoMedio',
        tooltip=['Categoria', 'Vendas', 'PrecoMedio']
    ).properties(
        width=600,
        height=400
    )

    # Display the chart
    st.altair_chart(chart, use_container_width=True)
