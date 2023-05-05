import hashlib
import smtplib
import csv
import os
import logging
import altair as alt
import pydeck as pdk
import pandas as pd
import numpy as np
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
import client.setup as setup
titlePlaceholder = st.empty()



if __name__ == '__main__':
  # Encerrar a sessão do Spark
  # spark.stop()
  
  def login_page():
    st.title("Login")
    original_title = '<p style="font-family:Monospace; color:Gray; font-size: 25px;"></p>'
    titlePlaceholder.markdown(original_title, unsafe_allow_html=True)

    # Solicitar nome de usuário e senha
    username = st.text_input("Nome de usuário", key="username_input")
    password = st.text_input("Senha", type="password", key="password_input")
    st.button("Login")

    if setup.authenticate_user(username, password):
        st.empty()
        
        return True
    else:
        # Informa que o nome de usuário ou senha estão incorretos
        if username == "" and password == "":
          st.error("Por favor, insira um nome de usuário e senha.")
        # caso o usuario tenha inserido nome de usuario e senha incorretos
        elif username != "" and password != "":
          st.error("Nome de usuário ou senha incorretos.")
        # authenticate_user = False
        return False
    
  if "logged_in" not in st.session_state:
      st.session_state.logged_in = False

  if not st.session_state.logged_in:
      logged_in = login_page()

      if logged_in:
          st.session_state.logged_in = True
          st.experimental_rerun()
  else:
      st.empty()
      setup.mainLogin()
