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
# from src.pages.menu import selecionar


def vendas_por_categoria(dados):
  # Gráfico de bolhas
  fig = px.scatter(dados, x='Categoria', y='Vendas',
                    size='Preço Médio', hover_name='Categoria')
  st.plotly_chart(fig)

  # Salvar dados em arquivo
  dados.to_csv('client/src/data/vendasCategorias.csv', index=False)

  # Projeção de vendas
  st.subheader('Projeção de vendas para a próxima semana')

  # Calcular média de vendas e preço médio
  media_vendas = dados['Vendas'].mean()
  media_preco = dados['Preço Médio'].mean()

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
