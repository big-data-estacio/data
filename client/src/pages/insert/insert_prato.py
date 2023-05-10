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
db_deta_pratos = deta.Base("prato")

# TODO Inserir dados no banco prato
def inserir_prato(id, nome, preco, acompanhamento):
  # Insert data into the "prato" database
  db_deta_pratos.put({
      "ID": id,
      "NOME": nome,
      "PRECO": preco,
      "ACOMPANHAMENTO": acompanhamento
  })

  st.success('Prato cadastrado com sucesso!')
  
  show_chart = st.radio('Deseja visualizar o gráfico de bolhas para os pratos?', ('Sim', 'Não'))

  if show_chart == 'Sim':
    st.markdown("### Comparação de Pratos")
    st.markdown("Neste gráfico, cada bolha representa um prato e o tamanho da bolha representa a quantidade em estoque.")
    st.markdown("##### CLASSIFICAÇÃO DE DADOS DE PRATOS ★★★★★")

    # Fetch data from the "prato" database and convert it to a DataFrame
    fetch_response = db_deta_pratos.fetch()
    data = [item for item in fetch_response.items]
    df_pratos = pd.DataFrame(data)

    # Create a bubble chart with dish name on x-axis, price on y-axis, and color representing the accompaniment
    chart = alt.Chart(df_pratos).mark_circle(size=100).encode(
        x='NOME',
        y='PRECO',
        color='ACOMPANHAMENTO',
        tooltip=['NOME', 'PRECO', 'ACOMPANHAMENTO']
    ).properties(
        width=600,
        height=400
    )

    # Display the chart
    st.altair_chart(chart, use_container_width=True)