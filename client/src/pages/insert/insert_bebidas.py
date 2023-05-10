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
import client.src.pages.criar_conta as conta
import client.src.pages.informacoes as info


DETA_KEY = "e0u31gqkqju_2Ps7fJD5a1kAKF2Rr4Y31ASSdvUUeX8Y"
deta = Deta(DETA_KEY)
db_deta_bebidas = deta.Base("bebidas")

def inserir_bebida(id, nome, preco, quantidade, descricao, total_vendas, quantidade_vendas):
              # Get database
  db_bebidas = deta.Base("bebidas")

  # Put new drink into the database
  db_bebidas.put({
      "key": id,
      "nome": nome,
      "preco": preco,
      "quantidade": quantidade,
      "descricao": descricao,
      "total_vendas": total_vendas,
      "quantidade_vendas": quantidade_vendas
  })

  st.success('Bebida inserida com sucesso!')

  # Get the "bebidas" database
  db_bebidas = deta.Base("bebidas")

  # Ask the user if they want to see the bubble chart
  show_chart = st.radio('Deseja visualizar o gráfico de bolhas para as bebidas?', ('Sim', 'Não'))

  if show_chart == 'Sim':
    st.markdown("##### CLASSIFICAÇÃO DE BEBIDAS ★★★★★")

    # Fetch data from the "bebidas" database and convert it to a DataFrame
    fetch_response = db_bebidas.fetch()
    data = [item for item in fetch_response.items]
    df_bebidas = pd.DataFrame(data)

    # Create a bubble chart with price on the x-axis, quantity sold on the y-axis, and bubble size representing total sales
    chart = alt.Chart(df_bebidas).mark_circle().encode(
        x=alt.X('preco', title='Preço'),
        y=alt.Y('quantidade_vendas', title='Quantidade Vendida'),
        size=alt.Size('total_vendas', title='Total de Vendas'),
        color=alt.Color('nome', title='Bebida'),
        tooltip=['nome', 'preco', 'quantidade_vendas', 'total_vendas']
    ).properties(width=700, height=500)

    # Display the chart
    st.altair_chart(chart)
