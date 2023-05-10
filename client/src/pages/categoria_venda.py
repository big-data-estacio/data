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
db = deta.Base("data")
# TODO - Conecte-se às bases de dados
db_deta_categoriavendas = deta.Base("categoriavendas")


def vendas_por_categoria():
  # Obtém todas as entradas do banco de dados
  todas_categoriavendas = list(db_deta_categoriavendas.fetch().items)
  dados = pd.DataFrame(todas_categoriavendas)

  # Converte as colunas 'Vendas' e 'PrecoMedio' para numéricas
  dados['Vendas'] = pd.to_numeric(dados['Vendas'], errors='coerce')
  dados['PrecoMedio'] = pd.to_numeric(dados['PrecoMedio'], errors='coerce')

  # Gráfico de bolhas
  fig = px.scatter(dados, x='Categoria', y='Vendas', size='PrecoMedio', hover_name='Categoria')
  st.plotly_chart(fig)

  # Projeção de vendas
  st.subheader('Projeção de vendas para a próxima semana')

  # Calcular média de vendas e PrecoMedio
  media_vendas = dados['Vendas'].mean()
  media_preco = dados['PrecoMedio'].mean()

  # Calcular projeção de vendas
  projecao_vendas = media_vendas * 1.1

  # Calcular projeção de receita
  projecao_receita = projecao_vendas * media_preco

  # Exibir resultados
  st.write('Média de vendas da última semana:', media_vendas)
  st.write('Média de preço da última semana:', media_preco)
  st.write('Projeção de vendas para a próxima semana:', projecao_vendas)
  st.write('Projeção de receita para a próxima semana:', projecao_receita)

  # Gráfico de barras
  grafico = px.bar(dados, x='Categoria', y='Vendas', color='Categoria')
  st.plotly_chart(grafico)