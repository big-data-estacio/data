from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType
import hashlib
import csv
from typing import List, Dict
import hydralit_components as hc
from datetime import datetime
import json
import smtplib
from datetime import date, timedelta
import os
from client.resources.developers import developers
import logging
from streamlit_lottie import st_lottie
import altair as alt
import pydeck as pdk
import pandas as pd
import numpy as np
import base64
import plotly.express as px
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import streamlit as st
import time
import plotly.graph_objects as go
from PIL import Image
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from deta import Deta


DETA_KEY = "e0u31gqkqju_2Ps7fJD5a1kAKF2Rr4Y31ASSdvUUeX8Y"
deta = Deta(DETA_KEY)

def cadastrar_venda():
  db_deta_previsaoVendas = deta.Base("previsaoVendas")

  st.title("Previsão de Vendas")

  # Input para a data da venda
  data = st.date_input("Data da venda")

  # Input para o total de vendas
  total_vendas = st.number_input("Total de vendas")

  # Botão para cadastrar a venda
  if st.button("Cadastrar Venda"):
    # Adiciona a venda no banco de dados
    db_deta_previsaoVendas.put({"key": str(data), "Data": data.isoformat(), "Total Vendas": total_vendas})
    st.success("Venda cadastrada com sucesso!")

  # Obtém todas as vendas do banco de dados
  todas_vendas = list(db_deta_previsaoVendas.fetch().items)

  if todas_vendas:
    # Cria um DataFrame a partir dos dados
    dados = pd.DataFrame(todas_vendas)

    # Converte a coluna 'Data' para datetime
    dados["Data"] = pd.to_datetime(dados["Data"])

    # Gráfico de linha
    fig, ax = plt.subplots()
    ax.plot(dados["Data"], dados["Total Vendas"])
    ax.set_xlabel("Data")
    ax.set_ylabel("Total de Vendas")
    ax.set_title("Previsão de Vendas")
    st.pyplot(fig)