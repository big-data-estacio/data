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

# Load environment variables
DETA_KEY = "e0u31gqkqju_2Ps7fJD5a1kAKF2Rr4Y31ASSdvUUeX8Y"
# Initialize Deta
deta = Deta(DETA_KEY)
# Get database
db = deta.Base("data")
# TODO - Conecte-se às ba


def insert_data(username, name, password):
    return db.put(
    {
        "key": username,
        "name": name,
        "password": password
    }
  )



# TODO - Criar conta no banco
def criar_conta():
    logging.info('O cliente começou a criar uma conta')

    # Solicitar nome de usuário e senha para criar uma conta
    new_username = st.text_input("Nome de usuário", key="new_username_input")
    new_password = st.text_input("Senha", type="password", key="new_password_input")

    if st.button("Criar conta"):
        # Verificar se o nome de usuário já existe
        if db.get(new_username):
            st.error("Nome de usuário já existe. Por favor, escolha outro.")
            return False

        # Caso contrário, adicionar o novo nome de usuário e senha no banco de dados
        insert_data(new_username, new_username, new_password) 

        st.success("Conta criada com sucesso!")
        return True

    return False
