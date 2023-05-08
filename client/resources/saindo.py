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

def sair():
    st.header("Autenticação de saída")
    login = st.text_input("Digite seu login:")
    senha = st.text_input("Digite sua senha:", type="password")
    enviar = st.button("Enviar")

    # utilize o arquivo .csv para criar o login e a senha

    with open("src/data/login.csv", "r") as arquivo:
        credenciais_salvas = arquivo.readlines()[1].strip().split(",")
        login_salvo = credenciais_salvas[0]
        senha_salva = credenciais_salvas[1]

    if enviar:
        if login == login_salvo and senha == senha_salva:
            st.success("Autenticação bem-sucedida!")
            st.balloons()
            st.markdown("---------------------------------")
            st.markdown("## Obrigado por utilizar o sistema!")
            st.markdown("## Espero que gostem. ✌︎ ✌︎ ✌︎")
            st.markdown("## Esperamos que tenha tido uma ótima experiência em nosso restaurante. 😃")
            st.markdown("# Até a próxima! 🍔🍕🍻")
            st.empty()
        else:
            st.error("Login ou senha incorretos.")
