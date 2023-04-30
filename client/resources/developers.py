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

def developers():
  st.title("Análise de sentimento de Vendas do Restaurante Pendacinho do Céu")
  st.sidebar.title("Análise de sentimento de Vendas do Restaurante Pendacinho do Céu")

  st.markdown("Este aplicativo é um painel Streamlit para analisar os dados de um Restaurante 🐦🐦")
  st.sidebar.markdown("Este aplicativo é um painel Streamlit para analisar os dados de um Restaurante 🐦🐦")

  st.title('Streamlit Tutorial')
  st.markdown('')
  st.markdown('''
  - developped by [`@estevam5s`](https://github.com/estevam5s/)
  - [`Github 💻 streamlit-tutorial`](https://github.com/estevam5s/Streamlit-Tutorial)
  ''')
  st.info('Streamlit é uma estrutura python de código aberto para a criação de aplicativos web para Machine Learning e Data Science. Podemos desenvolver instantaneamente aplicativos da web e implantá-los facilmente usando o Streamlit. O Streamlit permite que você escreva um aplicativo da mesma forma que escreve um código python. O Streamlit facilita o trabalho no loop interativo de codificação e visualização de resultados no aplicativo Web.')

  st.header('Streamlit Gallery 🖼️')

  with st.expander('Example 1'):
      st.markdown('''
  ## 💸 Clonando o repositório ✨

  # clone other repositories
  git clone https://github.com/big-data-estacio/data.git

      ''')

  with st.expander('Example 2'):
      st.markdown('''
  ## 💸 Instalação de bibliotecas ✨

    ```
  pip install -r requirements.txt
  ```
      ''')

  with st.expander('Example 3'):
      st.markdown('''
  ## 💸 Executando o projeto ✨

  ```
  streamlit run app.py
  ```
      ''')

  # bibliotecas do projeto

  with st.expander('Example 4'):
      st.markdown('''
  ## 💸 Bibliotecas do projeto ✨

  ```
  hashlib
  smtplib
  yagmail
  requests
  csv
  os
  logging
  Faker
  altair
  pydeck
  pandas
  numpy
  plotly.express
  plotly.graph_objects
  dotenv
  matplotlib.pyplot
  datetime
  streamlit
  streamlit_authenticator
  plotly.graph_objects
  plotly.subplots
  PIL
  hydralit_components
  ```
      ''')

  st.markdown('---')
  st.header('Streamlit API reference')
  st.markdown('')
  st.markdown('''
  **📒 Useful resource**
  - [`streamlit.io`](https://docs.streamlit.io/)
  - [`awesome-streamlit`](https://github.com/MarcSkovMadsen/awesome-streamlit)
  - [`streamlit gallery`](https://streamlit.io/gallery)
  - [`Python Streamlit 사용법 - 프로토타입 만들기`](https://zzsza.github.io/mlops/2021/02/07/python-streamlit-dashboard/)

  ''')

  st.code('import streamlit as st')