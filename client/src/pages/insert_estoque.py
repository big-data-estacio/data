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


DETA_KEY = "e0u31gqkqju_2Ps7fJD5a1kAKF2Rr4Y31ASSdvUUeX8Y"
deta = Deta(DETA_KEY)
# TODO - Conecte-se às bases de dados
db_deta_estoque = deta.Base("estoque")


def inserir_estoque(id, nome, quantidade):
  # Insert data into the "estoque" database
  db_deta_estoque.put({
      "ID": id,
      "NOME": nome,
      "QUANTIDADE": quantidade
  })

  st.success('Estoque atualizado com sucesso!')

  show_chart = st.radio('Deseja visualizar o gráfico de bolhas para o estoque?', ('Sim', 'Não'))

  if show_chart == 'Sim':
    st.markdown("### A COMPARAÇÃO DO ESTOQUE DE MERCADORIAS")
    st.markdown("Esta é a comparação do estoque de mercadorias por ID e quantidade. Aqui no eixo X, temos o ID e no eixo Y, a quantidade em estoque.")
    st.markdown("##### ESTOQUE DE MERCADORIAS ★★★★★")

    # Fetch data from the "estoque" database and convert it to a DataFrame
    fetch_response = db_deta_estoque.fetch()
    data = [item for item in fetch_response.items]
    df_mercadorias = pd.DataFrame(data)

    # Create a bar chart with ID on the x-axis and quantity on the y-axis
    chart = alt.Chart(df_mercadorias).mark_bar().encode(
        x=alt.X('ID', title='ID'),
        y=alt.Y('QUANTIDADE', title='Quantidade em Estoque'),
        tooltip=['NOME', 'QUANTIDADE']
    ).properties(width=700, height=500)

    # Display the chart
    st.altair_chart(chart)